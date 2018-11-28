# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uis/special_price.ui'
#
# Created: Thu Jul 19 05:03:21 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 123)
        Form.setStyleSheet(".QWidget { background: #44D9E6; }")
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtGui.QWidget(Form)
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtGui.QGridLayout(self.widget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget_2 = QtGui.QWidget(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_2 = QtGui.QGridLayout(self.widget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.price_spn = QtGui.QDoubleSpinBox(self.widget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.price_spn.sizePolicy().hasHeightForWidth())
        self.price_spn.setSizePolicy(sizePolicy)
        self.price_spn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.price_spn.setAlignment(QtCore.Qt.AlignCenter)
        self.price_spn.setObjectName("price_spn")
        self.gridLayout_2.addWidget(self.price_spn, 0, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.widget_2)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.widget_2, 0, 0, 1, 2)
        self.close_btn = QtGui.QPushButton(self.widget)
        self.close_btn.setObjectName("close_btn")
        self.gridLayout_3.addWidget(self.close_btn, 1, 0, 1, 1)
        self.add_btn = QtGui.QPushButton(self.widget)
        self.add_btn.setObjectName("add_btn")
        self.gridLayout_3.addWidget(self.add_btn, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "السعر الجديد", None, QtGui.QApplication.UnicodeUTF8))
        self.close_btn.setText(QtGui.QApplication.translate("Form", "الغاء", None, QtGui.QApplication.UnicodeUTF8))
        self.add_btn.setText(QtGui.QApplication.translate("Form", "تم", None, QtGui.QApplication.UnicodeUTF8))

