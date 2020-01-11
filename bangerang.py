# bangerang - series/movies local file manager and viewer
__author__ = "A Jones"
__copyright__ = "Copyright 2019"
__version__ = "v0.1-alpha"
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
from resources.utils.errors import translate_error
#+++++++++++++++

class Bangerang(QObject):
    """
    Main Bangerang class
    """
    #Argument used to expose string to QML
    error = pyqtSignal(list, arguments=['payload'])
    notify = pyqtSignal(list, arguments=['payload'])
    finished_loading = pyqtSignal(str, arguments=['callback'])
    config = pyqtSignal(list, arguments=['config'])
    config_check = pyqtSignal(list , arguments=['callback'])
    profiles = pyqtSignal(str, arguments=['profiles'])

    def __init__(self):
        QObject.__init__(self)


    #001
    @pyqtSlot()
    def check_update(self):
        """
        Thread worker used to run update method
        """
        update_thread = threading.Thread(target=self._check_update)
        update_thread.daemon = True
        update_thread.start()


    #001
    def _check_update(self):
        """
        Thread which checks for updates against
        the remote github repo. Emits a signal
        with either 'current' or 'update' parameters
        depending on the equality check between
        local and remote version numbers
        """
        try:
            remote_ver = self.get_remote_tag()
            if remote_ver != None:
                if __version__ != remote_ver:
                    self.finished_loading.emit('update')
                else:
                    self.finished_loading.emit('current')
            else:
                self.finished_loading.emit('current')
        except Exception as e:
            error = translate_error(e)
            self.error.emit(error)


    #001
    def get_remote_tag(self):
        """
        Collects remote refs and strips down to just
        the tag numbers for reference, sorted chronologically

        :return:                "v0.1-alpha"
        """
        remote_refs_list = []
        remote_tags_list = []
        g = git.cmd.Git()
        remote_refs = g.ls_remote('https://github.com/linuxson27/bangerang.git')
        
        for ref in remote_refs.split('\n'):
            hash_ref_list = ref.split('\t')
            remote_refs_list.append(hash_ref_list)

        for ref_hash in remote_refs_list:
            for ref in ref_hash:
                if 'tags' in ref:
                    ver = ref.split('/')
                    remote_tags_list.append(ver[2])
        print(remote_tags_list)
        if len(remote_tags_list) > 0:
            remote_ver = remote_tags_list[-1]
        else:
            remote_ver = None
        
        return remote_ver


    #002
    @pyqtSlot()
    def download_update(self):
        """
        Thread worker which runs the download function
        """
        download_thread = threading.Thread(target=self._download_update)
        download_thread.daemon = True
        download_thread.start()


    #002
    def _download_update(self):
        """
        Thread runs when the update check returns 'update'
        Opens a new browser window which initiates the download,
        letting the user choose where to download to
        """
        try:
            remote_ver = self.get_remote_tag()
            url = "https://github.com/linuxson27/bangerang/releases/download/" + \
                    remote_ver + "/bangerang-" + \
                    remote_ver + ".exe"
            webbrowser.open(url)
        except Exception as e:
            error = translate_error(e)
            self.error.emit(error)


    #003
    @pyqtSlot(bool)
    def get_config(self, req):
        """
        Reads config values from .ini file - mostly
        used to store db connection parameters and user details
        Depending on 'req' bool, will either return, or emit signal
        with all the required values

        :param req:             int
        :return:                []
        """
        config = configparser.ConfigParser()
        config.read('config.ini')
        pass


    #003
    @pyqtSlot()
    def check_config(self):
        """
        Checks the domain config group for any empty
        fields, and if present, calls to have the createUserPopup
        modal shown. If not, calls to have the connection checked
        """
        config_present = False

        params = self.get_config(1)
        app_init = params[0]

        if app_init[1] == "true":
            self.config_check.emit(['incomplete'])
        else:
            for value in domain_params:
                if value != "":
                    config_present = True
                else:
                    config_present = False
                    break

            if config_present:
                self.check_connection()
            else:
                self.config_check.emit(['incomplete'])


    #003
    @pyqtSlot(list)
    def write_config(self, data):
        """
        Writes the config back to the .ini file, called
        from the settingsPopup modal when the save button is clicked

        :param data:            list which contains new config.ini entries
        """
        config = configparser.ConfigParser()
        config.read('config.ini')

        # config.set('APP', 'initial_startup', 'false')

        # config.set('DOMAIN_PARAMS', 'domain', data[0])
        # config.set('DOMAIN_PARAMS', 'user', data[2])
        # config.set('DOMAIN_PARAMS', 'password', data[4])

        # config.set('DB_PARAMS', 'dbname', data[1])
        # config.set('DB_PARAMS', 'user', data[3])
        # config.set('DB_PARAMS', 'password', data[5])

        # with open('config.ini', 'w') as config_file:
        #     config.write(config_file)
        pass


    @pyqtSlot()
    def get_profiles(self):
        self.profiles.emit("All user profiles")