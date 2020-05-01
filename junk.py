#!/usr/bin/env python
# -*- coding: utf-8 -*-

from resources.utils.scraper import Scraper

scraper = Scraper()
soup = scraper.get_page_soup("https://www.google.co.za")
scraper.get_page_element(soup, 'name', 'q')
scraper.driver.quit()
