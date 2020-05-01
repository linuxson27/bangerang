#!/usr/bin/env python
# -*- coding: utf-8 -*-

# System imports
import time
#+++++++++++++++++
# Helpers and utils imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
# import pandas as pd
#+++++++++++++++++


class Scraper:
    """
    Main class for handling all scrape requests
    """
    def __init__(self):
        pass

        # Chrome driver instance - headless
        #options= webdriver.ChromeOptions()
        #options.add_argument('headless')
        #options.add_argument('window-size=1920x1080')
        #options.add_argument('disable-gpu')
        self.driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')#, chrome_options=options)


    def put_search_query(self):
        pass


    # Get the National Lotto URL and return as soup object
    def get_page_soup(self):
        content = self.driver.page_source
        soup= BeautifulSoup(content, 'html.parser')
        return soup


    # Retrieve all lotto results from url soup
    def get_data_from_soup(self):
        pass

