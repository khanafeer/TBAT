# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'info_dw.ui'
#
# Created: Tue Jul 18 12:18:36 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(641, 406)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/n/img/home.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.info_table = QtGui.QTableWidget(Form)
        self.info_table.setObjectName("info_table")
        self.info_table.setColumnCount(0)
        self.info_table.setRowCount(0)
        self.verticalLayout.addWidget(self.info_table)
        self.print_btn = QtGui.QPushButton(Form)
        self.print_btn.setObjectName("print_btn")
        self.verticalLayout.addWidget(self.print_btn)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "تفاصيل", None, QtGui.QApplication.UnicodeUTF8))
        self.print_btn.setText(QtGui.QApplication.translate("Form", "طباعة", None, QtGui.QApplication.UnicodeUTF8))

import source_rc
