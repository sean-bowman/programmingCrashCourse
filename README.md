# Programming Crash Course

**(A.K.A. I wish someone did this for me)**

Written by: Sean Bowman

Original Document: [10/10/2023]

Latest Revision: [12/08/2025]

- [Programming Crash Course](#programming-crash-course)
- [1: Introduction](#1-introduction)
  - [1.a: Motivation](#1a-motivation)
  - [1.b: Programming Basics](#1b-programming-basics)
    - [Language Types](#language-types)
    - [Compiled vs. Interpreted](#compiled-vs-interpreted)
    - [Object Oriented Programming: What is it?](#object-oriented-programming-what-is-it)
    - [Comments, comments, comments!](#comments-comments-comments)
    - [Programming Standards: Have Them!](#programming-standards-have-them)
  - [1.c: End-program teaser (Pressure Drop Calculator)](#1c-end-program-teaser-pressure-drop-calculator)
- [2: Python Fundamentals](#2-python-fundamentals)
  - [2.a: Variables, Arrays, and Quirks of Python](#2a-variables-arrays-and-quirks-of-python)
  - [2.b: Loops and Conditional Statements](#2b-loops-and-conditional-statements)
- [2.c: Repository Structure](#2c-repository-structure)
- [3: Worked Example of a Programming Standard](#3-worked-example-of-a-programming-standard)
  - [3.a: Class Definition](#3a-class-definition)
  - [3.b: Top Level / Code Interface](#3b-top-level--code-interface)
  - [3.c: Calculate Pressure Drop Method](#3c-calculate-pressure-drop-method)
  - [3.d: Running the program](#3d-running-the-program)

# 1: Introduction

## 1.a: Motivation

Learning to code can be a valuable tool in the arsenal of an engineer, especially those who work in computationally intense environments. This brief overview of coding in Python is intended to be a jumping-in point for individuals either learning to code for the first time, or those who have long since forgotten the introductory courses of early undergraduate work. In no way is this overview intended to be fully comprehensive of the depths of programming in all of its use cases, however these fundamental skills should create a foundation from which more intricate coding skills may be learned.

The structure of the course is broken into 3 distinct parts, each of which can be read as its own section divorced from the larger course structure. That is to say, if any one section is below the understanding level of the reader it may be entirely skipped at no detriment to the course flow. The 3 sections are as follows:

- Basics of Programming in General (Super High-Level)
- Fundamentals of Programming with Python (High-Level)
- Worked Example (More intricate coding practices employed)
  - Development of a Pressure Drop calculator for a Straight Pipe
  - Example of the programming standards I use when developing software

## 1.b: Programming Basics

### Language Types

Programming languages can have two different styles of variable typing:

- Static
- Dynamic

The first is *static* typing. Static typing means that each variable declared in the program must also have its data type pre-specified. An example of this is presented below as a snippet of C++ code (a statically typed language):

```c++
C++ (Static)
//----------------------------------------------------------------//
int    myNum      = 5;       // Integer (whole number without decimals)
double myFloatNum = 5.99;    // Floating point number (with decimals)
char   myLetter   = 'D';     // Character
string myText     = "Hello"; // String (text)
bool   myBoolean  = true;    // Boolean (true or false)
```

Preallocation of data type allows the program to be read more quickly by the compiler and is therefore quicker to execute. However, because the program must first be compiled before running, static languages are not used for scripting (single-purpose codes that perform a distinct action).

Conversely, there are *dynamically* typed languages. Dynamically typed languages do not require you to pre-specify data types; instead the compiler or interpreter figures out the type of the data on the fly for you. This makes your life a bit easier, at the cost of some performance. An example of some variable declarations in Python are presented below for comparison:

```python
PYTHON (Dynamic)
#---------------------------------------------------------#
myNum      = 5       # Integer (whole number without decimals)
myFloatNum = 5.99    # Floating point number (with decimals)
myLetter   = 'D'     # Character
myText     = "Hello" # String (text)
myBoolean  = True    # Boolean (true or false)
```

Also for comparison are the same variable declarations in Matlab:

```matlab
MATLAB (Dynamic)
%----------------------------------------------------------%
myNum      = 5;       % Integer (whole number without decimals)
myFloatNum = 5.99;    % Floating point number (with decimals)
myLetter   = 'D';     % Character
myText     = "Hello"; % String (text)
myBoolean  = true;    % Boolean (true or false)
```

### Compiled vs. Interpreted

As hinted at in the previous section, variable typing is not the only thing that distinguishes languages from each other. Programming languages in general are an abstraction above pure binary machine code (turning the tiny silicone transistors in your PC on and off), however some are more abstract than others to make our lives as humans easier. To continue using C++ as an example language, C++ is a *compiled* language as well as being statically typed. This means that the program must first be successfully compiled into machine code before executing, but once a program is successfully compiled it technically never has to be again and the same compiled executable can be run at will. This makes the language speedy and efficient, even more so thanks to its static typing which makes memory allocation smoother and more efficient as well.

Alternatively, languages may be read by an interpreter. Interpreted languages are slower as they have to be read and interpreted by the interpreter in order to be executed, however they do not have to be compiled in their entirety to run. That means that you can just write a few lines, press go, and get a command window output right away, no compiler step in between. Interpreted languages are generally easier to read and write in, which makes them very popular despite the inherent drawbacks in performance. One of the most popular open-source dynamically typed interpreted languages is Python, which has a variety of use-cases and packages to handle an honestly insane diversity of problems.

### Object Oriented Programming: What is it?

You may have heard of Object Oriented Programming (OOP) before, but what exactly does that mean? It might seem pedantic, but the name is quite literal. With OOP you are able to create *objects* in code that are able to store properties and methods to interact with them. Again, lots of jargon, what is an *object*? Using the example we will work towards in this course, let's start with the pressure drop in a pipe problem. This problem is workable entirely without objects, however implementing them could prove useful (if you know how to work with objects!).

In the pressure drop problem, we have a straight pipe with some fluid flowing through, and we want to take the inlet conditions along with some fancy math to determine what the outlet pressure of the pipe would be given the inlet conditions specified. This is a relatively simple problem and you could very well just use Python as a calculator to replace having to write down calculations by hand and there is nothing wrong with that approach. Crafting a framework around a problem, however, is a skill that will be more useful to you in future problem solving endeavors. To create something general purpose at the same time as solving our problem, it would be best to functionalize the problem so that when we return to it later we have already created the tool to solve similar problems.

One way to modularize this problem would be to create an object to store the pipe properties! You can think of the object as *representing* the pipe, its properties, and what you can do to it. We can define the pipe object in Python like this:

```python
class Pipe:

    #---------------------------------#
    # -- Public Properties -- #
    #---------------------------------#

    def __init__(self):

      ...

    #---------------------------------#
    # -- Public Methods -- #
    #---------------------------------#

    def publicMethod(self):

      ...

```

Here we can see the guts of a class in its most basic form.

We save this class definition to a file called $Pipe.py$ and store it in the assets directory.

That's cool and all, but how do we use this class? We can make a pipe of our own by instantiating the class like this:

```python
from assets import Pipe

myPipe = Pipe() # This step is called instantiation
```

Where the process of instantiation is basically asking the _ _ init _ _() method to make you a blank pipe object. Now that you have a pipe object, you can assign it properties either with dot indexing:

```python
myPipe.length        = 2
myPipe.innerDiameter = 0.1
```

or by running the setInputs() method that I wrote that reads the provided .csv config file:

```python
myPipe.setInputs()
```

With the properties set, we can call the calculatePressureDrop() method to run the pressure drop model:

```python
myPipe.calculatePressureDrop()
```

Now, if you were just writing this example out to solve it like a homework problem it might seem like overkill to use OOP patterns when the object only has like 2 stored properties, but objects can get quite large and when that is the case it is often much easier to manipulate the object as a whole as opposed to each of its individual properties or methods.

### Comments, comments, comments!

As you may have noticed in the code snippets in the above sections, programming languages come with the ability to hide certain components from the compiler/interpreter. These hidden lines and characters are called comments, and exist to make the code more readable for the human working with the code. Proper code commenting is essentially mandatory for any professional software development environment, so we will touch on it here.

Each language has a specific character that, when typed, the rest of that line of code is ignored by the compiler/interpreter. In Python this character is '#', but in other languages it takes on different forms. We will go more into detail later on how best to structure code comments, but for now just knowing they exist is an important step.

### Programming Standards: Have Them!

Writing code can often come with a lot of personality influences. Often when working in a team, pieces of code written by a different developer may be easily identified by idiosyncrasies in the structure of the code. This is a great consequence of the medium: A single developer is able to tackle a challenge in their own creative way, likely entirely unique if the problem is sufficiently complex. When working with others, especially on large complex code bases, it is often useful to have a set of programming standards that every developer in the company abides by. This allows the code base across the entire company to be easily readable and debuggable because everyone knows what to expect. The rules vary across the industry, and as a part of this overview we will go over some of the standards I employ to facilitate smooth code development.

## 1.c: End-program teaser (Pressure Drop Calculator)

By the end of this overview we will develop a tool in Python to calculate the pressure drop across a straight pipe. To accomplish this, we will touch on a variety of coding elements and techniques, and at the end you will walk away with a piece of software that you can use outside of the scope of this overview, or even add functionality to improve the program past its initial state.

Here is a preview of what we are working towards:

```python
# Instantiate a Pipe object
myPipe = Pipe()

# Set the inputs using the provided .csv file and the setInputs() method of the Pipe class
myPipe.setInputs()

# Run the pressure drop calculator to calculate pressure drop given the provided properties
outletPressure, totalPressureDrop = myPipe.calculatePressureDrop()
```

![Example Output Image](assets\ExampleOutput.png)

# 2: Python Fundamentals

## 2.a: Variables, Arrays, and Quirks of Python

We discussed this briefly in the previous introduction section, but for the sake of completeness of this document such that each section stands on its own I will go over the fundamental concepts again here.

Pyton is a dynamically typed interpreted language, which means that data types *do not* need to be pre-specified when defining variables. This makes our lives easier at the cost of some performance, but in the example we are working with today this performance penalty is negligible at best.

When defining variables in Python, you simply assign a value you wish to keep track of with a name, such as:

```python
testInteger = 1
testString  = 'Hello'
testBoolean = True
```

In Python, you don't need to terminate lines with semicolons, but to get outputs to print to the command window or terminal you must explicitly tell Python to do so:

```python
x = 1    # WON'T output anything to the terminal
print(x) # Prints the value stored in 'x' to the terminal
>>> 1
```

There are two different array-like types that are commonly used in Python: lists and numpy arrays. Lists are the default data structure baked into Python as a language, and numpy arrays are an added feature through the numpy module that can be imported into any project (assuming you have it installed). Lists have many of the fundamental actions you may expect of collections of data in programming, however they were not specifically designed with linear algebra in mind. Most software doesn't even deal with math, and most programmers don't do any math at all. To that end, lists can also store collections of any other type of data, be it strings or booleans or whatever else. This makes them broadly useful, unless your main goal is to do math. Often when engineers are using code to solve problems it often implies that repetitive math will be occurring. In this case Matlab as a programming tool becomes a common solution to engineering programming. Matlab comes with linear algebra tools baked right in, which makes working with matrices and math a breeze. Numpy is the Python equivalent of Matlab's array structures for Python programmers, and there are many similarities.

Here I will go over both lists and numpy arrays because both are useful in their own ways and there are often cases where one or the other should be used.

To initialize an empty list in Python, you don't need to specify what kind of information is going to be stored inside. You can simply ask Python to set aside some memory for a list of unknown size by doing:

```python
myList = []
```

If you begin with an empty list like this, adding a new value can be done with an 'append' operation, adding a value to the end of a list:

```python
myList.append(1)
print(myList)
>>> [1]
```

Lists in Python can contain any data type and do not need to contain all of the same data type (this would be equivalent to Matlab's cell array). A pre-filled list could look like:

```python
myList = [1, 3.14, 'Hello', True]
```

You can ask for the individual elements of a list by indexing, where indexes are specified with brackets and the first index is 0:

```python
print(myList[0])
>>> 1
print(myList[2])
>>> 'Hello'
print(myList[2][0])
>>> 'H'
```

Lists are useful either when the data type in a collection varies but all of it belongs together, or when you don't know the size of your array and just want to append values on to the end indefinitely.

As a side note here, if you have values that would be better described by words instead of array indices, there is a data type called a dict (or dictionary) to accomplish this. The goal is, as stated, to replace traditional indices (0, 1, 2, ...) with 'keys':

```python
myDict = {'iWishIWasAnIndex': 42,
          'carrots': 3.14}
print(myDict['carrots'])
>>> 3.14
```

Dicts are created with curly braces, {}, but are still indexed with square braces, [].

Numpy arrays make working with matrix-shaped data much easier, and if you are coming from Matlab it should feel familiar. There is a helpful resource for Matlab transplants that I will include here that goes over the differences in syntax between numpy and Matlab but I will go over the use of the library here.
[Numpy for Matlab Users](https://numpy.org/doc/stable/user/numpy-for-matlab-users.html)

To create a (2, 3) matrix of values using numpy you can do this:

```python
import numpy as np
'''
the 'as ____' statement renames the module to something more
convenient to type over and over, 'np' is the community agreed-upon
shorthand for numpy
'''
myArray = np.array([[1, 2, 3], [4, 5, 6]])
print(myArray)
>>> [[1, 2, 3],
     [4, 5, 6]]
print(myArray[0,1])
>>> 2
```

Here the second operation of indexing a particular (row, column) pair is performed differently than in the case with the list (where the indices each had their own set of braces). With numpy arrays, just like Matlab arrays, indexing can all be done in the same set of brackets separated by commas. (Also, the individual brackets thing works for numpy arrays too, so you have both options)

You may notice that there are lots of braces hanging around, what's that all about? Well, the idea of a 2D (2, 3) matrix works well with a piece of paper but computers don't think that way. In fact, it's nice of numpy to even put the two rows on a different level for visualization purposes. In reality there are only 1D lists, but like I mentioned earlier you can put anything into a list, even another list! This can be done with native lists as well, numpy arrays just come with a lot of convenient features (like transposing a multi-dimensional array with a simple .T method). In this setting, a 2D 2 row by 3 column matrix is represented programmatically as one large list that contains two more lists, one list of three elements long for each row.

## 2.b: Loops and Conditional Statements

What good are numerical techniques if we don't make the computer do a super repetitive task way faster than a human ever could by hand? That's where loops and conditional statements come in, which are a way to tell the computer to repeat a task over and over again, or only when a certain condition is met. Here are some examples of the common loop structures in Python and most other languages, 'for' and 'while', being used to print the first 10 numbers to the terminal window:

```python
x = 0       # Give 'x' an initial value

# This statement says take 'i' and start at 0 and do the instructions inside the loop
# Then, incriment 'i' by 1 making i = 1 and then perform the steps of the loop again and repeat this process 10 times
for i in range(10):

  x += 1   # Each time this loop runs, take the value stored in 'x' and add one to it
  print(x) # Print 'x' to the terminal window
    
  # End of the for loop, once this is reached Python checks if the iterator has reached its last element. If not, it runs again

y = 0       # Give 'y' an initial value

# This statement says look at the value of 'y' and check if it is less than 10
# If it is, do the thing in the loop
while y < 10

  y += 1   # Each time this loop runs, take the value stored in 'y' and add one to it
  print(y) # Print 'y' to the command window

  #End of the while loop, once this is reached Matlab checks if the value stored in 'y' has reached its condition and if not, it runs again

>>> 1
    2
    3
    4
    5
    6
    7
    8
    9
    10
```

Another common practice is to index through an array using a loop! I will provide an example here in the context of a 'for' loop:

```python
x = np.array([1, 2, 3, 4, 5]) # Initialize an array of 5 values

for index, value in enumerate(x):  # Loop over the elements of the array

  # Old value
  print(f'The old value was {value}')

  # Update and print new value
  x[index] += 1
  print(f'The new value is {x[index]}')

>>> The old value was 1
    The new value is 2
    ...
```

What if we only wanted to add 1 to the current element up to 3 and then stop? We can create a conditional statement!

```python
x = np.array([1, 2, 3, 4, 5]) # Initialize an array of 5 values

for index, value in enumerate(x):  # Loop over the elements of the array

  if value < 4:
    # Old value
    print(f'The old value was {value}')

    # Update and print new value
    x[index] += 1
    print(f'The new value is {x[index]}')
  
  else:
    print(f'The new value is {value}')

>>> The old value was 1
    The new value is 2
    The old value was 2
    The new value is 3
    The old value was 3
    The new value is 4
    The new value is 4
    The new value is 5
```

There are a few helpful ideas in this section as well, such as the enumerate function being used to keep track of both the iterator for the loop and simultaneously the value of the array at that index, as well as the use of an 'f-string' inside of the print statement that allows for variables to be embedded into the string without needing to concatenate multiple strings together.

## 2.c: Repository Structure

This repository is organized to separate the main code interface from the supporting class definitions and utilities. Here's the structure:

```text
programmingcrashcourse/
│
├── crashCourseCodeInterface.py    # Main program entry point
├── README.md                       # This document
├── .gitignore                      # Git ignore file
│
└── assets/                         # Supporting files
    ├── __init__.py                 # Python module initialization
    ├── Pipe.py                     # Pipe class definition
    ├── utils.py                    # Utility functions (RefProp wrapper, etc.)
    ├── pipeProperties.csv          # Configuration file with input parameters
    └── ExampleOutput.png           # Example output image
```

**File Descriptions:**

- [crashCourseCodeInterface.py](crashCourseCodeInterface.py): The top-level script that instantiates the Pipe class, sets inputs, and runs the pressure drop calculation
- [assets/Pipe.py](assets/Pipe.py): Contains the `Pipe` class definition with all methods for calculating pressure drop
- [assets/utils.py](assets/utils.py): Contains utility functions including the REFPROP wrapper for fluid property calculations
- [assets/__init__.py](assets/__init__.py): Allows the assets folder to be imported as a Python module
- [assets/pipeProperties.csv](assets/pipeProperties.csv): Configuration file where pipe geometry, fluid properties, and options are specified

# 3: Worked Example of a Programming Standard

This section serves both as a guided walkthrough of the aggressively over-commented code and as a rough standard for the style of code writing I use.

## 3.a: Class Definition

Before we dive into the physics part of this problem, first we must construct a class to create pipe objects. I say must, but really this is dramatic overkill for a problem like this. It is just an excuse to shove OOP into the lesson and force you to learn it for when it is more useful.

Earlier in the document we used the Pipe class as an example of what a class is, but we can repeat it here in case you skipped over that section:

```python
class Pipe:

    #---------------------------------#
    # -- Public Properties -- #
    #---------------------------------#

    def __init__(self):

      ...

    #---------------------------------#
    # -- Public Methods -- #
    #---------------------------------#

    def publicMethod(self):

      ...
```

This is a very basic example of what a class can be, but we're just getting our feet wet here. Now that we've defined a class for the pipe we can move on to the top level code.

## 3.b: Top Level / Code Interface

We will start in the top level code and explain what is happening. We start, as is the case with most of the code I write, with almost 100 lines of comments! I know, I'm a bit dramatic, but there is good reason! I write my code with a basic philosophy in mind. My code should be:

- Readable
- Understandable
- Implementable

If it fails at any of these things then it is, by definition, **bad code**. To that end, I go overboard with documentation up front because it makes both my colleagues and future me's life a ton easier. In general my code block at the top of any code has this basic structure:

```python

# -- Identifiable Name -- #

'''

Intro/Motivation

------------------------------------------------------------------------
# Inputs
------------------------------------------------------------------------
What does this code need to run?

------------------------------------------------------------------------
## Input Breakdown 1 of n
------------------------------------------------------------------------
Certain properties of ________ are editable by the user:

| Variable Description             |  Units |
|:--------------------------------:|-------:|
| Variable 1                       |    []  |
| Variable 2                       |    []  |

------------------------------------------------------------------------
## Options
------------------------------------------------------------------------
Certain functionality of the code can be disabled/enabled by entering
either 'on' or 'off' respectively for the presented options.

| Option Functionality           | Input Options |
|:------------------------------:|--------------:|
| Option 1                       | 'on' , 'off'  |
| Option 2                       | [int] |

------------------------------------------------------------------------
# Outputs
------------------------------------------------------------------------
The program outputs:

- Sum stuff

# Required module(s) / code(s):

- youNeedMe.py

Author: Sean Bowman
Date:   MM/DD/YYYY

'''
```

I've been told it looks like a CVS receipt.

Anyway, the next thing is the actual code in the top level code. I like to start every top-level script with the following statements:

```python
import os
os.system('cls')
```

This statement imports operating system commands so that they can be accessed, and then sends the command 'cls' to the terminal which CLears the Screen and de-clutters the terminal outputs.

I want to address as many useful concepts in one example as I can, so with that in mind we are going to read data off of a .csv to get input properties for our program. The inputs will be handled with a method of the Pipe class that we can write:

```python
def setInputs(self, inputFilepath: str = '.\\assets\\pipeProperties.csv') -> None:

  # Locally import pandas to read config
        import pandas as pd

        # Read the .csv in using pandas
        inputs = pd.read_csv(inputFilepath)

        for i, _ in enumerate(inputs.values):

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
```

This method utilizes a concept known as a switch-case (or in python a match-case for some reason but same thing) which is kinda like an if-else statement but evaluates much faster. If-else statements evaluate top-to-bottom requiring a boolean True or False to be spit out of each evaluation. This means that many math operations may happen in sequence (if you had a statement like if x > 2 for example) that occur top-down until your condition is found. It is much more efficient to just compare cases and here we are comparing to the string stored in the named column in the .csv. This is still essentially a boolean comparison, however there is only one operation per step (seeing what is stored in the match part of the statement) instead of running through the entire if-elif-else list every time.

Now that the method has been written, we can instantiate the class and set the inputs in our top level code interface:

```python
import os
from assets import Pipe

os.system('cls') # Clear terminal window when running

# Instantiate a blank object called 'myPipe' from the 'Pipe' class to hold our pipe info
myPipe = Pipe()

# Set the inputs using the provided .csv file and the setInputs() method of the Pipe class
myPipe.setInputs()
```

Finally, with the inputs set, we can calculate pressure drop:

```python
myPipe.calculatePressureDrop()
>>> type object 'Pipe' has no attribute 'calculatePressureDrop'
```

Why did it throw an error?

Oh.

I didn't write the method yet.

Alright let's do that.

## 3.c: Calculate Pressure Drop Method

```python
def calculatePressureDrop(self):
  ...
```

Here we are inside of our pressure drop calculator method. This is where we will perform the calculations to ACTUALLY CALCULATE pressure drop (among other things).

As a first step within the function, we are required by Python to pre-allocate the arrays that will be used to calculate fluid properties. You do not need to specify the length of the array when declaring it for the first time, however if you know the length of your array ahead of time (like we do in this case) then everything will be very efficient. Here I will use a list comprehension to initialize 7 numpy arrays of length 'numSlice' at the same time:

```python
'''

Calculate pressure drop in a straight pipe broken into 'n' slices using Darcy-Weisbach equation.

'''

# Initialize arrays with a list comprehension
numPreAllocatedArrays = 7
pressure, frictionFactor, density, dynamicViscosity, \
velocity, reynoldsNumber, pressureDrop \
= [np.zeros(self.numSlices) for _ in range(numPreAllocatedArrays)]

# Assign the inlet pressure to the first element of the pressure array. Python arrays start at 0.
pressure[0] = self.fluidInitialPressure
```

Before we get to the loop, it would be good to calculate things that do
not change as the looped parameter changes. This will make our code more
efficient.

```python
# Calculate dependent constant properties
pipeAxis = np.linspace(0, self.length, self.numSlices)
segmentLength = self.length / self.numSlices
crossSectionalArea = np.pi*(self.innerDiameter / 2)**2
```

Here is the meat and potatoes of the function: calculating pressure drop. We want to break up the pipe into sections to make calculating pressure drop more accurate, so we use a for loop to index over each pipe segment and calculate the individual dP at each segment and add them all up.

```python
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

# After the loop has finished, the outlet pressure is at the end of the pressure array, and the cumulative sum of pressure
# drops gives us thew total pressure drop
outletPressure = pressure[-1]
totalPressureDrop = np.cumsum(pressureDrop)[-1]

return outletPressure, totalPressureDrop
```

And there you have it! Pressure drop function complete.

## 3.d: Running the program

Now that we have everything set up, let's test out our calculator! Head over to the top level code ($crashCourseCodeInterface.py$), navigate to the run and debug panel (on the left there is a play button with a little bug on it) and click the big 'Run and Debug' button at the top (or press the F5 key if you're savvy).

In the command window at the bottom you should see:

```python
>>> The pipe inlet pressure was  300000.0 [Pa], and the outlet pressure ended at  225180.5 [Pa], where the total pressure drop is  74819.5 [Pa]
```

We've successfully created a program that takes in properties of a pipe and fluid conditions and outputs pressure drop. There is a lot to improve here, such as adding heat transfer to the problem and updating temperature within the loop in addition to the pressure, but hopefully this simple example is a good starting point to get you primed for the process of using programming to solve engineering problems.
