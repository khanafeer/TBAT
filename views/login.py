# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uis/login.ui'
#
# Created: Tue Feb 06 01:57:23 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(845, 554)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_w = QtGui.QWidget(Form)
        self.main_w.setStyleSheet("")
        self.main_w.setObjectName("main_w")
        self.gridLayout_2 = QtGui.QGridLayout(self.main_w)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget_2 = QtGui.QWidget(self.main_w)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_2.addWidget(self.widget_2, 1, 2, 1, 1)
        self.login_w = QtGui.QWidget(self.main_w)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(6)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.login_w.sizePolicy().hasHeightForWidth())
        self.login_w.setSizePolicy(sizePolicy)
        self.login_w.setMinimumSize(QtCore.QSize(320, 200))
        self.login_w.setStyleSheet(".QWidget\n"
"{\n"
"background:rgba(0, 0, 0,150);\n"
"border-radius:10px;\n"
"}\n"
"QLineEdit\n"
"{\n"
"color:#000;\n"
"border: 1px solid #032632;\n"
"}\n"
".QLabel\n"
"{\n"
"color:#fff;\n"
"}\n"
".QPushButton\n"
"{\n"
"background:#000;\n"
"border-radius:8px;\n"
"border: 0px solid;\n"
"color:#fff;\n"
"}\n"
"")
        self.login_w.setObjectName("login_w")
        self.gridLayout = QtGui.QGridLayout(self.login_w)
        self.gridLayout.setContentsMargins(25, 25, 25, 25)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(25)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.user_lbl = QtGui.QLineEdit(self.login_w)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.user_lbl.sizePolicy().hasHeightForWidth())
        self.user_lbl.setSizePolicy(sizePolicy)
        self.user_lbl.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.user_lbl.setFont(font)
        self.user_lbl.setStyleSheet("")
        self.user_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.user_lbl.setObjectName("user_lbl")
        self.gridLayout.addWidget(self.user_lbl, 3, 0, 1, 2)
        self.label = QtGui.QLabel(self.login_w)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("AlArabiya")
        font.setPointSize(48)
        font.setWeight(50)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.login_btn = QtGui.QPushButton(self.login_w)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_btn.sizePolicy().hasHeightForWidth())
        self.login_btn.setSizePolicy(sizePolicy)
        self.login_btn.setMinimumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.login_btn.setFont(font)
        self.login_btn.setCursor(QtCore.Qt.PointingHandCursor)
        self.login_btn.setObjectName("login_btn")
        self.gridLayout.addWidget(self.login_btn, 5, 1, 1, 1)
        self.exit_btn = QtGui.QPushButton(self.login_w)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exit_btn.sizePolicy().hasHeightForWidth())
        self.exit_btn.setSizePolicy(sizePolicy)
        self.exit_btn.setMinimumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.exit_btn.setFont(font)
        self.exit_btn.setCursor(QtCore.Qt.PointingHandCursor)
        self.exit_btn.setObjectName("exit_btn")
        self.gridLayout.addWidget(self.exit_btn, 5, 0, 1, 1)
        self.wrong_pass = QtGui.QLabel(self.login_w)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wrong_pass.sizePolicy().hasHeightForWidth())
        self.wrong_pass.setSizePolicy(sizePolicy)
        self.wrong_pass.setStyleSheet("QLabel\n"
"{\n"
"color:#bd1e1e;\n"
"}")
        self.wrong_pass.setAlignment(QtCore.Qt.AlignCenter)
        self.wrong_pass.setObjectName("wrong_pass")
        self.gridLayout.addWidget(self.wrong_pass, 1, 0, 1, 2)
        self.pass_lbl = QtGui.QLineEdit(self.login_w)
        self.pass_lbl.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pass_lbl.sizePolicy().hasHeightForWidth())
        self.pass_lbl.setSizePolicy(sizePolicy)
        self.pass_lbl.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.pass_lbl.setFont(font)
        self.pass_lbl.setEchoMode(QtGui.QLineEdit.Password)
        self.pass_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.pass_lbl.setObjectName("pass_lbl")
        self.gridLayout.addWidget(self.pass_lbl, 4, 0, 1, 2)
        self.wrong_name = QtGui.QLabel(self.login_w)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wrong_name.sizePolicy().hasHeightForWidth())
        self.wrong_name.setSizePolicy(sizePolicy)
        self.wrong_name.setStyleSheet("QLabel\n"
"{\n"
"color:#bd1e1e;\n"
"}")
        self.wrong_name.setAlignment(QtCore.Qt.AlignCenter)
        self.wrong_name.setObjectName("wrong_name")
        self.gridLayout.addWidget(self.wrong_name, 2, 0, 1, 2)
        self.gridLayout_2.addWidget(self.login_w, 1, 1, 1, 1)
        self.widget_4 = QtGui.QWidget(self.main_w)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_2.addWidget(self.widget_4, 2, 1, 1, 1)
        self.widget_3 = QtGui.QWidget(self.main_w)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_3 = QtGui.QGridLayout(self.widget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2.addWidget(self.widget_3, 0, 1, 1, 1)
        self.widget_6 = QtGui.QWidget(self.main_w)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.widget_6.setObjectName("widget_6")
        self.gridLayout_2.addWidget(self.widget_6, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.main_w)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "تسجيل الدخول", None, QtGui.QApplication.UnicodeUTF8))
        self.user_lbl.setPlaceholderText(QtGui.QApplication.translate("Form", "User name", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "تسجيل الدخول", None, QtGui.QApplication.UnicodeUTF8))
        self.login_btn.setText(QtGui.QApplication.translate("Form", "دخول", None, QtGui.QApplication.UnicodeUTF8))
        self.exit_btn.setText(QtGui.QApplication.translate("Form", "اغلاق", None, QtGui.QApplication.UnicodeUTF8))
        self.wrong_pass.setText(QtGui.QApplication.translate("Form", "الرقم الذى ادخلته غير صحيح", None, QtGui.QApplication.UnicodeUTF8))
        self.pass_lbl.setPlaceholderText(QtGui.QApplication.translate("Form", "password", None, QtGui.QApplication.UnicodeUTF8))
        self.wrong_name.setText(QtGui.QApplication.translate("Form", "اﻻسم الذى ادخلته غير صحيح", None, QtGui.QApplication.UnicodeUTF8))

import source_rc
