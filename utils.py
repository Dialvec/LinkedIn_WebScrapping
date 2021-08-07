# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 03:36:13 2021

@author: Dialvec
"""
import sys
from datetime import date

#Parameters
    #Browser Parameters
LOGIN_URL     = "https://www.linkedin.com"
OPTS_ARGUMENT = 'user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36'
CHROME_DRIVER = './chromedriver.exe'
TIMEOUT       = 30
SCROLL_DOWN_WAIT = 3
LNK_COMPANY   = 'https://www.linkedin.com/company/'
LNK_HEADCOUNT = '/insights/?insightType=HEADCOUNT'
    #Common error message
NO_COMPANY_DATA = "Could not find data for company: "
    #xml login mapping
BODY          = '//body'
MAIN          = '//main'
USER_TEXTBOX  = '//main//div[@class="sign-in-form-container"]//input[@name="session_key"]'
PASS_TEXTBOX  = '//main//div[@class="sign-in-form-container"]//input[@name="session_password"]'
LOGIN_BUTTON  = '//main//div[@class="sign-in-form-container"]//button[@class="sign-in-form__submit-button"]'
    #xml company chart mapping
XPATH_HEADCOUNT_CHART = '//main//section[@class="org-insights-module org-insights-functions-growth org-insights-jobs-module"]/div[@class="org-premium-container premium-accent-bar artdeco-card"]/div[@class="org-premium-container__content"]/div[@class="org-insights-functions-growth__content"]/div[@class="org-insights-functions-growth__chart"]//div[@class="highcharts-wrapper ember-view"]/div[@class="chart-container"]/div[@class="highcharts-container "]'

#Exception messages    
def moduleNotFoundExit(missing_packages):
    if( len(missing_packages) > 0 ):
        for package in missing_packages:
            print("Library", package, "not found.")
        print("******* Execution finished *******")
        sys.exit("Please install missing libraries")

def xpathNotFound(xpath):
    sys.exit("Could not find xpath: " + xpath)
    
def today():
    return date.today().strftime("%Y/%m/%d")

    
    