# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 04:12:31 2021

@author: Dialvec
"""
import utils
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

class NewLnkDriver:
    
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        #Set up browser driver
        self.__opts = Options()
        self.__opts.add_argument(utils.OPTS_ARGUMENT)
        self.__webdriver = None
        
    def __getUsername(self):
        return self.__username
    
    def __getPassword(self):
        return self.__password
    
    def getWebDriver(self):
        return self.__webdriver
    
    def __setupWebDriver(self):
        opts = Options()
        opts.add_argument(utils.OPTS_ARGUMENT)
        self.__webdriver = webdriver.Chrome(utils.CHROME_DRIVER, options = opts)
        #self.__webdriver = webdriver.firefox(utils.FIREFOX_DRIVER)
        
        
    #Browses to company's linkedin headcount page
    def browseCompany(self, Company):
        driver = self.getWebDriver()
        url = utils.LNK_COMPANY + Company + utils.LNK_HEADCOUNT
        driver.get(url)
    
    def startSession(self):
        self.__setupWebDriver()
        
        driver = self.getWebDriver()
        
        driver.get(utils.LOGIN_URL)
        
        #Find username and password text boxes
        input_username = WebDriverWait(driver, utils.TIMEOUT).until(
          EC.presence_of_element_located((By.XPATH, utils.USER_TEXTBOX))
        )
        
        input_password = WebDriverWait(driver, utils.TIMEOUT).until(
        EC.presence_of_element_located((By.XPATH, utils.PASS_TEXTBOX))
        )
        
        #Fill up username and password
        input_username.send_keys( self.__getUsername() )
        input_password.send_keys( self.__getPassword() )
        
        #Get log in button and click
        login_button = driver.find_element(By.XPATH, utils.LOGIN_BUTTON)
        login_button.click()
        
        try:
            WebDriverWait(driver, utils.TIMEOUT).until(
                EC.presence_of_element_located((By.XPATH , utils.BODY))
            )
        except:
            print("Failed to load main page")
        
        
    def endSession(self):
        self.driver.close()
        self.driver.quit()