
# -- Pipe Class Definition Example -- #

'''

This class is an example for how to build a class structure in Python.

In this example we will build a 'Pipe' object and use the object structure
to calculate the pressure drop of a fluid flowing in the pipe due to friction.

Built with Python 3.10.19 in VSCode

Author: Sean Bowman
Date:   12/11/2025

'''

# Global class imports
import numpy as np
import matplotlib.pyplot as plt

# Here the python file utils.py is preceeded with a '.' because it is being referenced locally from within the 'assets' subfolder.
# This is important because if you just wrote 'import utils' Python would look for a globally installed package called 'utils' instead of
# the local file. By using the relative pathing with the '.' we ensure that Python looks in the current folder for the file.
from .utils import RefWrap, plotLine

class Pipe:

    # The 'dunder' method __init__() is called a constructor in other languages, and is run first whenever a class is instantiated.
    # This step can technically contain nothing, but as a matter of coding style, pre-define object properties here.
    # This means that we can pre-specify a bunch of object properties that we want to keep track of so that the object has a list
    # of 'defaults' so-to-speak. You can always add properties on later (that process is called 'monkey patching') but I like
    # to keep my properties organized and give things I intend to calculate down the line and save a home before they're calculated.
    def __init__(self):

        # -- Geometric Properties -- #

        self.length           = [] # [m]
        self.innerDiameter    = [] # [m]

        # -- Fluid Properties -- #

        self.fluid                   = [] # [case insensitive string]
        self.fluidInitialTemperature = [] # [K]
        self.fluidInitialPressure    = [] # [Pa]
        self.totalMassFlow           = [] # [kg/s]

        # -- Options -- #

        self.plots     = [] # 'on' or 'off'
        self.numSlices = [] # [int]

    #---------------------------------#
    # -- Public Methods -- #
    #---------------------------------#

    # Public methods are accessible by the user in whatever their code interface is. That means a user with a
    # 'Pipe' object can call a public method to perform some action. Private methods are nested within public
    # methods, and act like public method helpers, but are not directly callable by a user.
    # Sometimes private methods are called 'internal methods' as well, and are often prefixed with an underscore

    # This method will handle setting the object's properties using the config file
    def setInputs(self, inputFilepath: str = '.\\assets\\pipeProperties.csv') -> None:

        '''
        
        This function sets the object properties according to a .csv config file. Only the path
        to the .csv file needs to be specified, and the default file path is:
        
            .\\assets\\pipeProperties.csv

        The fields of the config file can be arranged in an arbitrary order, so long as the fill
        fields have the same names as given in the example config file.
        
        '''

        # Locally import pandas to read config
        import pandas as pd
        
        # Read the .csv in using pandas
        inputs = pd.read_csv(inputFilepath)

        # Read config by matching setting name from config file
        # This loop uses a process called 'enumerate'. What this does is look at an array
        # and create an iterable variable over the array length. The second output of enumerate
        # is the value that is stored in the array itself. Here we are throwing that away with the
        # dummy variable '_' instead of using it.
        for i, _ in enumerate(inputs.values):
            
            # Here we are implementing a switch-case statement (called 'match-case' in Python for some reason)
            # which is kinda like an if-else statement but evaluates much faster. If-else statements evaluate top-to-bottom
            # requiring a boolean True or False to be spit out of each evaluation. This means that many math operations may happen
            # in sequence (if you had a statement like if x > 2 for example) that occur top-down until your condition is found.
            # It is much more efficient to just compare cases and here we are comparing to the string stored in the named column in the .csv
            # This is still essentially a boolean comparison, however there is only one operation per step (seeing what is stored in the 
            # match part of the statement) instead of running through the entire if-elif-else list every time.

            match inputs.values[i][0]:

                # -- Pipe Properties -- # inputs.values[i][1]

                # Geometry Properties
                case 'Total Pipe Length':
                    self.length                  = float(inputs.values[i][1])
                case 'Pipe Inner Diameter':
                    self.innerDiameter           = float(inputs.values[i][1])

                # Fluid Properties
                case 'Fluid':
                    self.fluid                   = inputs.values[i][1]
                case 'Initial Temperature':
                    self.fluidInitialTemperature = float(inputs.values[i][1])
                case 'Initial Pressure':
                    self.fluidInitialPressure    = float(inputs.values[i][1])
                case 'Total Mass Flow':
                    self.totalMassFlow           = float(inputs.values[i][1])

                # Options
                case 'Plots':
                    self.plots                   = inputs.values[i][1]
                case 'Number of Pipe Slices':
                    self.numSlices               = int(inputs.values[i][1])

    # This method will handle the calculation of pressure drop. Here I specified a boolean flag called 'justOutletPressure'
    # and gave it a default value of False, which we will discuss at the end of the function. Of note: variable typing
    # in Python is not enforced, so the typing tag ': bool' is meaningless from a code interpreter perspective. It just helps the
    # user know what is expected to go there. This also applies to the return hint '-> float | tuple[float,float]' which
    # is just a helpful hint to the user of what to expect this function to return. Type hints are not required, but they are
    # nice and professional. Default values can also be specified here (such as = False) but values with defaults
    # must all come after variables that do not have defaults specified. Un-specified arguments are called 'positional'
    # and the compiler gets upset if the wrong number are specified when a function gets called.
    def calculatePressureDrop(self, justOutletPressure: bool = False) -> float | tuple[float,float]:

        '''

        Calculate pressure drop in a straight pipe broken into 'n' slices using Darcy-Weisbach equation.

        '''

        # Initialize arrays with a list comprehension
        # List comprehensions are like little loops within lists. That means we can repeat an operation
        # and store the result in a list all in one line. The structure looks like:
        # [thingToRepeat for iterator in range(numberOfThingsToRepeat)]
        # Which makes 'numberOfThingsToRepeat' copies of the piece 'thingToRepeat' and saves them in a list.
        # If you unpack the list right away (by writing multiple variables as an output) then this operation
        # creates 'numberOfThingsToRepeat' different outputs
        numPreAllocatedArrays = 7
        pressure, frictionFactor, density, dynamicViscosity, \
        velocity, reynoldsNumber, pressureDrop \
        = [np.zeros(self.numSlices) for _ in range(numPreAllocatedArrays)]

        # Assign the inlet pressure to the first element of the pressure array. Python arrays start at 0.
        pressure[0] = self.fluidInitialPressure

        # Calculate dependent constant properties
        pipeAxis = np.linspace(0, self.length, self.numSlices)
        segmentLength = self.length / self.numSlices
        crossSectionalArea = np.pi*(self.innerDiameter / 2)**2

        # Now we loop over the pipe slices and calculate pressure drop at each slice. This is a bit more accurate than just
        # calculating the pressure drop across the entire pipe all at once, and it is really easy to implement in code.
        # Here we want to stop before we reach the end of the pipe because we will be updating the downstream pressure
        # with information from the upstream properties, meaning once we get to the end of the pipe our last step would 
        # land us outside of the defined domain.
        for i in range(self.numSlices - 1):

            # Step 1: Get fluid properties from REFPROP at the current temperature (held constant) and pressure
            density[i], dynamicViscosity[i] = RefWrap(self.fluid, 'TP', 'D VIS', self.fluidInitialTemperature, pressure[i])

            # Step 2: Calculate incompressible fluid velocity and Reynolds Number
            velocity[i]       = self.totalMassFlow / (density[i] * crossSectionalArea)
            reynoldsNumber[i] = density[i] * velocity[i] * self.innerDiameter / dynamicViscosity[i]

            # Step 3: Calculate friction factor using Gneilinski correlation for turbulent internal flows
            frictionFactor[i] = (0.79 * np.log(reynoldsNumber[i]) - 1.64)**-2

            # Step 4: Use Darcy-Weisbach equation to calculate the pressure drop given friction factor
            pressureDrop[i]   = frictionFactor[i] * segmentLength * density[i] * velocity[i]**2 / (2 * self.innerDiameter)

            # Step 5: Update the pressure at the next pipe slice
            pressure[i+1]     = pressure[i] - pressureDrop[i]

            # Now re-run the loop using the new pressure to find the new fluid properties and iterate over the entire domain

        # With the loop completed, we have the outlet properties of the pipe
        # The outlet pressure is the last pressure element. In Python you can grab the end of an array by indexing the -1st element.
        # This works further into the negatives as well, the -2nd element is the 2nd from last and so on.
        outletPressure = pressure[-1]
        # Another fun thing about object-oriented languages is that they usually support cascading operations. This means methods run left-to-right
        # and you can simply do two things at once. Here we are calculating the cumulative sum of pressure drops using numpy's cumsum() function.
        # This array increases as you move through the array, but we want the total cumulative sum which is at the end of this array. So let's
        # just index the last element off right afterwards and do it all at once.
        totalPressureDrop = np.cumsum(pressureDrop)[-1]

        # Make plots if the user specifies to. Here we force the value stored in the 'plots' property to be all lowercase
        # so that it will evaluate to True regardless of the casing of the original string.
        if self.plots.lower() == 'on':

            # Assign array endpoints for plotting for arrays that didn't get their last element calculated
            # Set i to be -1 so that we can do the loop structure again but assign the end of every array
            i = -1
            # Step 1: Get fluid properties from REFPROP at the current temperature (held constant) and pressure
            density[i], dynamicViscosity[i] = RefWrap(self.fluid, 'TP', 'D VIS', self.fluidInitialTemperature, pressure[i])

            # Step 2: Calculate incompressible fluid velocity and Reynolds Number
            velocity[i]       = self.totalMassFlow / (density[i] * crossSectionalArea)
            reynoldsNumber[i] = density[i] * velocity[i] * self.innerDiameter / dynamicViscosity[i]

            # Step 3: Calculate friction factor using Gneilinski correlation for turbulent internal flows
            frictionFactor[i] = (0.79 * np.log(reynoldsNumber[i]) - 1.64)**-2

            # Step 4: Use Darcy-Weisbach equation to calculate the pressure drop given friction factor
            pressureDrop[i]   = frictionFactor[i] * segmentLength * density[i] * velocity[i]**2 / (2 * self.innerDiameter)

            # plotLine is a plotting wrapper that I wrote that *hopefully* makes the formatting of plotting easier. Everything can
            # be passed in to this function as an input instead of writing lots of formatting lines. Check out the function description for
            # a list of the options for changing up the plots, or plot manually yourself if you're comfortable with that.
            plotLine(pipeAxis, pressure, \
                        title = 'Pressure vs. Pipe Axis', xLabel = 'Pipe Axis [m]', yLabel = 'Pressure [Pa]', \
                        color = 'g', lineStyle = '-', lineWidth = 2, markerStyle = '*', markerSize = 6, \
                        label = 'Pressure', fontSize = 14)
            plt.legend()

            plotLine(pipeAxis, pressureDrop, \
                        title = 'Pressure Drop vs. Pipe Axis', xLabel = 'Pipe Axis [m]', yLabel = 'Pressure Drop [Pa]', \
                        color = 'r', lineStyle = '--', lineWidth = 2, markerStyle = '1', markerSize = 6, \
                        label = 'Pressure Drop', fontSize = 14)
            plt.legend()

        # Tell the function what values to spit back at the user. This generally happens at the end of the function, but technically the return statement can exist anywhere in the function.
        # Also, because return is just an action (similar to for, while, if,  etc) you can also hide it within conditional statements to make your function return different things
        # in different situations. Here we didn't specify and the default value is False so we will get them all, but the user could optionally ask for just outlet pressure for some reason.
        if justOutletPressure is True:
            return outletPressure
        else:
            return outletPressure, totalPressureDrop
