#!/usr/bin/env python
# -*- coding: utf-8 -*-

from resources.utils.scraper import Scraper

try:
    scraper = Scraper()
    content = scraper.get_page_content("https://www.google.com")
    element = scraper.get_page_element(by="name", value="q")
    print("Element is: ", element)
except Exception as e:
    print(e)
finally:
    scraper.driver.quit()
