# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 03:36:13 2021

@author: Dialvec
"""
import sys

#General ModuleNotFound error message
    
def moduleNotFoundExit(missing_packages):
    if( len(missing_packages) > 0 ):
        for package in missing_packages:
            print("Library", package, "not found.")
        print("******* Execution finished *******")
        sys.exit("Please install missing libraries")

def xpathNotFound(xpath):
    sys.exit("Could not find xpath: " + xpath)
    
    