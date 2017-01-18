"""
Greenart draws image on your github green panel

Usage:
  greenart <image_filename>

Example:
  greenart image.jpg
"""

import sys
from docopt import docopt
from .image import Image
from . import __version__


def main():
    arguments = docopt(__doc__, version=__version__)

    filename = arguments['<image_filename>']
    image = Image(filename)

    commands = image.get_commands()

    for command in commands:
        print(command)
