# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uis/course_add.ui'
#
# Created: Tue Jul 17 12:15:25 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(760, 579)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtGui.QWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout = QtGui.QGridLayout(self.widget_2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        self.print_btn = QtGui.QPushButton(self.widget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.print_btn.sizePolicy().hasHeightForWidth())
        self.print_btn.setSizePolicy(sizePolicy)
        self.print_btn.setMaximumSize(QtCore.QSize(200, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/n/img/Printer Door Open Filled-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.print_btn.setIcon(icon)
        self.print_btn.setObjectName("print_btn")
        self.gridLayout.addWidget(self.print_btn, 1, 1, 1, 1)
        self.search_edt = QtGui.QLineEdit(self.widget_2)
        self.search_edt.setAlignment(QtCore.Qt.AlignCenter)
        self.search_edt.setObjectName("search_edt")
        self.gridLayout.addWidget(self.search_edt, 0, 1, 1, 1)
        self.add_btn = QtGui.QPushButton(self.widget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_btn.sizePolicy().hasHeightForWidth())
        self.add_btn.setSizePolicy(sizePolicy)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/n/img/Plus-500.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_btn.setIcon(icon1)
        self.add_btn.setObjectName("add_btn")
        self.gridLayout.addWidget(self.add_btn, 1, 2, 1, 1)
        self.verticalLayout.addWidget(self.widget_2)
        self.all_courses = QtGui.QTableView(Form)
        self.all_courses.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.all_courses.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.all_courses.setObjectName("all_courses")
        self.verticalLayout.addWidget(self.all_courses)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.print_btn.setText(QtGui.QApplication.translate("Form", "طباعة", None, QtGui.QApplication.UnicodeUTF8))
        self.search_edt.setPlaceholderText(QtGui.QApplication.translate("Form", "اسم المجموعة", None, QtGui.QApplication.UnicodeUTF8))
        self.add_btn.setText(QtGui.QApplication.translate("Form", "اضافة", None, QtGui.QApplication.UnicodeUTF8))

import source_rc
