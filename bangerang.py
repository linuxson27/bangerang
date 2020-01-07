# bangerang - series/movies local file manager and viewer
__author__ = "A Jones"
__copyright__ = "Copyright 2019"
__version__ = "1.0.0"
__maintainer__ = "A Jones"
__email__ = "linuxson27@gmail.com"
__contact__ = "081 028 7472"
__date__ = "7 January 2020"
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
    test = pyqtSignal()
    # finished_loading = pyqtSignal(str, arguments=['callback'])
    # config = pyqtSignal(list, arguments=['config'])
    # config_check = pyqtSignal(list , arguments=['callback'])

    def __init__(self):
        QObject.__init__(self)


    @pyqtSlot()
    def signal_test(self):
        self.test.emit()