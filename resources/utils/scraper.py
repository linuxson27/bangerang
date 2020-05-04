#!/usr/bin/env python
# -*- coding: utf-8 -*-

# System imports
import time
#+++++++++++++++++
# Helpers and utils imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import logzero
from logzero import logger
#+++++++++++++++++

# Setup log file
logzero.logfile("logs/logfile.log", maxBytes=1e6, backupCount=3)


class Scraper:
    """
    Main class for handling all scrape requests
    """
    driver = None

    def __init__(self):
        pass


    # Create browser instance
    def __get_browser_instance(self, url):
        if self.driver == None:
            # Chrome driver instance - headless
            options= webdriver.ChromeOptions()
            options.add_argument('headless')
            options.add_argument('window-size=1920x1080')
            options.add_argument('disable-gpu')
            self.driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver', options=options)
            self.driver.get(url)
            return self.driver
        else:
            return self.driver.get(url)


    # Get page source for further manipulation
    def get_page_content(self, url):
        # Get browser instance
        self.__get_browser_instance(url)
        # Get page content
        return self.driver.page_source


    # Get specified page element
    def get_page_element(self, by="id", value=None):
        # Convert to lower case
        by = by.lower()
        # Test by value and return By locator
        if by == "id":
            by = By.CSS_SELECTOR
            value = '[id="%s"]' % value
        elif by == "tag":
            by = By.CSS_SELECTOR
        elif by == "class":
            by = By.CSS_SELECTOR
            value = ".%s" % value
        elif by == "name":
            by = By.CSS_SELECTOR
            value = '[name="%s"]' % value
        else:
            # Log if incorrect 'by' value was supported
            logger.exception("Locator type '" + by + "' not correct/supported")
            raise(ValueError)

        # ['value'] at end of statement actualy refers 
        # to the 'value' key of the dict returned
        return self.driver.execute("findElements",
                                   {"using": by, "value": value})['value']


    # Get soup from driver page source
    def get_page_soup(self, content):
        soup= BeautifulSoup(content, 'html.parser')
        # Close page and browser object
        self.driver.quit()
        self.driver = None
        return soup


    # Enter value into input query field
    def do_query(self, element , query):
        pass

