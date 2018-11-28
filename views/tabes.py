# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uis/tabes.ui'
#
# Created: Sun Jul 23 20:11:56 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_TabWidget(object):
    def setupUi(self, TabWidget):
        TabWidget.setObjectName("TabWidget")
        TabWidget.resize(755, 523)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/n/img/home.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TabWidget.setWindowIcon(icon)
        TabWidget.setStyleSheet(".QTabBar::tab { background: gray; color: white; } \n"
".QTabBar::tab:selected { background: #44D9E6;color: black; } \n"
".QTabWidget::pane { border: 0; } \n"
".QWidget { background: #44D9E6; }\n"
".Line\n"
"{\n"
"background:#000;\n"
"color:#000;\n"
"}")

        self.retranslateUi(TabWidget)
        TabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    def retranslateUi(self, TabWidget):
        TabWidget.setWindowTitle(QtGui.QApplication.translate("TabWidget", "batcoders.com", None, QtGui.QApplication.UnicodeUTF8))

import source_rc
