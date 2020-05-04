#!/usr/bin/env python
# -*- coding: utf-8 -*-

from resources.utils.scraper import Scraper

#  scraper = Scraper()
#  locator = scraper.get_element_locator(by="name")
#  print(locator)
#  locator = scraper.get_element_locator(by="class")
#  print(locator)
#  print(type(locator))
#  locator = scraper.get_element_locator(by="anthony")

try:
    scraper = Scraper()
    content = scraper.get_page_content("https://www.google.com")
    element = scraper.get_page_element(by="name", value="q")
    print("Element is: ", element)
except Exception as e:
    print(e)
finally:
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
