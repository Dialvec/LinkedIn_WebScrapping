# -*- coding: utf-8 -*-

"""
Created on Sat Aug  7 00:01:51 2021

@author: Dialvec
"""
#Packages importing
missing_packages=[]

import sys

try:
    import os
except ModuleNotFoundError:
    sys.exit("""Library os not found 
                 Please install missing library""")

#Working directory setup for local modules
cwd = os.getcwd()
print("Current Working Directory ->" , cwd)
os.chdir(cwd)
    
try:
    import utils
except ModuleNotFoundError:
    sys.exit("""Custom library utils.py not found 
                 Please check project files""")

try:
    import pandas as pd
except ModuleNotFoundError:
    missing_packages.append("Pandas")
    
try:
    from datetime import date
except ModuleNotFoundError:
    missing_packages.append("datetime")
    
try:
    import selenium
except ModuleNotFoundError:
    missing_packages.append("selenium")

try:
    import LnkDriver
except ModuleNotFoundError:
    missing_packages.append("LnkDriver.py")
    
try:
    import LnkCrawler
except ModuleNotFoundError:
    missing_packages.append("LnkCrawler.py")

try:
    import Database
except ModuleNotFoundError:
    missing_packages.append("Database.py")

utils.moduleNotFoundExit(missing_packages)

Database = Database.NewDatabase(df_path = utils.FILE_PATH)

Driver = LnkDriver.NewLnkDriver('daggercrow@gmail.com', '57FtjCIbbZ')
Driver.startSession()

MyCrawler = LnkCrawler.NewLnkCrawler(Driver)
df_chunk = MyCrawler.scanCompaniesSalesOpenings(['google', 'microsoft', 'amazon'])

Database.add_chunk(df_chunk)
Database.save()

Driver.endSession()

print("Excecution finished")

