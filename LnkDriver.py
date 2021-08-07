# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 04:12:31 2021

@author: Dialvec
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

class NewLnkDriver:
    
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        
    def __getUsername(self):
        return self.__username
    
    def __getPassword(self):
        return self.__password
        
    def startSession(self):

        #Parameters
        __LOGIN_URL     = "https://www.linkedin.com"
        __OPTS_ARGUMENT = "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"
        __USER_TEXTBOX  = '//main//div[@class="sign-in-form-container"]//input[@name="session_key"]'
        __PASS_TEXTBOX  = '//main//div[@class="sign-in-form-container"]//input[@name="session_password"]'
        __LOGIN_BUTTON  = '//main//div[@class="sign-in-form-container"]//button[@class="sign-in-form__submit-button"]'
        
        #Set up browser driver
        opts = Options()
        opts.add_argument(__OPTS_ARGUMENT)
        driver = webdriver.Chrome('./chromedriver.exe', options=opts)
        driver.get(__LOGIN_URL)
        
        #Find username and password text boxes
        input_username = WebDriverWait(driver, 10).until(
          EC.presence_of_element_located((By.XPATH, __USER_TEXTBOX))
        )
        input_password = driver.find_element(By.XPATH, __PASS_TEXTBOX)
        
        #Fill up username and password
        input_username.send_keys( self.__getUsername() )
        input_password.send_keys( self.__getPassword() )
        
        #Get log in button and click
        login_button = driver.find_element(By.XPATH, __LOGIN_BUTTON)
        login_button.click()
        
    def endSession(self):
        self.driver.close()
        self.driver.quit()