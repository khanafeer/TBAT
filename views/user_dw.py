# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/user_dw.ui'
#
# Created: Tue Mar 14 03:56:49 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(300, 152)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtGui.QWidget(Form)
        self.widget.setStyleSheet(".QWidget{\n"
"background:#44D9E6;\n"
"}\n"
".QLabel\n"
"{\n"
"color:#000;\n"
"}")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_33 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("AlArabiya")
        font.setPointSize(14)
        self.label_33.setFont(font)
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.verticalLayout_2.addWidget(self.label_33)
        self.user_edt = QtGui.QLineEdit(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.user_edt.sizePolicy().hasHeightForWidth())
        self.user_edt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("AlArabiya")
        font.setPointSize(14)
        self.user_edt.setFont(font)
        self.user_edt.setAlignment(QtCore.Qt.AlignCenter)
        self.user_edt.setObjectName("user_edt")
        self.verticalLayout_2.addWidget(self.user_edt)
        self.user_search = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.user_search.sizePolicy().hasHeightForWidth())
        self.user_search.setSizePolicy(sizePolicy)
        self.user_search.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/n/img/Search-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.user_search.setIcon(icon)
        self.user_search.setIconSize(QtCore.QSize(50, 50))
        self.user_search.setFlat(True)
        self.user_search.setObjectName("user_search")
        self.verticalLayout_2.addWidget(self.user_search)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_33.setText(QtGui.QApplication.translate("Form", "ابحث عن المستخدم", None, QtGui.QApplication.UnicodeUTF8))
        self.user_edt.setPlaceholderText(QtGui.QApplication.translate("Form", "الرقم - اﻻسم", None, QtGui.QApplication.UnicodeUTF8))

import source_rc
