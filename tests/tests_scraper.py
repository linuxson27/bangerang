#!/usr/bin/env python
# -*- coding: utf-8 -*-

# System imports
from os import path
#+++++++++++++++
# Utils and helpers imports
import pytest
import logzero
from logzero import logger
from PyQt5.QtCore import QObject
#+++++++++++++++
# Log file setup
logzero.logfile("logs/tests_scraper.log", maxBytes=1e6, backupCount=3)
#+++++++++++++++
# Tested module imports
try:    # Wrapped in try/except to catch import/file errors
    from resources.utils.scraper import Scraper
except Exception as e:
    logger.exception("Import Error")
    raise e
#+++++++++++++++


class TestScraper:
    """
    Tests all properties of the bangerang.py script
    """
    # Catch exceptions at startup
    def raise_system_exit(self):
        raise SystemExit(1)


    # Test modules for import errors
    def catch_system_exit(self):
        with pytest.raises(SystemExit):
            self.raise_system_exit()


    # Fixture
    @pytest.fixture
    def get_browser_instance(self):
        scraper = Scraper()
        return scraper.get_browser_instance("https://www.google.co.za")


    @pytest.fixture
    def get_soup(self):
        scraper = Scraper()
        source = scraper.get_browser_instance("https://www.google.co.za")
        return scraper.get_page_soup(source)


    #001
    # Test if driver is available
    def test_if_driver_available(self, get_browser_instance):
        assert get_browser_instance


    #002
    # Check if page element can be found
    def test_get_page_element(self, get_soup):
        pass
