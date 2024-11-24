#!/bin/python
# v.iroshan

import argparse
import sys
import re
import subprocess


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--bin-path",
        help = "Path to the binary",
        dest = "bin_path",
        required = True
    )
    parser.add_argument(
        "--work-dir",
        help = "Directory to execute command in",
        dest = "work_dir",
        default=""
    )
    parser.add_argument(
        "--command",
        help = "Command to run",
        dest = "command",
        required = True
    )
    parser.add_argument(
        "--args",
        nargs = "+",
        help = "command line arguments, NOTE: supply args like so:\
            --args=-var a=b -var foo=bar. you must supply as --args=\
            initially due to the nature of argparse.",
        dest = "extra_parameters"
    )
    
    environment_group = parser.add_mutually_exclusive_group()
    environment_group.add_argument(
        "--env",
        help = "environment variables for authentication",
        dest = "env"
    )
    environment_group.add_argument(
        "--username",
        help = "username for authentication",
        dest = "env"
    )

    environment_group.add_argument(
        "--password",
        help = "password for authentication",
        dest = "password"
    )

    args, other_options = parser.parse_known_args()
    if other_options:
        args.extra_parameters.extend(other_options)

    try:
        run_command = f"{args.bin_path} {args.command} {args.work_dir} {args.extra_parameters}"
        output = subprocess.check_output(run_command, shell=True, text=True)
        print(output)
    except subprocess.CalledProcessError as Error:
        print("Error:\n")
        print(Error.stderr)
        sys.exit(1)


if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(main())
