# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/about.ui'
#
# Created: Sun Apr 23 12:44:48 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(752, 500)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/n/img/home.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_3 = QtGui.QWidget(Form)
        self.widget_3.setStyleSheet(".QWidget { background: #44D9E6; }")
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtGui.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.widget = QtGui.QWidget(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setStyleSheet("background:url(:/n/img/batman-logo.png) no-repeat;\n"
"background-position:ceneter;")
        self.widget.setObjectName("widget")
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2.addWidget(self.widget)
        self.info_lbl = QtGui.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.info_lbl.setFont(font)
        self.info_lbl.setText("")
        self.info_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.info_lbl.setOpenExternalLinks(True)
        self.info_lbl.setObjectName("info_lbl")
        self.verticalLayout_2.addWidget(self.info_lbl)
        self.widget_2 = QtGui.QWidget(self.widget_3)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.phone_btn = QtGui.QPushButton(self.widget_2)
        self.phone_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/n/img/phone-symbol-of-an-auricular-inside-a-circle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.phone_btn.setIcon(icon1)
        self.phone_btn.setIconSize(QtCore.QSize(50, 50))
        self.phone_btn.setFlat(True)
        self.phone_btn.setObjectName("phone_btn")
        self.horizontalLayout.addWidget(self.phone_btn)
        self.fb_btn = QtGui.QPushButton(self.widget_2)
        self.fb_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/n/img/facebook-logo-button (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fb_btn.setIcon(icon2)
        self.fb_btn.setIconSize(QtCore.QSize(50, 50))
        self.fb_btn.setFlat(True)
        self.fb_btn.setObjectName("fb_btn")
        self.horizontalLayout.addWidget(self.fb_btn)
        self.twit_btn = QtGui.QPushButton(self.widget_2)
        self.twit_btn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/n/img/twitter-logo-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.twit_btn.setIcon(icon3)
        self.twit_btn.setIconSize(QtCore.QSize(50, 50))
        self.twit_btn.setFlat(True)
        self.twit_btn.setObjectName("twit_btn")
        self.horizontalLayout.addWidget(self.twit_btn)
        self.ins_btn = QtGui.QPushButton(self.widget_2)
        self.ins_btn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/n/img/instagram-logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ins_btn.setIcon(icon4)
        self.ins_btn.setIconSize(QtCore.QSize(50, 50))
        self.ins_btn.setFlat(True)
        self.ins_btn.setObjectName("ins_btn")
        self.horizontalLayout.addWidget(self.ins_btn)
        self.mail_btn = QtGui.QPushButton(self.widget_2)
        self.mail_btn.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/n/img/email.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mail_btn.setIcon(icon5)
        self.mail_btn.setIconSize(QtCore.QSize(50, 50))
        self.mail_btn.setFlat(True)
        self.mail_btn.setObjectName("mail_btn")
        self.horizontalLayout.addWidget(self.mail_btn)
        self.site_btn = QtGui.QPushButton(self.widget_2)
        self.site_btn.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/n/img/Worldwide Location-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.site_btn.setIcon(icon6)
        self.site_btn.setIconSize(QtCore.QSize(50, 50))
        self.site_btn.setFlat(True)
        self.site_btn.setObjectName("site_btn")
        self.horizontalLayout.addWidget(self.site_btn)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.verticalLayout.addWidget(self.widget_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "عن الشركة", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "شركة بات كودرز", None, QtGui.QApplication.UnicodeUTF8))
        self.phone_btn.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p align=\"center\">01006371068 | 01006371067</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.fb_btn.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p align=\"center\"><a href=\"https://www.facebook.com/batcoders.company\"><span style=\" text-decoration: underline; color:#0000ff;\">https://www.facebook.com/batcoders.company</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.twit_btn.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p align=\"center\"><a href=\"https://twitter.com/BatCoders\"><span style=\" text-decoration: underline; color:#0000ff;\">https://twitter.com/BatCoders</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.ins_btn.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p align=\"center\"><a href=\"https://www.instagram.com/batcoders/\"><span style=\" text-decoration: underline; color:#0000ff;\">https://www.instagram.com/batcoders/</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.mail_btn.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p align=\"center\">SALES@BATCODERS.COM | BATCODERS@GMAIL.COM | BATCODERS@YAHOO.COM</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.site_btn.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p align=\"center\"><a href=\"http://batcoders.com\"><span style=\" text-decoration: underline; color:#0000ff;\">http://batcoders.com</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

import source_rc
