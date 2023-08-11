import argparse
import sys
import os

import qimpy
from qimpy import log, rc, io
from qimpy.rc import MPI
from qimpy.profiler import StopWatch
from . import Transport


def main():
    """Stand-alone QimPy transport calculation from YAML input file

    Typical usage:

    :code:`mpirun [mpi-options] python -m qimpy.transport -i INPUT_FILE [qimpy-options]`

    Command-line parameters (obtained using :code:`python -m qimpy.run -h`):

    .. code-block:: bash

        python -m qimpy.transport (-h | -v | -i FILE) [-o FILE] [-c C] [-p Pr Pk]
                               [-n] [-d] [-m FILE] [-V]

    optional arguments:

    Run a QimPy transport calculation from an input file
      -h, --help            show this help message and exit
      -v, --version         print version information and quit
      -i FILE, --input-file FILE
                            input file in YAML format
      -o FILE, --output-file FILE
                            output file (stdout if unspecified)
      -c C, --cores C       number of cores per process (overridden by SLURM)

      -p Pr Pk, --process-grid Pr Pk
                            dimensions of process grid: real-space x kpoints, whose
                            product must match process count; any -1 will be set to
                            distribute available tasks for that dimension most equally.
                            Default: -1 -1 implies all dimensions set automatically.

      -n, --dry-run         quit after initialization (to check input file)
      -d, --no-append       overwrite output file instead of appending
      -m FILE, --mpi-log FILE
                            file prefix for debug logs from other MPI processes
      -V, --verbose         print extra information in log for debugging


    Note that qimpy must be installed to the python path for these to work in any
    directory. For development, run `python setup.py develop --user` in the root
    directory of the source repository to make the above usage possible without
    instaling from pip/conda.
    """
    # Parse the commandline arguments on main process:
    i_proc = MPI.COMM_WORLD.Get_rank()
    if i_proc == 0:

        # Set terminal size (used by argparse) if unreasonable:
        columns_min = 80
        try:
            if os.get_terminal_size().columns < columns_min:
                os.environ["COLUMNS"] = str(columns_min)
        except OSError:
            os.environ["COLUMNS"] = str(columns_min)

        # Modify ArgumentParser to not exit:
        class ArgumentParser(argparse.ArgumentParser):
            def error(self, message):
                self.print_usage(sys.stderr)
                print(f"{self.prog}: error: {message}\n", file=sys.stderr)
                raise ValueError(message)  # Quit after bcast'ing error

        parser = ArgumentParser(
            add_help=False,
            prog="python -m qimpy.transport",
            description="Run a QimPy transport calculation from an input file",
        )
        # --- mutually-exclusive group of help, version or input file
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument(
            "-h", "--help", action="store_true", help="show this help message and exit"
        )
        group.add_argument(
            "-v",
            "--version",
            action="store_true",
            help="print version information and quit",
        )
        group.add_argument(
            "-i", "--input-file", metavar="FILE", help="input file in YAML format"
        )
        # ---
        parser.add_argument(
            "-o",
            "--output-file",
            metavar="FILE",
            help="output file (stdout if unspecified)",
        )
        parser.add_argument(
            "-c",
            "--cores",
            type=int,
            metavar="C",
            help="number of cores per process (overridden by SLURM)",
        )
        parser.add_argument(
            "-p",
            "--process-grid",
            type=int,
            nargs=2,
            default=[-1, -1],
            metavar=("Pr", "Pk"),
            help="dimensions of process grid: real-space x kpoints"
            ", whose product must match process count; any -1 will be set to "
            "distribute available tasks for that dimension most equally. "
            "Default: -1 -1 implies all dimensions set automatically.",
        )
        parser.add_argument(
            "-n",
            "--dry-run",
            action="store_true",
            help="quit after initialization (to check input file)",
        )
        parser.add_argument(
            "-d",
            "--no-append",
            action="store_true",
            help="overwrite output file instead of appending",
        )
        parser.add_argument(
            "-m",
            "--mpi-log",
            metavar="FILE",
            help="file prefix for debug logs from other MPI processes",
        )
        parser.add_argument(
            "-V",
            "--verbose",
            action="store_true",
            help="print extra information in log for debugging",
        )
        try:
            args = parser.parse_args()
            setattr(args, "error_occured", False)
        except ValueError:
            args = argparse.Namespace()
            setattr(args, "error_occured", True)
    else:
        args = argparse.Namespace()

    # Make commandline arguments available on all processes:
    args = MPI.COMM_WORLD.bcast(args, root=0)
    if args.error_occured:
        exit()  # exit all processes

    if args.version:
        # Print version and exit:
        if i_proc == 0:
            print("QimPy", qimpy.__version__)
        exit()

    if args.help:
        # Print help and exit:
        if i_proc == 0:
            parser.print_help()
        exit()

    # Setup logging:
    io.log_config(
        output_file=args.output_file,
        mpi_log=args.mpi_log,
        mpi_comm=MPI.COMM_WORLD,
        append=(not args.no_append),
        verbose=args.verbose,
    )

    # Print version header
    log.info("*" * 15 + " QimPy " + qimpy.__version__ + " " + "*" * 15)

    # Configure hardware resources
    rc.init(cores_override=args.cores)

    # Load input parameters from YAML file:
    input_dict = io.dict.key_cleanup(io.yaml.load(args.input_file))
    # --- Set default checkpoint file (if not specified in input):
    input_dict.setdefault("checkpoint", os.path.splitext(args.input_file)[0] + ".h5")
    # --- Include processed input in log:
    log.info(f"\n# Processed input:\n{io.yaml.dump(input_dict)}")
    input_dict = io.dict.remove_units(input_dict)  # Remove units

    # Initialize system with input parameters:
    transport = Transport(process_grid_shape=args.process_grid, **input_dict)

    # Dry-run bypass:
    if args.dry_run:
        log.info("Dry run initialization successful: input is valid.")
        rc.report_end()
        StopWatch.print_stats()
        exit()

    # Perform specified actions:
    transport.run()

    # Report timings:
    rc.report_end()
    StopWatch.print_stats()
