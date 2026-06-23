
# -- Init file to tell Python that this Repo is a Package -- #

'''

The dunder method __init__.py specifies to python that this repository is a package and can be imported and used
in other python projects with the familiar from NAME.OTHERNAME import NAMES structure as long as this repo (programmingcrashcourse)
exists in your python interpreter's site-packages folder.

Author: Sean Bowman
Date:   02/20/2024

'''

from .utils import *
from .Pipe import *
# Add new classes as they are created