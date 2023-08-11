from typing import Optional, Union

import numpy as np
import torch

from qimpy import log, MPI
from qimpy.mpi import BufferView, TaskDivision
from . import spherical_bessel, quintic_spline


class RadialFunction:
    """Set of radial functions in real and reciprocal space.
    For l > 0, the convention is to remove a factor of r^l in real space (`f`)
    and G^l in reciprocal space (`f_tilde`). This makes it convenient to work with
    solid harmonics that already contain these factors of r^l or G^l.
    """

    r: torch.Tensor  #: radial grid
    dr: torch.Tensor  #: radial grid integration weights (dr in 4 pi r^2 dr)
    f: torch.Tensor  #: real-space values corresponding to r (n x len(r))
    l: torch.Tensor  #: angular momentum for each function in `f`
    DG: float = 0.02  #: reciprocal space spacing of (quintic) spline nodes
    Gmax: float  #: max G till which reciprocal space versions are current
    G: torch.Tensor  #: uniform reciprocal-space grid
    f_tilde: torch.Tensor  #: reciprocal-space version of each `f` on `G`
    f_tilde_coeff: torch.Tensor  #: quintic spline coefficients for `f_tilde`

    def __init__(
        self,
        r: torch.Tensor,
        dr: torch.Tensor,
        f: Optional[Union[np.ndarray, torch.Tensor]] = None,
        l: Optional[Union[np.ndarray, torch.Tensor]] = None,
    ) -> None:
        """Initialize real-space portion of radial function.
        Note that f should have a factor of r^l removed for correct
        subsequent behavior with transforms and solid harmonics."""
        self.r = r
        self.dr = dr
        f = (
            torch.zeros_like(r)
            if f is None
            else (
                (f if isinstance(f, torch.Tensor) else torch.tensor(f, device=r.device))
            )
        )
        self.f = f if (len(f.shape) == 2) else f[None]
        self.l = (
            torch.zeros(1, dtype=torch.int, device=r.device)
            if l is None
            else (
                l if isinstance(l, torch.Tensor) else torch.tensor(l, device=r.device)
            )
        )
        assert dr.shape == r.shape
        assert r.shape[0] == self.f.shape[-1]
        assert self.l.shape == self.f.shape[:-1]
        self.Gmax = 0  # No reciprocal space versions available yet

    @classmethod
    def transform(
        cls,
        radial_functions: list["RadialFunction"],
        Gmax: float,
        comm: MPI.Comm,
        name: str = "",
    ) -> None:
        """Initialize reciprocal space version of radial functions.
        For efficiency, perform this together on all radial functions
        that share the same radial grid (r and dr) and parallelize the
        computation over MPI communicator `comm`.
        """
        # Collect all radial functions together, dividing r over comm:
        if not radial_functions:
            return  # Nothing to do
        r_div = TaskDivision(
            n_tot=radial_functions[0].r.shape[0],
            n_procs=comm.Get_size(),
            i_proc=comm.Get_rank(),
        )
        r_slice = slice(r_div.i_start, r_div.i_stop)
        r = radial_functions[0].r[r_slice]
        dr = radial_functions[0].dr[r_slice]
        wr = (2.0 / 3) * (4 * np.pi) * (r**2 * dr)  # Simpson 1/3-rule odd weights
        wr[(r_div.i_start + 1) % 2 :: 2] *= 2.0  # ... modify to even weights
        if not r_div.i_start:
            wr[0] *= 0.5  # ... modify left end-point weight
        if (r_div.i_stop == r_div.n_tot) and r_div.n_mine:
            wr[-1] *= 0.5  # ... modify right end-point weight
        f = torch.cat([rf.f[:, r_slice] for rf in radial_functions])
        l = torch.cat([rf.l for rf in radial_functions])
        l_max = int(l.max().item())

        # Set up radial G grid:
        nG = int(np.ceil(Gmax / cls.DG)) + 5  # with sufficient margin
        G = torch.arange(nG, device=r.device) * cls.DG

        # Perform transform for each l:
        f_tilde = torch.empty((f.shape[0], nG), device=f.device)
        jl_by_Grl = spherical_bessel.jl_by_xl(l_max, r.outer(G))
        for l_i in range(0, l_max + 1):
            sel = torch.where(l == l_i)[0]
            f_tilde[sel] = (f[sel] * (r ** (2 * l_i)) * wr) @ jl_by_Grl[l_i]
        if f_tilde.is_cuda:
            torch.cuda.current_stream().synchronize()
        comm.Allreduce(MPI.IN_PLACE, BufferView(f_tilde), op=MPI.SUM)  # collect over r

        # Compute spline coefficients:
        f_tilde_coeff = quintic_spline.get_coeff(f_tilde)

        # Split results back over input radial functions:
        nf = [rf.f.shape[0] for rf in radial_functions]
        f_tilde_split = f_tilde.split(nf)
        f_tilde_coeff_split = f_tilde_coeff.split(nf, dim=1)
        for i_rf, rf in enumerate(radial_functions):
            rf.G = G
            rf.f_tilde = f_tilde_split[i_rf]
            rf.f_tilde_coeff = f_tilde_coeff_split[i_rf]
        if name:
            log.info(
                f"Transformed {f.shape[0]} radial functions for {name}"
                f" from n_r={r_div.n_tot} to nG={nG} points."
            )
