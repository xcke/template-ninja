#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple project to template Jinja2 files from CSV.
"""

__author__ = "Gabor, Kis-Hegedus"
__version__ = "0.1.0"
__license__ = "MIT"

""" Imports """
import argparse
import re
import logging
import logzero
from logzero import logger
from methods import *
from pathlib import Path
"""Functions & Methods"""
""" Statics"""
# Disable Self-Signed Cert warning for demo urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning
templates_dir = './Templates/'
output_dir = './Output/'

def main(arg):
    if args.debug:
        logzero.loglevel(logging.DEBUG)
        logger.info("Verbose output.")
    else:
        logzero.loglevel(logging.INFO)
    logger.info("hello world!:-)")
    logger.info(args)
    logger.debug("Debug message!")
    """ Main program """
    template_filename = args.template
    input_filename = args.input
    template = load_template(templates_dir, template_filename)
    data = load_excel(input_filename)
    filename = Path(template_filename).stem + '.xml'
    with open(Path(output_dir) / filename, 'w', encoding='utf-8') as f:
        f.write(template.render(records=data))
    logger.info(f"{filename} was created in the Output folder.")


if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()

    # Required positional argument
    parser.add_argument("template", help="Name of the template from the Templates dir", default='21T1042E.j2')

    parser.add_argument("input", help="Input Excel file", default='adatbazis.xlsx')

    # Optional argument flag which defaults to False
    parser.add_argument("-D", "--debug", action="store_true", default=False)

    # Optional argument which requires a parameter (eg. -d test)
    parser.add_argument("-n", "--name", action="store", dest="name")

    # Optional verbosity counter (eg. -v, -vv, -vvv, etc.)
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="Verbosity (-v, -vv, etc)")

    # Specify output of "--version"
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
    main(args)