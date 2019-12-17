# module is a python file with functions,classes and other components

#why use modules as it breaks code down and make code reusable 

#create a module

def display(message,is_warning=False):
    if is_warning:
        print('Warning!!')
    print(message)
    
# import module as namespace
import helpers
helpers.display('Not a warning')

# import all into current namespace
from helpers import *
display('Not a Warning!!')

# import specific items into urrent namespace
from helpers import display
display('Not a warning')


# packages are published collections of modules can be found python package index
# pip install colorama

# virtual environments 
# by default packages are installed globbally
# Due to this version management beomes a  challenge
# Virtual environments can be used to contain and manage package collections
# virtualenvs are basically a folder behind the scenes with all your packages
#pip install virtualenv
# In Windows:
# python -m venv <folder_name>
# OSX/Linux:
# virtualenv <folder_name>
# <folder_name>/bin/activate