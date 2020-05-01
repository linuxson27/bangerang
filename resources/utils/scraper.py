#!/usr/bin/env python
# -*- coding: utf-8 -*-

# System imports
import time
#+++++++++++++++++
# Helpers and utils imports
from selenium import webdriver
from bs4 import BeautifulSoup
#+++++++++++++++++


class Scraper:
    """
    Main class for handling all scrape requests
    """
    def __init__(self):
        pass

        # Chrome driver instance - headless
        options= webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument('disable-gpu')
        self.driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver', options=options)


    # Get soup from driver page source
    def get_page_soup(self, url):
        self.driver.get(url)
        content = self.driver.page_source
        soup= BeautifulSoup(content, 'html.parser')
        return soup


    # Get specified page element - single only
    def get_page_element(self, soup, prop, value):
        element = soup.find('input', attrs={prop: value})
        return element


    # Enter value into input query field
    def do_query(self, query):
        pass

