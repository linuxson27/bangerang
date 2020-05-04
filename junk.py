#!/usr/bin/env python
# -*- coding: utf-8 -*-

from resources.utils.scraper import Scraper
from time import sleep

#  scraper = Scraper()
#  locator = scraper.get_element_locator(by="name")
#  print(locator)
#  locator = scraper.get_element_locator(by="class")
#  print(locator)
#  print(type(locator))
#  locator = scraper.get_element_locator(by="anthony")

try:
    scraper = Scraper()
    content = scraper.get_driver_content("https://www.nationallottery.co.za/lotto-history")
    
    from_date = scraper.get_driver_element(by="id", value="fromDate")[0]
    scraper.insert_text(from_date, text="01/01/2009")
    scraper.send_enter_key_to_element(from_date)
    
    to_date = scraper.get_driver_element(by='id', value="toDate")[0]
    scraper.insert_text(to_date, text="04/05/2020")
    scraper.send_enter_key_to_element(to_date)

    search_button = scraper.get_driver_element(by="id", value="search")[0]
    scraper.send_enter_key_to_element(search_button)

    soup = scraper.get_driver_soup(content)
    print(soup)

    sleep(5)
except Exception as e:
    print(e)
finally:
    if scraper.driver != None:
        scraper.driver.quit()

#  from selenium import webdriver
#  from selenium.webdriver.common.by import By
#
#
#  def my_method(by=str, value=str):
#      by = by.lower()
#      locator = None
#
#      # Test by value and return By locator
#      if by == "class":
#          locator = By.CLASS_NAME
#      else:
#          raise(ValueError)
#
#      return locator
#
#
#
#  obj = my_method(by="class", value="q")
#  print(obj)
#  print(type(obj))
