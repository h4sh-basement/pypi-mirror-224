"""Geometry actions: relaxation and dynamics."""
from __future__ import annotations
from typing import Union, Protocol, Callable, Optional

import torch

from qimpy import rc, TreeNode
from qimpy.io import CheckpointPath, CheckpointContext, Unit, UnitOrFloat
from qimpy.mpi import BufferView
from qimpy.dft import geometry
from ._gradient import Gradient

# List exported symbols for doc generation
__all__ = (
    "Thermostat",
    "ThermostatMethod",
    "NVE",
    "NoseHoover",
    "Berendsen",
    "Langevin",
)


class Thermostat(TreeNode):
    """Select between possible geometry actions."""

    method: ThermostatMethod

    def __init__(
        self,
        *,
        dynamics: geometry.Dynamics,
        checkpoint_in: CheckpointPath = CheckpointPath(),
        nve: Union[dict, NVE, None] = None,
        nose_hoover: Union[dict, NoseHoover, None] = None,
        berendsen: Union[dict, Berendsen, None] = None,
        langevin: Union[dict, Langevin, None] = None,
    ) -> None:
        """Specify one of the supported thermostat methods.
        Defaults to `NVE` if none specified.

        Parameters
        ----------
        nve
            :yaml:`No thermostat (or barostat), i.e. NVE ensemble.`
        nose_hoover
            :yaml:`Nose-Hoover thermostat and/or barostat.`
        berendsen
            :yaml:`Berendsen velocity-rescaling thermostat and/or barostat.`
        langevin
            :yaml:`Langevin stochastic thermostat and/or barostat.`
        """
        super().__init__()
        ChildOptions = TreeNode.ChildOptions
        self.add_child_one_of(
            "method",
            checkpoint_in,
            ChildOptions("nve", NVE, nve, dynamics=dynamics),
            ChildOptions("nose_hoover", NoseHoover, nose_hoover, dynamics=dynamics),
            ChildOptions("berendsen", Berendsen, berendsen, dynamics=dynamics),
            ChildOptions("langevin", Langevin, langevin, dynamics=dynamics),
            have_default=True,
        )


class ThermostatMethod(Protocol):
    """Class requirements to use as a thermostat method."""

    def step(self, velocity: Gradient, acceleration: Gradient, dt: float) -> Gradient:
        """Return velocity after `dt`, given current `velocity` and `acceleration`."""

    def initialize_gradient(self, gradient: Gradient) -> None:
        """Initialize optional terms in `gradient` needed by this thermostat to zero."""

    def get_velocity(self, velocity: Gradient) -> None:
        """Get optional velocity components used by this thermostat in `velocity`."""

    def set_velocity(self, velocity: Gradient) -> None:
        """Set optional velocity components used by this thermostat from `velocity`."""


class NVE(TreeNode):
    """No thermostat (or barostat), i.e. NVE ensemble."""

    dynamics: geometry.Dynamics

    def __init__(
        self,
        *,
        dynamics: geometry.Dynamics,
        checkpoint_in: CheckpointPath = CheckpointPath(),
    ) -> None:
        super().__init__()
        self.dynamics = dynamics

    def step(self, velocity: Gradient, acceleration: Gradient, dt: float) -> Gradient:
        """Return velocity after `dt`, given current `velocity` and `acceleration`."""
        return velocity + acceleration * dt

    def initialize_gradient(self, gradient: Gradient) -> None:
        """No optional `gradient` terms for this thermostat method."""

    def get_velocity(self, velocity: Gradient) -> None:
        """No optional velocity components for this thermostat method."""

    def set_velocity(self, velocity: Gradient) -> None:
        """No optional velocity components for this thermostat method."""


