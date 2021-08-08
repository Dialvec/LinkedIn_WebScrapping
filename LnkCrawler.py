# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 06:22:09 2021

@author: Dialvec
"""
import utils
import pandas as pd
import LnkDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class NewLnkCrawler:
    def __init__(self, LnkDriver):
        self.__lnkDriver = LnkDriver
    
    def __getLnkDriver(self):
        return self.__lnkDriver
    
    def __getWebDriver(self):
        return self.__getLnkDriver().getWebDriver()
    
    def browseCompany(self, Company):
        self.__getLnkDriver().browseCompany(Company)
    
    #loops over companies list to gather data from the premium job openings chart
    def scanCompaniesSalesOpenings(self, Companies):
        
        df_chunk = pd.DataFrame( columns=utils.COLNAMES )
        
        timestamp = utils.today()
    
        for company in Companies:
            
            driver=self.__getWebDriver()
            
            self.browseCompany(company)
            
            #try:
            #    WebDriverWait(driver, utils.TIMEOUT).until(
            #    EC.presence_of_element_located((By.XPATH , utils.MAIN))
            #    )
            #except:
            #    print(utils.NO_COMPANY_DATA + company)
            #    continue
        
            #Scroll down to page end
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            
            WebDriverWait(driver, utils.TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, utils.XPATH_HEADCOUNT_CHART))
            )
            
            xpath=utils.XPATH_HEADCOUNT_CHART
            
            total_openings = driver.find_element_by_xpath( xpath + '//*[local-name()="svg"]/*[local-name()="text" and @class="highcharts-title"]/*[local-name()="tspan"]').text
            #print(total_openings)
            
            q_period = driver.find_element_by_xpath( xpath + '//*[local-name()="svg"]/*[local-name()="text" and @class="highcharts-subtitle"]/*[local-name()="tspan"]').text
            #print(q_period)
            
            #Sales job openings window needs a mouse hover action
            
            sales_job_chart_section = driver.find_element_by_xpath( xpath + '//*[local-name()="svg"]/*[local-name()="g"]/*[local-name()="g" and @class="highcharts-series highcharts-series-0 highcharts-pie-series highcharts-tracker"]/*[local-name()="path" and @class="highcharts-point highcharts-color-1 org-insights__highcharts-function-color-2"]')
            #print(sales_job_chart_section)
            actions = ActionChains(driver)
            actions.move_to_element(sales_job_chart_section).perform()

            sales_openings = driver.find_element_by_xpath(xpath + '/div[@class="highcharts-label highcharts-tooltip highcharts-color-1"]/span/p/strong').text
            #print(sales_openings)
            
            df_chunk = df_chunk.append({utils.COLNAMES[0] : timestamp,
                                        utils.COLNAMES[1] : company,
                                        utils.COLNAMES[2] : q_period,
                                        utils.COLNAMES[3] : total_openings,
                                        utils.COLNAMES[4] : sales_openings
                                        }, ignore_index=True)
        #print(df_chunk)
        return df_chunk
            
            