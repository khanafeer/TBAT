# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uis/bc_num.ui'
#
# Created: Wed Jun 20 19:54:37 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(449, 225)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtGui.QWidget(Form)
        self.widget.setObjectName("widget")
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.a4_w = QtGui.QWidget(self.widget)
        self.a4_w.setObjectName("a4_w")
        self.gridLayout_2 = QtGui.QGridLayout(self.a4_w)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.st_spn = QtGui.QSpinBox(self.a4_w)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.st_spn.sizePolicy().hasHeightForWidth())
        self.st_spn.setSizePolicy(sizePolicy)
        self.st_spn.setAlignment(QtCore.Qt.AlignCenter)
        self.st_spn.setMinimum(1)
        self.st_spn.setMaximum(999999999)
        self.st_spn.setObjectName("st_spn")
        self.gridLayout_2.addWidget(self.st_spn, 5, 0, 1, 1)
        self.h_num_spn = QtGui.QSpinBox(self.a4_w)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.h_num_spn.sizePolicy().hasHeightForWidth())
        self.h_num_spn.setSizePolicy(sizePolicy)
        self.h_num_spn.setAlignment(QtCore.Qt.AlignCenter)
        self.h_num_spn.setMinimum(1)
        self.h_num_spn.setMaximum(999999999)
        self.h_num_spn.setObjectName("h_num_spn")
        self.gridLayout_2.addWidget(self.h_num_spn, 0, 0, 1, 1)
        self.st_lbl = QtGui.QLabel(self.a4_w)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.st_lbl.sizePolicy().hasHeightForWidth())
        self.st_lbl.setSizePolicy(sizePolicy)
        self.st_lbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.st_lbl.setObjectName("st_lbl")
        self.gridLayout_2.addWidget(self.st_lbl, 5, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.a4_w)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.a4_w)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.a4_w)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 4, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.a4_w)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 3, 1, 1, 1)
        self.v_num_spn = QtGui.QSpinBox(self.a4_w)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.v_num_spn.sizePolicy().hasHeightForWidth())
        self.v_num_spn.setSizePolicy(sizePolicy)
        self.v_num_spn.setAlignment(QtCore.Qt.AlignCenter)
        self.v_num_spn.setMinimum(1)
        self.v_num_spn.setMaximum(999999999)
        self.v_num_spn.setObjectName("v_num_spn")
        self.gridLayout_2.addWidget(self.v_num_spn, 2, 0, 1, 1)
        self.w_sin = QtGui.QDoubleSpinBox(self.a4_w)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w_sin.sizePolicy().hasHeightForWidth())
        self.w_sin.setSizePolicy(sizePolicy)
        self.w_sin.setAlignment(QtCore.Qt.AlignCenter)
        self.w_sin.setMaximum(999999999.0)
        self.w_sin.setObjectName("w_sin")
        self.gridLayout_2.addWidget(self.w_sin, 3, 0, 1, 1)
        self.height_spn = QtGui.QDoubleSpinBox(self.a4_w)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.height_spn.sizePolicy().hasHeightForWidth())
        self.height_spn.setSizePolicy(sizePolicy)
        self.height_spn.setAlignment(QtCore.Qt.AlignCenter)
        self.height_spn.setMaximum(999999999.0)
        self.height_spn.setObjectName("height_spn")
        self.gridLayout_2.addWidget(self.height_spn, 4, 0, 1, 1)
        self.gridLayout.addWidget(self.a4_w, 1, 0, 4, 1)
        self.widget_2 = QtGui.QWidget(self.widget)
        self.widget_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.widget_2.setAutoFillBackground(False)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.one_rd = QtGui.QRadioButton(self.widget_2)
        self.one_rd.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.one_rd.setChecked(True)
        self.one_rd.setObjectName("one_rd")
        self.horizontalLayout.addWidget(self.one_rd)
        self.two_rd = QtGui.QRadioButton(self.widget_2)
        self.two_rd.setObjectName("two_rd")
        self.horizontalLayout.addWidget(self.two_rd)
        self.a4_rd = QtGui.QRadioButton(self.widget_2)
        self.a4_rd.setObjectName("a4_rd")
        self.horizontalLayout.addWidget(self.a4_rd)
        self.gridLayout.addWidget(self.widget_2, 1, 2, 1, 2)
        self.line = QtGui.QFrame(self.widget)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 1, 4, 1)
        self.pr_num = QtGui.QSpinBox(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pr_num.sizePolicy().hasHeightForWidth())
        self.pr_num.setSizePolicy(sizePolicy)
        self.pr_num.setAlignment(QtCore.Qt.AlignCenter)
        self.pr_num.setMaximum(999999999)
        self.pr_num.setProperty("value", 1)
        self.pr_num.setObjectName("pr_num")
        self.gridLayout.addWidget(self.pr_num, 2, 2, 1, 1)
        self.label = QtGui.QLabel(self.widget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 3, 1, 1)
        self.details_edt = QtGui.QLineEdit(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.details_edt.sizePolicy().hasHeightForWidth())
        self.details_edt.setSizePolicy(sizePolicy)
        self.details_edt.setAlignment(QtCore.Qt.AlignCenter)
        self.details_edt.setObjectName("details_edt")
        self.gridLayout.addWidget(self.details_edt, 3, 2, 1, 1)
        self.pushButton = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/n/img/Printer Door Open Filled-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 2, 1, 2)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 3, 1, 1)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "تفاصيل الطباعة", None, QtGui.QApplication.UnicodeUTF8))
        self.st_lbl.setText(QtGui.QApplication.translate("Form", "البداية", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "العدد فى  الارتفاع", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "العدد فى العرض", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "الارتفاع", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Form", "العرض", None, QtGui.QApplication.UnicodeUTF8))
        self.one_rd.setText(QtGui.QApplication.translate("Form", "ورقة", None, QtGui.QApplication.UnicodeUTF8))
        self.two_rd.setText(QtGui.QApplication.translate("Form", "ورقتين", None, QtGui.QApplication.UnicodeUTF8))
        self.a4_rd.setText(QtGui.QApplication.translate("Form", "A4", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "العدد", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "طباعة", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "التفاصيل", None, QtGui.QApplication.UnicodeUTF8))

import source_rc
