
# -- Programming Crash Course (A.K.A. I wish someone did this for me) -- #

# Python 3.10.19

'''

This directory serves as a crash course in using programming to solve problems.
The lessons taught in this introduction are intended to be used as a rapid
spin-up for individuals looking to utilize Python or other programming
languages to perform job functions. The principles discussed are focused on
a Python environment, but are generalizable to any programming language.

Top level code interfaces (or entry-points) are basically GUIs for code.
To make this crash course also an example of how I generally structure
programming projects, this directory structure is very similar to what you
would find in a design code repository. A mock-up of the comment block structure
that is used for code interfaces is recreated here for our problem:

---------------------------------------------------------------------------
# Inputs
---------------------------------------------------------------------------

Interfacing with the Pipe Pressure Drop Calculator is done through editing the
pipeProperties.csv file and making changes to the code interface here in this file.

If navigating to the repository through the Windows File Explorer, simply open the pipeProperties.csv in an
appropriate .csv editor (such as Microsoft Excel) to make the required configuration changes before a run.

If you open the .csv in VSCode (and have the RainbowCSV extension installed) you can make easy edits to values
from your VSCode environment as well.

---------------------------------------------------------------------------
## Geometry Parameters
---------------------------------------------------------------------------

Certain geometric properties of the pipe are editable by the user:

| Variable Description             |  Units |
|:--------------------------------:|-------:|
| Total Length                     |   [m]  |
| Inner Diameter                   |   [m]  |

---------------------------------------------------------------------------
## Fluid Properties
---------------------------------------------------------------------------
Certain properties of the fluid in the pipe are editable by the user:

| Variable Description              |  Units   |
|:---------------------------------:|---------:|
| Fluid Species                     | [string] |
| Inlet Temperature                 | [K]      |
| Inlet Pressure                    | [Pa]     |
| Total Mass Flow                   | [kg/s]   |

---------------------------------------------------------------------------
## Options
---------------------------------------------------------------------------

Certain functionality of the code can be disabled/enabled by entering
either 'on' or 'off' respectively for the presented options.

| Option Functionality                                  | Input Options |
|:-----------------------------------------------------:|--------------:|
| Enable/disable plotted outputs                        | 'on' , 'off'  |
| Number of pipe slices                                 | [int]         |

---------------------------------------------------------------------------
# Outputs
---------------------------------------------------------------------------

The program outputs:

- Pipe Outlet Pressure [Pa]
- Total Pressure Drop [Pa]

---------------------------------------------------------------------------
# Dependencies:
---------------------------------------------------------------------------

All files required to run the top level code are present in the working directory.
At the start of the code the relevant functions are imported as necessary.
The relevant files that live in the project subfolder 'assets' that are needed
to run this program are as follows:

- Pipe.py
- utils.py
- pipeProperties.csv

Author: Sean Bowman
Date:   12/11/2025

-----------------------------------------------------------------------------------------------------------

RUNNING THE PROGRAM:
This script can be run with any capable python 3.10 interpreter. This example script was tested using
Virtual Studio Code, downloadable from Microsoft at https://code.visualstudio.com/
The version of V.S. Code that tested this script contained the following extensions:

Extension Name (Author): Extension ID
-------------------------------------
Python (Microsoft): ms-python.python
Pylance (Microsoft): ms-python.vscode-pylance
Jupyter (Microsoft): ms-toolsai.jupyter

'''

# Import necessary functionality as well as other functions/classes we've written for this problem
import os
from assets import Pipe

os.system('cls') # Clear terminal window when running

# Instantiate a blank object called 'myPipe' from the 'Pipe' class to hold our pipe info
myPipe = Pipe()

# Set the inputs using the provided .csv file and the setInputs() method of the Pipe class
# By default the setInputs() method looks at the file located at .\assets\pipeProperties.csv
# so no inputs are required. However, if you want you can specify the filepath as an input
myPipe.setInputs(inputFilepath = '.\\assets\\pipeProperties.csv')

# Run the pressure drop calculator to calculate pressure drop given the provided properties
outletPressure, totalPressureDrop = myPipe.calculatePressureDrop()
print(f'The pipe inlet pressure was {myPipe.fluidInitialPressure: 0.1f} [Pa], and the outlet pressure ended at {outletPressure: 0.1f} [Pa], where the total pressure drop is {totalPressureDrop: 0.1f} [Pa]')
