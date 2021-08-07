# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 06:22:09 2021

@author: Dialvec
"""

import utils
from datetime import date
from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

   
class NewLinkedInCrawler:
    def __init__(self, WebDriver):
        self.__webdriver = WebDriver
    
    def __getWebDriver(self):
        return self.__webdriver
        
    def browseCompany(self, Company):
        url = 'https://www.linkedin.com/company/' + Company + '/insights/?insightType=HEADCOUNT'
        self.__getWebDriver().get(url)
    
    def scanCompaniesSalesOpenings(self, Companies):
        
        timestamp = date.today().strftime("%Y/%m/%d")
    
        for company in Companies:
            self.browseCompany(company)
            
            try:
                xpath = '//main//section[@class="org-premium-insights-module"]//div[@class="org-insights-functions-growth__content"]//g[@class="highcharts-series highcharts-series-0 highcharts-pie-series highcharts-tracker"]'
                WebDriverWait(self.__getWebDriver(), 10).until(
                    EC.presence_of_all_elements_located((By.XPATH, xpath))
                    )
            except:
                print("Could not find data for company: " + company)
                continue
            
            total_openings = self.__getWebDriver().find_element_by_xpath(xpath+'//text[@class="highcharts-title"]/text()')
            q_period = self.__getWebDriver().find_element_by_xpath(xpath+'//text[@class="highcharts-subtitle"]/text()')
            sales_openings = self.__getWebDriver().find_element_by_xpath(xpath+'//text[@class="highcharts-title"]/text()')
            
            
            