# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uis/exam_add.ui'
#
# Created: Sun Feb 11 02:37:26 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(760, 579)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtGui.QWidget(Form)
        self.widget.setObjectName("widget")
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.search_edt = QtGui.QLineEdit(self.widget)
        self.search_edt.setAlignment(QtCore.Qt.AlignCenter)
        self.search_edt.setObjectName("search_edt")
        self.gridLayout.addWidget(self.search_edt, 0, 1, 1, 1)
        self.add_btn = QtGui.QPushButton(self.widget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/n/img/Plus-500.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_btn.setIcon(icon)
        self.add_btn.setIconSize(QtCore.QSize(30, 30))
        self.add_btn.setObjectName("add_btn")
        self.gridLayout.addWidget(self.add_btn, 2, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.widget)
        self.tableView = QtGui.QTableView(Form)
        self.tableView.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.search_edt.setPlaceholderText(QtGui.QApplication.translate("Form", "بحث", None, QtGui.QApplication.UnicodeUTF8))
        self.add_btn.setText(QtGui.QApplication.translate("Form", "اضافة", None, QtGui.QApplication.UnicodeUTF8))

import source_rc
