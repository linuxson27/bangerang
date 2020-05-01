#!/usr/bin/env python
# -*- coding: utf-8 -*-

# bangerang - series/movies local file manager and viewer
__author__ = "A Jones/N Rudman"
__copyright__ = "Copyright 2020"
__version__ = "v0.1-alpha"
__maintainer__ = "A Jones, N Rudman"
__email__ = "linuxson27@gmail.com"
__contact__ = ""
__date__ = "02 May 2020"
__license__ = "MIT"
# ---------------------------------------------------------------------------->
# System imports
import git
import threading
import configparser
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QTimer, QStandardPaths
#+++++++++++++++
# Helpers and utils imports
#+++++++++++++++

class Bangerang(QObject):
    """
    Main Bangerang class
    """
    #Argument used to expose string to QML
    error = pyqtSignal(list, arguments=['payload'])

    def __init__(self):
        QObject.__init__(self)
