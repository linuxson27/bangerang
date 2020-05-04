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


    # Get specified page element - single only
    def get_page_element(self, by=None, value=None):
        by = by.lower()
        # Test by value and return By locator
        if by == "class":
            return By.CLASS_NAME
        elif by == "css":
            return By.CSS_SELECTOR
        elif by == "id":
            return By.ID
        elif by == "link":
            return By.LINK_TEXT
        elif by == "name":
            return By.NAME
        elif by == "tag":
            return By.TAG_NAME
        elif by == "xpath":
            return By.XPATH
        else:
            logger.exception("Locator type '" + by + "' not correct/supported")
            raise(ValueError)
        return False


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