class NoseHoover(TreeNode):
    """Nose-Hoover thermostat and/or barostat."""

    dynamics: geometry.Dynamics
    chain_length_T: int  #: Nose-Hoover chain length for thermostat
    chain_length_P: int  #: Nose-Hoover chain length for barostat
    thermostat_velocity: torch.Tensor  #: Velocity of extra thermostat DOFs
    barostat_velocity: Optional[torch.Tensor]  #: Velocity of extra barostat DOFs

    def __init__(
        self,
        *,
        dynamics: geometry.Dynamics,
        chain_length_T: int = 3,
        chain_length_P: int = 3,
        checkpoint_in: CheckpointPath = CheckpointPath(),
    ) -> None:
        """
        Specify thermostat parameters.

        Parameters
        ----------

        chain_length_T
            :yaml:`Nose-Hoover chain length for thermostat.`
        chain_length_P
            :yaml:`Nose-Hoover chain length for barostat.`
        """
        super().__init__()
        self.dynamics = dynamics
        assert chain_length_T >= 3
        assert chain_length_P >= 3
        if checkpoint_in:
            attrs = checkpoint_in.attrs
            self.chain_length_T = attrs["chain_length_T"]
            self.chain_length_P = attrs["chain_length_P"]
            self.thermostat_velocity = checkpoint_in.read("thermostat_velocity")
            self.barostat_velocity = checkpoint_in.read_optional("barostat_velocity")
        else:
            self.chain_length_T = chain_length_T
            self.chain_length_P = chain_length_P
            self.thermostat_velocity = torch.zeros(chain_length_T, device=rc.device)
            self.barostat_velocity = None

    def _save_checkpoint(
        self, cp_path: CheckpointPath, context: CheckpointContext
    ) -> list[str]:
        attrs = cp_path.attrs
        attrs["chain_length_T"] = self.chain_length_T
        attrs["chain_length_P"] = self.chain_length_P
        saved_list = ["chain_length_T", "chain_length_P", "thermostat_velocty"]
        cp_path.write("thermostat_velocity", self.thermostat_velocity)
        if self.barostat_velocity is not None:
            cp_path.write("barostat_velocity", self.barostat_velocity)
            saved_list.append("barostat_velocity")
        return saved_list

    def extra_acceleration(self, velocity: Gradient) -> Gradient:
        """Extra velocity-dependent acceleration due to thermostat/barostat."""
        dynamics = self.dynamics
        nDOF = dynamics.nDOF

        # Damp ionic velocities due to thermostat coupling:
        assert velocity.thermostat is not None
        gamma = velocity.thermostat[0]
        acceleration = dynamics.create_gradient(-gamma * velocity.ions)

        # Coupling to previous thermostat DOF / system:
        T = dynamics.get_T(dynamics.get_KE(velocity.ions))
        omega_sq = (1.0 / dynamics.t_damp_T) ** 2
        assert acceleration.thermostat is not None
        acceleration.thermostat[0] = omega_sq * (T / dynamics.T0 - 1.0)
        acceleration.thermostat[1] = nDOF * (velocity.thermostat[0] ** 2) - omega_sq
        acceleration.thermostat[2:] = (velocity.thermostat[1:-1] ** 2) - omega_sq

        # Coupling to next thermostat DOF:
        acceleration.thermostat[:-1] -= (
            velocity.thermostat[:-1] * velocity.thermostat[1:]
        )

        lattice = dynamics.system.lattice
        if lattice.movable:
            n_free_L = 1 if dynamics.isotropic else 3  # TODO: lattice constraint DOFs
            nDOF_L = (n_free_L * (n_free_L + 1)) // 2

            # Ionic acceleration due to strain rate:
            assert velocity.lattice is not None
            gamma_extra = torch.trace(velocity.lattice) / nDOF
            acceleration.ions -= velocity.ions * gamma_extra
            acceleration.ions -= velocity.ions @ velocity.lattice.T

            # Lattice acceleration due to barostat coupling:
            omega_sq_L = (1.0 / dynamics.t_damp_P) ** 2
            dstress = dynamics.stress0 - dynamics.get_stress(velocity.ions)
            assert velocity.barostat is not None
            acceleration.lattice = (omega_sq_L / ((nDOF + n_free_L) * dynamics.T0)) * (
                lattice.volume * dstress + T * torch.eye(3, device=rc.device)
            ) - velocity.barostat[0] * velocity.lattice

            # Coupling to previous barostat DOF / system:
            assert acceleration.barostat is not None
            acceleration.barostat[0] = (
                (nDOF + n_free_L) / nDOF_L
            ) * velocity.lattice.square().sum() - omega_sq_L
            acceleration.barostat[1] = nDOF_L * (velocity.barostat[0] ** 2) - omega_sq_L
            acceleration.barostat[2:] = (velocity.barostat[1:-1] ** 2) - omega_sq_L

            # Coupling to next barostat DOF:
            acceleration.barostat[:-1] -= velocity.barostat[:-1] * velocity.barostat[1:]

        return acceleration

    def step(self, velocity: Gradient, acceleration: Gradient, dt: float) -> Gradient:
        """Return velocity after `dt`, given current `velocity` and `acceleration`."""
        return second_order_step(velocity, acceleration, self.extra_acceleration, dt)

    def initialize_gradient(self, gradient: Gradient) -> None:
        """Initialize `thermostat` and, if needed, `barostat` terms in `gradient`."""
        gradient.thermostat = torch.zeros(self.chain_length_T, device=rc.device)
        if self.dynamics.system.lattice.movable:
            gradient.barostat = torch.zeros(self.chain_length_P, device=rc.device)

    def get_velocity(self, velocity: Gradient) -> None:
        """Get `thermostat` and optional `barostat` components within `velocity`."""
        velocity.thermostat = self.thermostat_velocity
        if self.barostat_velocity is not None:
            velocity.barostat = self.barostat_velocity

    def set_velocity(self, velocity: Gradient) -> None:
        """Set `thermostat` and optional `barostat` components from `velocity`."""
        assert velocity.thermostat is not None
        self.thermostat_velocity = velocity.thermostat
        if velocity.barostat is not None:
            self.barostat_velocity = velocity.barostat


