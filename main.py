# -*- coding: utf-8 -*-

"""
Created on Sat Aug  7 00:01:51 2021

@author: Dialvec
"""

import sys

def Lnk_scrapper(username, password, companies):
    
    #missing packages importing
    missing_packages=[]
    
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
        
    def cleanup_companies(companies):
        for i in range(len(companies)):
            companies[i] = companies[i].lower().replace(" ", "")
        return companies
    
    companies = cleanup_companies(companies)
    
    utils.moduleNotFoundExit(missing_packages)

    Database = Database.NewDatabase(df_path = utils.FILE_PATH)
    
    Driver = LnkDriver.NewLnkDriver(username, password)
    Driver.startSession()
    
    MyCrawler = LnkCrawler.NewLnkCrawler(Driver)
    df_chunk = MyCrawler.scanCompaniesSalesOpenings(companies)
    
    Database.add_chunk(df_chunk)
    Database.save()
    
    Driver.endSession()
    
    print("Excecution finished")
    
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    companies=[]
    
    for i in range(3, len(sys.argv)):
        companies.append(sys.argv[i])
        
    Lnk_scrapper(username, password, companies)

