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
logzero.logfile("logs/tests_bangerang.log", maxBytes=1e6, backupCount=3)
#+++++++++++++++
# Tested module imports
try:    # Wrapped in try/except to catch import/file errors
    import bangerang
except Exception as e:
    logger.exception("Import Error")
    raise e
#+++++++++++++++


class TestBangerang:
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


    #001
    # Check if logfile is present and created
    def test_logfile_exists(self):
        logfile = "logs/logfile.log"
        assert path.exists(logfile)


    #002
    # Test if main primer object is subclassed from QObject
    def test_bangerang_is_qobject(self):
        obj = bangerang.Bangerang()
        assert isinstance(obj, QObject)