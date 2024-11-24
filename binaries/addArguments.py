#!/bin/python
""" Main function to parse arguments to a command
"""
import argparse
import subprocess
import sys
import re


def main():
    """Main function for CLI execution"""

    parser = argparse.ArgumentParser(description="Lightweight wrapper")
    parser.add_argument(
        "--bin-path",
        help="Path to the binary",
        dest="bin_path",
        required=True
    )
    parser.add_argument(
        "--work-dir",
        help="Directory to execute command in",
        dest="work-dir",
        required=True
    )
    parser.add_argument(
        "--command",
        help="Command to run",
        dest="command",
        required=True
    )
    parser.add_argument(
        "--args",
        nargs="+",
        help="command line arguments, NOTE: supply args like so:\
            --args=-var a=b -var foo=bar. you must supply as --tf-args=\
            initially due to the nature of arparser.",
        dest="extra_parameters"
    )
    parser.add_argument(
        "--other-options",
        nargs="+",
        help="Options to pass at command execution",
        dest="other_options",
        default=False
    )
    
    environment_group = parser.add_mutually_exclusive_group()
    environment_group.add_argument(
        "--env",
        help="environment variables for cloud authentication",
        dest="env"
    )
    environment_group.add_argument(
        "--user-name",
        help="environment variables for cloud authentication",
        dest="env"
    )


if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(main())