# -*- coding: utf-8 -*-
# Module currently not in use. Yet future functionality is not discarded
"""
Created on Sat Aug  7 02:16:59 2021

@author: Dialvec
"""
#Specific functions import
import utils

#Packages importing
missing_packages=[]

try:
    import requests
except ModuleNotFoundError:
    missing_packages.append("requests")

try:
    from lxml import html
except ModuleNotFoundError:
    missing_packages.append("lxml")

utils.moduleNotFoundExit(missing_packages)

#parameters
LOGIN_URL = "https://www.linkedin.com/uas/login-submit"


def getSessionRequest(username, password):
    
    #Create session object
    session_requests = requests.session()
    
    #Extract login csfr token
    result = session_requests.get(LOGIN_URL)
    
    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath("//input[@name='loginCsrfParam']/@value")))[0]
    
    #Define payload to send post login request to LinkedIn premium
    payload = {
        "session_key": username,
        "session_password" : password,
        "loginCsrfParam":authenticity_token
        }
    
    #Send POST request
    result = session_requests.post(
        LOGIN_URL,
        data = payload,
        headers = dict(referer=LOGIN_URL)
        )
    
    print(result.status_code)
    
    return session_requests  