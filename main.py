#!/usr/bin/env python
# -*- coding: utf-8 -*-

# System imports
import sys
# +++++++++++++++++++
# Framework imports
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine
from bangerang import Bangerang
# +++++++++++++++++++

app = QApplication(sys.argv)
app.setOrganizationName("bangerang")
app.setOrganizationDomain("www.facebook.com/trojandesigns")

bangerang = Bangerang()

engine = QQmlApplicationEngine()
engine.rootContext().setContextProperty('Bangerang', bangerang)
engine.load('resources/qml/main.qml')
engine.quit.connect(app.quit)

sys.exit(app.exec_())