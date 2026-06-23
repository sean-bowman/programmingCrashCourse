
# -- Example Utilities file for Crash Course -- #

'''

This utilities python file serves as a function repository that can be added to any python project to
quickly access commonly used functions.

These functions are:

> RefWrap
    >> Pull fluid thermophysical properties from the REFPROP EOS model
> plotLine
    >> Wrapper for matplotlib 2D line plots

Author: Sean Bowman
Date:   01/24/2024

'''

import os
import numpy as np
import matplotlib.pyplot as plt

# -- Weird imports that people might not have -- #

# ctREFPROP (This needs to be a global import instead of a nested local import because RefWrap sometimes
# is called within a loop and re-importing this module each time RefWrap is called makes it take FOREVER)
try:
    from ctREFPROP.ctREFPROP import REFPROPFunctionLibrary
except:
    # raise Exception(f'Uh oh, ctREFPROP isn\'t found. You can to pip install that with \'pip install -U ctREFPROP\'')
    print(f'Uh oh, ctREFPROP isn\'t found. You won\'t be able to call REFPROP. You can to pip install that with \'pip install -U ctREFPROP\'')

def RefWrap(species: str, inputTypes: str, outputTypes: str, inputTypeFirst: float, inputTypeSecond: float, mixtureRatio: tuple[float,...] = [1.0], units: bool = False) -> float | tuple[float] | str | tuple[str]:

    '''
    
    This function acts as a simple wrapper for REFPROP.

    The function structures the input to the python REFPROP extension in such a
    way that the wrapping function can be easily structured in the following
    format:

    ---------------------------------------------------------------------------
                                    INPUTS
    ---------------------------------------------------------------------------
    - Fluid Species                                   [case insensitive string]

    - Input Types         [case insensitive string of 2 values (no delimiters)]
        Supported Inputs:
        + 'T'                                    specifying fluid [Temperature]
        + 'P'                                       specifying fluid [Pressure]
        + 'D'                                        specifying fluid [Density]
        + 'E'                                specifying fluid [Internal Energy]
        + 'H'                                       specifying fluid [Enthalpy]
        + 'S'                                        specifying fluid [Entropy]
        + 'Q'                                        specifying fluid [Quality]
        i.e. 'TP' specifies [Temperature,Pressure] inputs

    - Output Types                    [space delimited case insensitive string]
        Supported input list can be found in REFPROP DOCUMENTATION (link
        below)
        i.e. 'D Cp Cp/Cv' specifies [density , specific heat , gamma] outputs

    - First Input Type                                           [Mass Base SI]
        i.e. for 'TP' input types, this input will be Temeprature [K]

    - Second Input Type                                          [Mass Base SI]
        i.e. for 'TP' input types, this input will be Pressure [Pa]

    ***NOTE:
    All input types are presented in [Mass Base SI] units i.e. [K , Pa , kg/m^3 , etc]

    ---------------------------------------------------------------------------
                                OPTIONAL INPUTS
    ---------------------------------------------------------------------------
    - Mixture ratio
        + If the fluid species being passed in is a mixture of 2 or more fluids
          the optional input 'mixtureRatio' may be passed in to specify the
          mixture ratio.
    
    - Units
        + If the user wants to return the units of the relevant property instead
          of the value of the property itself the 'units' value can be set to
          the boolean True.

    ---------------------------------------------------------------------------
                                    OUTPUTS
    ---------------------------------------------------------------------------
    RefWrap can handle an arbitrary number of outputs, saved in the order that
    the outputs are specified.

    Example function call 1: Thermophysical Properties

    rho, mu, K, Cp = RefWrap('O2','TP','D VIS TCX Cp',350,5e6)

    unpacks a REFPROP array for Oxygen at 350 [K] and 5 [MPa] containing:

    - Density [kg/m^3]
    - Dynamic Viscosity [Pa-s]
    - Thermal Conductivity [W/m-K]
    - Const. Pres. Specific Heat [J/kg-K]

    and returns stored variables for each property.

    Example function call 2: Saturation Properties

    T_sat = RefWrap('O2','PQ','T',101325,0)

    returns the saturation temperature of Oxygen at 101325 [Pa] assuming the
    fluid is all liquid (i.e. vapor quality = 0).

    ---------------------------------------------------------------------------

    To call the phase of a fluid, simply pass the string 'PHASE' as the output
    type for the call to RefWrap. The function will return a 1 x n character
    array specifying the phase of the fluid at the passed in input types.

    *NOTE*: Calling phase as well as other thermophysical properties will
    return the phase as an error message (-9999950) because the Python output
    structure does not store any value for the string output of 'PHASE' in the
    Output field. When calling the phase of a fluid, do so separately from
    other thermophysical property calls.

    ---------------------------------------------------------------------------
    LINK TO REFPROP DOCUMENTATION
    ---------------------------------------------------------------------------
    For information about the unit system, full input list, and REFPROP output array see:
    https://refprop-docs.readthedocs.io/en/latest/DLL/high_level.html#f/_/REFPROPdll

    *NOTE*:
    - A value of -9999990 will be returned by REFPROP if no value is calculated
      for a given input.
    - A value of -9999970 will be returned by REFPROP if an error occurs during
      calculation.
    - A value of -9999950 will be returned by REFPROP if no value is stored in
      the Output structure, but does have values stored in other fields (i.e.
      when calling the phase of a fluid, the field hUnits contains the string
      identifier for the phase, but the Output field will return an error).

    '''

    # Define location where REFPROP is stored and let the dll know
    rootUsers                = os.path.expanduser('~') + '\\REFPROP'
    rootProgramFilesx86      = 'C:\\Program Files (x86)\\REFPROP'
    REFPROPinUsers           = os.path.exists(rootUsers)
    REFPROPinProgramFilesx86 = os.path.exists(rootProgramFilesx86)

    if (REFPROPinUsers is False) or (REFPROPinProgramFilesx86 is False):
        raise Exception(f'Uh oh, REFPROP isn\'t found at Users\\%YOURUSERNAME%\\REFPROP or C:\\Program Files (x86)\\REFPROP')
    
    # Will default to User directory even if both are True because if statements check top-down
    if REFPROPinUsers is True:
        RP = REFPROPFunctionLibrary(rootUsers)
        RP.SETPATHdll(rootUsers)
    elif REFPROPinProgramFilesx86 is True:
        RP = REFPROPFunctionLibrary(rootProgramFilesx86)
        RP.SETPATHdll(rootProgramFilesx86)

    # Separate the outputs and count them
    outputTypesSplit = outputTypes.split(" ")
    numOutputs = len(outputTypesSplit)

    iUnits = RP.GETENUMdll(0,"MASS BASE SI").iEnum # Setting units to Mass Base SI
    iMass = 1                                      # 0: molar fractions; 1: mass fractions (for mixtures)
    iFlag = 0                                      # 0: don't call SATSPLN; 1: call SATSPLN

    # Structure the call to REFPROP
    x = RP.REFPROPdll(species,inputTypes,outputTypes,iUnits,iMass,iFlag,inputTypeFirst,inputTypeSecond,mixtureRatio)

    # If only one value output is asked for, return it
    if (numOutputs == 1) and (outputTypesSplit[0] != 'PHASE') and (units is False):
        return x.Output[0]
    # If unit output is asked for, or if the only output is the fluid phase, return that instead
    elif ((numOutputs == 1) and (outputTypesSplit[0] != 'PHASE') and (units is True)) or (outputTypes == 'PHASE'):
        return x.hUnits
    # If multiple unit outputs are asked for, warn user that only unit of first output can be returned
    elif (numOutputs > 1) and (outputTypesSplit[0] != 'PHASE') and (units is True):
        print(f'Only first output can return units, sorry. If you want multiple units you have to make multiple calls.')
        return x.hUnits
    # Otherwise, make a tuple to hold all of the outputs and unpack each one into the subsequent output
    # This is specifically a tuple so that python doesn't return a generator object but instead the values
    else:
        return tuple(outputValue for outputValue in x.Output[0:numOutputs])

def plotLine(xData: np.ndarray | list, yData: np.ndarray | list,
             title: str = '2D Line Plot', xLabel: str = 'X', yLabel: str = 'Y',
             color: str = 'cyan', lineWidth: float = 1, lineStyle: str = None,
             markerStyle: str = None, markerSize: float = 4, fontSize: int = 12, label: str = '2D Line') -> None:

    '''
    
    Wrapper for matplotlib plots bc I'm lazy.
    
    '''
    
    plt.rcParams.update({'font.size': fontSize})
    plt.style.use('dark_background')

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(xData, yData,
             label = label, color = color,
             lw = lineWidth, ls = lineStyle,
             marker = markerStyle, ms = markerSize)
    
    ax = plt.gca()
    ax.set_xlabel(xLabel)
    ax.set_ylabel(yLabel)
    ax.set_title(title)
    plt.show(block = False)
