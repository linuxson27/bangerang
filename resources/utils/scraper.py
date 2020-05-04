#!/usr/bin/env python
# -*- coding: utf-8 -*-

# System imports
import time
#+++++++++++++++++
# Helpers and utils imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
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
    def __get_driver_instance(self, url):
        if self.driver == None:
            # Chrome driver instance - headless
            #  options= webdriver.ChromeOptions()
            #  options.add_argument('headless')
            #  options.add_argument('window-size=1920x1080')
            #  options.add_argument('disable-gpu')
            self.driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')#, options=options)
            self.driver.get(url)
        else:
            self.driver.get(url)

    # Get page source for further manipulation
    def get_driver_content(self, url):
        # Get browser instance
        self.__get_driver_instance(url)
        # Get page content
        return self.driver.page_source


    # Get specified page element/s
    def get_driver_element(self, by="id", value=None):
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
            # Log if incorrect 'by' value was supplied
            logger.warning("Locator type '" + by + "' not correct/supported")
            raise(ValueError)

        # ['value'] at end of statement actualy refers 
        # to the 'value' key of the dict returned
        return self.driver.execute("findElements", 
                                   {"using": by, "value": value})['value']


    # Insert text into input field
    def insert_text(self, element=WebElement, text=None):
        # Test here if element is of type WebElement
        if isinstance(element, WebElement):
            # Test here if webelement has 'text' attribute
            if element.get_attribute('type') == 'text':
                # Test if element readonly
                if element.get_attribute('readonly'):
                    self.driver.execute_script("arguments[0].readOnly=false", element)
                element.send_keys(text)
            else:
                # Log any errors
                logger.warning("Element is not of type 'input'")
                raise(TypeError)
        else:
            logger.warning("Element is not of type HTML element")
            raise(TypeError)


    def send_enter_key_to_element(self, element):
        return element.send_keys(Keys.RETURN)


    # Get soup from driver page source
    def get_driver_soup(self, content):
        soup= BeautifulSoup(content, 'html.parser')
        # Close page and browser object
        self.driver.quit()
        self.driver = None
        return soup