class Berendsen(TreeNode):
    """Berendsen velocity-rescaling thermostat and/or barostat."""

    dynamics: geometry.Dynamics

    def __init__(
        self,
        *,
        dynamics: geometry.Dynamics,
        B0: UnitOrFloat = Unit(2.2, "GPa"),
        checkpoint_in: CheckpointPath = CheckpointPath(),
    ) -> None:
        """
        Specify thermostat parameters.

        Parameters
        ----------

        B0
            :yaml:`Characteristic bulk modulus for Berendsen barostat.`
            Default value corresponds to water, which should be acceptable for
            typical liquid simulations, but maybe too small for most solids.
            Make sure to set correct order of magnitude of `B0` in order for
            pressure to be equilibrated on the expected `t_damp_P` time scale.
        """
        super().__init__()
        self.dynamics = dynamics
        self.B0 = checkpoint_in.attrs["B0"] if checkpoint_in else float(B0)

    def _save_checkpoint(
        self, cp_path: CheckpointPath, context: CheckpointContext
    ) -> list[str]:
        cp_path.attrs["B0"] = self.B0
        return ["B0"]

    def extra_acceleration(self, velocity: Gradient) -> Gradient:
        """Extra velocity-dependent acceleration due to thermostat/barostat."""
        dynamics = self.dynamics
        T = dynamics.get_T(dynamics.get_KE(velocity.ions))
        gamma = 0.5 * (T / dynamics.T0 - 1.0) / dynamics.t_damp_T
        acceleration = Gradient(ions=(-gamma * velocity.ions))
        # Optional barostat contributions:
        if dynamics.system.lattice.movable:
            dstress = dynamics.stress0 - dynamics.get_stress(velocity.ions)
            strain_rate = dstress / (dynamics.t_damp_P * self.B0)
            velocity.lattice = strain_rate
            acceleration.ions -= velocity.ions @ strain_rate.T
            acceleration.lattice = torch.zeros_like(strain_rate)
        return acceleration

    def step(self, velocity: Gradient, acceleration: Gradient, dt: float) -> Gradient:
        """Return velocity after `dt`, given current `velocity` and `acceleration`."""
        return second_order_step(velocity, acceleration, self.extra_acceleration, dt)

    def initialize_gradient(self, gradient: Gradient) -> None:
        """No optional `gradient` terms for this thermostat method."""

    def get_velocity(self, velocity: Gradient) -> None:
        """No optional velocity components for this thermostat method."""

    def set_velocity(self, velocity: Gradient) -> None:
        """No optional velocity components for this thermostat method."""


class Langevin(TreeNode):
    """Langevin stochastic thermostat and/or barostat."""

    dynamics: geometry.Dynamics

    def __init__(
        self,
        *,
        dynamics: geometry.Dynamics,
        checkpoint_in: CheckpointPath = CheckpointPath(),
    ) -> None:
        super().__init__()
        self.dynamics = dynamics

    def extra_acceleration(self, velocity: Gradient) -> Gradient:
        """Extra velocity-dependent acceleration due to thermostat."""
        return velocity * (-1.0 / self.dynamics.t_damp_T)

    def step(self, velocity: Gradient, acceleration: Gradient, dt: float) -> Gradient:
        """Return velocity after `dt`, given current `velocity` and `acceleration`."""
        dynamics = self.dynamics
        # Generate MPI-consistent stochastic acceleration (not velocity dependent):
        rand = torch.randn_like(velocity.ions)
        self.dynamics.comm.Bcast(BufferView(rand))
        variances = 2 * dynamics.T0 / (dynamics.masses * (dynamics.t_damp_T * dt))
        acceleration_noise = Gradient(ions=(rand * variances.sqrt()))
        # Take step including velocity-dependent damping:
        return second_order_step(
            velocity, acceleration + acceleration_noise, self.extra_acceleration, dt
        )

    def initialize_gradient(self, gradient: Gradient) -> None:
        """No optional `gradient` terms for this thermostat method."""

    def get_velocity(self, velocity: Gradient) -> None:
        """No optional velocity components for this thermostat method."""

    def set_velocity(self, velocity: Gradient) -> None:
        """No optional velocity components for this thermostat method."""


def second_order_step(
    velocity: Gradient,
    acceleration0: Gradient,
    acceleration: Callable[[Gradient], Gradient],
    dt: float,
) -> Gradient:
    """
    Integrate dv/dt = acceleration0 + acceleration(v) over dt to second order.
    Start from v = velocity at time t, and return velocity at t+dt.
    """
    velocity_half = velocity + (acceleration0 + acceleration(velocity)) * (0.5 * dt)
    return velocity + (acceleration0 + acceleration(velocity_half)) * dt
