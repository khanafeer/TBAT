# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uis/student_enter.ui'
#
# Created: Mon Aug  7 03:03:34 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(867, 537)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtGui.QWidget(Form)
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_2 = QtGui.QWidget(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_5 = QtGui.QWidget(self.widget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout.addWidget(self.widget_5)
        self.widget_6 = QtGui.QWidget(self.widget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widget_6)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_9 = QtGui.QWidget(self.widget_6)
        self.widget_9.setObjectName("widget_9")
        self.gridLayout_3 = QtGui.QGridLayout(self.widget_9)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.st_search = QtGui.QLineEdit(self.widget_9)
        self.st_search.setAlignment(QtCore.Qt.AlignCenter)
        self.st_search.setPlaceholderText("")
        self.st_search.setObjectName("st_search")
        self.gridLayout_3.addWidget(self.st_search, 0, 2, 1, 1)
        self.auto_attend = QtGui.QCheckBox(self.widget_9)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.auto_attend.sizePolicy().hasHeightForWidth())
        self.auto_attend.setSizePolicy(sizePolicy)
        self.auto_attend.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.auto_attend.setChecked(True)
        self.auto_attend.setObjectName("auto_attend")
        self.gridLayout_3.addWidget(self.auto_attend, 0, 1, 1, 1)
        self.widget_15 = QtGui.QWidget(self.widget_9)
        self.widget_15.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.widget_15.setStyleSheet(".QWidget\n"
"{\n"
"background:rgba(255, 255, 255,150);\n"
"}")
        self.widget_15.setObjectName("widget_15")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget_15)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gp_rd = QtGui.QRadioButton(self.widget_15)
        self.gp_rd.setChecked(True)
        self.gp_rd.setObjectName("gp_rd")
        self.horizontalLayout_3.addWidget(self.gp_rd)
        self.ex_rd = QtGui.QRadioButton(self.widget_15)
        self.ex_rd.setObjectName("ex_rd")
        self.horizontalLayout_3.addWidget(self.ex_rd)
        self.gridLayout_3.addWidget(self.widget_15, 1, 2, 1, 1)
        self.exam_cmb = QtGui.QComboBox(self.widget_9)
        self.exam_cmb.setObjectName("exam_cmb")
        self.gridLayout_3.addWidget(self.exam_cmb, 1, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.widget_9)
        self.widget_13 = QtGui.QWidget(self.widget_6)
        self.widget_13.setObjectName("widget_13")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget_13)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.exam_btn = QtGui.QPushButton(self.widget_13)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exam_btn.sizePolicy().hasHeightForWidth())
        self.exam_btn.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/n/img/Bullish-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exam_btn.setIcon(icon)
        self.exam_btn.setIconSize(QtCore.QSize(40, 40))
        self.exam_btn.setFlat(True)
        self.exam_btn.setObjectName("exam_btn")
        self.horizontalLayout_4.addWidget(self.exam_btn)
        self.mony_btn = QtGui.QPushButton(self.widget_13)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mony_btn.sizePolicy().hasHeightForWidth())
        self.mony_btn.setSizePolicy(sizePolicy)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/n/img/Cash In Hand-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mony_btn.setIcon(icon1)
        self.mony_btn.setIconSize(QtCore.QSize(40, 40))
        self.mony_btn.setFlat(True)
        self.mony_btn.setObjectName("mony_btn")
        self.horizontalLayout_4.addWidget(self.mony_btn)
        self.attend_btn = QtGui.QPushButton(self.widget_13)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.attend_btn.sizePolicy().hasHeightForWidth())
        self.attend_btn.setSizePolicy(sizePolicy)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/n/img/Event Accepted Tentatively Filled-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.attend_btn.setIcon(icon2)
        self.attend_btn.setIconSize(QtCore.QSize(30, 30))
        self.attend_btn.setFlat(True)
        self.attend_btn.setObjectName("attend_btn")
        self.horizontalLayout_4.addWidget(self.attend_btn)
        self.search_btn = QtGui.QPushButton(self.widget_13)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/n/img/Search-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_btn.setIcon(icon3)
        self.search_btn.setIconSize(QtCore.QSize(50, 50))
        self.search_btn.setFlat(True)
        self.search_btn.setObjectName("search_btn")
        self.horizontalLayout_4.addWidget(self.search_btn)
        self.verticalLayout_3.addWidget(self.widget_13)
        self.horizontalLayout.addWidget(self.widget_6)
        self.widget_7 = QtGui.QWidget(self.widget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout.addWidget(self.widget_7)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.widget_4 = QtGui.QWidget(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.widget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.result_lbl = QtGui.QLabel(self.widget_4)
        self.result_lbl.setText("")
        self.result_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.result_lbl.setObjectName("result_lbl")
        self.verticalLayout_4.addWidget(self.result_lbl)
        self.verticalLayout_2.addWidget(self.widget_4)
        self.line_2 = QtGui.QFrame(self.widget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.widget_3 = QtGui.QWidget(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setStyleSheet("")
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.exams_dw = QtGui.QWidget(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.exams_dw.sizePolicy().hasHeightForWidth())
        self.exams_dw.setSizePolicy(sizePolicy)
        self.exams_dw.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.exams_dw.setObjectName("exams_dw")
        self.gridLayout_4 = QtGui.QGridLayout(self.exams_dw)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setHorizontalSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.days_lbl_2 = QtGui.QLabel(self.exams_dw)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.days_lbl_2.sizePolicy().hasHeightForWidth())
        self.days_lbl_2.setSizePolicy(sizePolicy)
        self.days_lbl_2.setAlignment(QtCore.Qt.AlignCenter)
        self.days_lbl_2.setObjectName("days_lbl_2")
        self.gridLayout_4.addWidget(self.days_lbl_2, 2, 0, 1, 1)
        self.hours_lbl_2 = QtGui.QLabel(self.exams_dw)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hours_lbl_2.sizePolicy().hasHeightForWidth())
        self.hours_lbl_2.setSizePolicy(sizePolicy)
        self.hours_lbl_2.setAlignment(QtCore.Qt.AlignCenter)
        self.hours_lbl_2.setObjectName("hours_lbl_2")
        self.gridLayout_4.addWidget(self.hours_lbl_2, 4, 0, 1, 1)
        self.name_lbl_3 = QtGui.QLabel(self.exams_dw)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_lbl_3.sizePolicy().hasHeightForWidth())
        self.name_lbl_3.setSizePolicy(sizePolicy)
        self.name_lbl_3.setAlignment(QtCore.Qt.AlignCenter)
        self.name_lbl_3.setObjectName("name_lbl_3")
        self.gridLayout_4.addWidget(self.name_lbl_3, 0, 0, 1, 1)
        self.label_16 = QtGui.QLabel(self.exams_dw)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout_4.addWidget(self.label_16, 2, 1, 1, 1)
        self.label_17 = QtGui.QLabel(self.exams_dw)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout_4.addWidget(self.label_17, 7, 1, 1, 1)
        self.label_19 = QtGui.QLabel(self.exams_dw)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.gridLayout_4.addWidget(self.label_19, 4, 1, 1, 1)
        self.label_20 = QtGui.QLabel(self.exams_dw)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout_4.addWidget(self.label_20, 3, 1, 1, 1)
        self.details_lbl_3 = QtGui.QLabel(self.exams_dw)
        self.details_lbl_3.setAlignment(QtCore.Qt.AlignCenter)
        self.details_lbl_3.setObjectName("details_lbl_3")
        self.gridLayout_4.addWidget(self.details_lbl_3, 7, 0, 1, 1)
        self.label_18 = QtGui.QLabel(self.exams_dw)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout_4.addWidget(self.label_18, 0, 1, 1, 1)
        self.max_lbl = QtGui.QLabel(self.exams_dw)
        self.max_lbl.setText("")
        self.max_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.max_lbl.setObjectName("max_lbl")
        self.gridLayout_4.addWidget(self.max_lbl, 3, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.exams_dw)
        self.courses_dw = QtGui.QWidget(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.courses_dw.sizePolicy().hasHeightForWidth())
        self.courses_dw.setSizePolicy(sizePolicy)
        self.courses_dw.setObjectName("courses_dw")
        self.gridLayout_2 = QtGui.QGridLayout(self.courses_dw)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setHorizontalSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.hours_lbl = QtGui.QLabel(self.courses_dw)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hours_lbl.sizePolicy().hasHeightForWidth())
        self.hours_lbl.setSizePolicy(sizePolicy)
        self.hours_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.hours_lbl.setObjectName("hours_lbl")
        self.gridLayout_2.addWidget(self.hours_lbl, 4, 1, 1, 1)
        self.days_lbl = QtGui.QLabel(self.courses_dw)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.days_lbl.sizePolicy().hasHeightForWidth())
        self.days_lbl.setSizePolicy(sizePolicy)
        self.days_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.days_lbl.setObjectName("days_lbl")
        self.gridLayout_2.addWidget(self.days_lbl, 2, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.courses_dw)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 2, 1, 1)
        self.label_10 = QtGui.QLabel(self.courses_dw)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 4, 2, 1, 1)
        self.inst_lbl = QtGui.QLabel(self.courses_dw)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inst_lbl.sizePolicy().hasHeightForWidth())
        self.inst_lbl.setSizePolicy(sizePolicy)
        self.inst_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.inst_lbl.setObjectName("inst_lbl")
        self.gridLayout_2.addWidget(self.inst_lbl, 7, 1, 1, 1)
        self.name_lbl_2 = QtGui.QLabel(self.courses_dw)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_lbl_2.sizePolicy().hasHeightForWidth())
        self.name_lbl_2.setSizePolicy(sizePolicy)
        self.name_lbl_2.setAlignment(QtCore.Qt.AlignCenter)
        self.name_lbl_2.setObjectName("name_lbl_2")
        self.gridLayout_2.addWidget(self.name_lbl_2, 0, 1, 1, 1)
        self.bill_method = QtGui.QLabel(self.courses_dw)
        self.bill_method.setText("")
        self.bill_method.setAlignment(QtCore.Qt.AlignCenter)
        self.bill_method.setObjectName("bill_method")
        self.gridLayout_2.addWidget(self.bill_method, 5, 1, 1, 1)
        self.price_lbl = QtGui.QLabel(self.courses_dw)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.price_lbl.sizePolicy().hasHeightForWidth())
        self.price_lbl.setSizePolicy(sizePolicy)
        self.price_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.price_lbl.setObjectName("price_lbl")
        self.gridLayout_2.addWidget(self.price_lbl, 6, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.courses_dw)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 7, 2, 1, 1)
        self.label_15 = QtGui.QLabel(self.courses_dw)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 6, 2, 1, 1)
        self.label_9 = QtGui.QLabel(self.courses_dw)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 2, 2, 1, 1)
        self.label_14 = QtGui.QLabel(self.courses_dw)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 5, 2, 1, 1)
        self.label_11 = QtGui.QLabel(self.courses_dw)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 8, 2, 1, 1)
        self.details_lbl_2 = QtGui.QLabel(self.courses_dw)
        self.details_lbl_2.setAlignment(QtCore.Qt.AlignCenter)
        self.details_lbl_2.setObjectName("details_lbl_2")
        self.gridLayout_2.addWidget(self.details_lbl_2, 8, 1, 1, 1)
        self.horizontalLayout_2.addWidget(self.courses_dw)
        self.line = QtGui.QFrame(self.widget_3)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.widget_8 = QtGui.QWidget(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy)
        self.widget_8.setObjectName("widget_8")
        self.gridLayout = QtGui.QGridLayout(self.widget_8)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.ph_lbl = QtGui.QLabel(self.widget_8)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ph_lbl.sizePolicy().hasHeightForWidth())
        self.ph_lbl.setSizePolicy(sizePolicy)
        self.ph_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.ph_lbl.setObjectName("ph_lbl")
        self.gridLayout.addWidget(self.ph_lbl, 6, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.widget_8)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 1, 1, 1)
        self.bc_label = QtGui.QLabel(self.widget_8)
        self.bc_label.setText("")
        self.bc_label.setAlignment(QtCore.Qt.AlignCenter)
        self.bc_label.setObjectName("bc_label")
        self.gridLayout.addWidget(self.bc_label, 1, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.widget_8)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 11, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.widget_8)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 10, 1, 1, 1)
        self.add_lbl = QtGui.QLabel(self.widget_8)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_lbl.sizePolicy().hasHeightForWidth())
        self.add_lbl.setSizePolicy(sizePolicy)
        self.add_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.add_lbl.setObjectName("add_lbl")
        self.gridLayout.addWidget(self.add_lbl, 11, 0, 1, 1)
        self.mail_lbl = QtGui.QLabel(self.widget_8)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mail_lbl.sizePolicy().hasHeightForWidth())
        self.mail_lbl.setSizePolicy(sizePolicy)
        self.mail_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.mail_lbl.setObjectName("mail_lbl")
        self.gridLayout.addWidget(self.mail_lbl, 10, 0, 1, 1)
        self.details_lbl = QtGui.QLabel(self.widget_8)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.details_lbl.sizePolicy().hasHeightForWidth())
        self.details_lbl.setSizePolicy(sizePolicy)
        self.details_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.details_lbl.setObjectName("details_lbl")
        self.gridLayout.addWidget(self.details_lbl, 12, 0, 1, 1)
        self.label = QtGui.QLabel(self.widget_8)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 6, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.widget_8)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 12, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.widget_8)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 1, 1, 1)
        self.name_lbl = QtGui.QLabel(self.widget_8)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_lbl.sizePolicy().hasHeightForWidth())
        self.name_lbl.setSizePolicy(sizePolicy)
        self.name_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.name_lbl.setObjectName("name_lbl")
        self.gridLayout.addWidget(self.name_lbl, 3, 0, 1, 1)
        self.school_lbl = QtGui.QLabel(self.widget_8)
        self.school_lbl.setText("")
        self.school_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.school_lbl.setObjectName("school_lbl")
        self.gridLayout.addWidget(self.school_lbl, 4, 0, 1, 1)
        self.label_12 = QtGui.QLabel(self.widget_8)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 4, 1, 1, 1)
        self.label_13 = QtGui.QLabel(self.widget_8)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 7, 1, 1, 1)
        self.fph_lbl = QtGui.QLabel(self.widget_8)
        self.fph_lbl.setText("")
        self.fph_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.fph_lbl.setObjectName("fph_lbl")
        self.gridLayout.addWidget(self.fph_lbl, 7, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.widget_8)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.auto_attend.setText(QtGui.QApplication.translate("Form", "تلقائى", None, QtGui.QApplication.UnicodeUTF8))
        self.gp_rd.setText(QtGui.QApplication.translate("Form", "مجموعة", None, QtGui.QApplication.UnicodeUTF8))
        self.ex_rd.setText(QtGui.QApplication.translate("Form", "اختبار", None, QtGui.QApplication.UnicodeUTF8))
        self.exam_btn.setText(QtGui.QApplication.translate("Form", "الدرجة", None, QtGui.QApplication.UnicodeUTF8))
        self.mony_btn.setText(QtGui.QApplication.translate("Form", "دفع", None, QtGui.QApplication.UnicodeUTF8))
        self.attend_btn.setText(QtGui.QApplication.translate("Form", "حضور", None, QtGui.QApplication.UnicodeUTF8))
        self.search_btn.setText(QtGui.QApplication.translate("Form", "بحث", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("Form", "عدد الاختبارات", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("Form", "التفاصيل", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("Form", "عدد ساعات الاختبار", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("Form", "الدرجة العظمى", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("Form", "اسم الاختبار", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Form", "اسم الدورة", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Form", "عدد ساعات المحاضرة", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Form", "المحاضر", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("Form", "السعر", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Form", "عدد المحاضرات", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("Form", "نظام الدفع", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("Form", "تفاصيل", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "اسم الطالب", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "العنوان", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "البريد الالكترونى", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "هاتف الطالب", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "التفاصيل", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Form", "الباركود", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("Form", "المدرسة", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("Form", "هاتف ولى الامر", None, QtGui.QApplication.UnicodeUTF8))

import source_rc