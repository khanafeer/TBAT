# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uis/report_all.ui'
#
# Created: Tue Jul 17 12:03:23 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(997, 512)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtGui.QWidget(Form)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_3 = QtGui.QWidget(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_6 = QtGui.QWidget(self.widget_3)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget_6)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.grid_btn = QtGui.QPushButton(self.widget_6)
        self.grid_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/n/img/line-chart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.grid_btn.setIcon(icon)
        self.grid_btn.setCheckable(True)
        self.grid_btn.setObjectName("grid_btn")
        self.horizontalLayout_4.addWidget(self.grid_btn)
        self.list_btn = QtGui.QPushButton(self.widget_6)
        self.list_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/n/img/icons8-Select All-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.list_btn.setIcon(icon1)
        self.list_btn.setCheckable(True)
        self.list_btn.setChecked(True)
        self.list_btn.setObjectName("list_btn")
        self.horizontalLayout_4.addWidget(self.list_btn)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.widget_6)
        self.report_w = QtGui.QStackedWidget(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.report_w.sizePolicy().hasHeightForWidth())
        self.report_w.setSizePolicy(sizePolicy)
        self.report_w.setStyleSheet("")
        self.report_w.setObjectName("report_w")
        self.rep_w = QtGui.QWidget()
        self.rep_w.setObjectName("rep_w")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.rep_w)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.info_tbl = QtGui.QTableView(self.rep_w)
        self.info_tbl.setObjectName("info_tbl")
        self.verticalLayout_5.addWidget(self.info_tbl)
        self.report_w.addWidget(self.rep_w)
        self.graph_w = QtGui.QWidget()
        self.graph_w.setObjectName("graph_w")
        self.report_w.addWidget(self.graph_w)
        self.verticalLayout_2.addWidget(self.report_w)
        self.horizontalLayout.addWidget(self.widget_3)
        self.widget_2 = QtGui.QWidget(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_4 = QtGui.QWidget(self.widget_2)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.exm_btn = QtGui.QPushButton(self.widget_4)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/n/img/Bullish-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exm_btn.setIcon(icon2)
        self.exm_btn.setIconSize(QtCore.QSize(30, 30))
        self.exm_btn.setObjectName("exm_btn")
        self.horizontalLayout_2.addWidget(self.exm_btn)
        self.gp_btn = QtGui.QPushButton(self.widget_4)
        self.gp_btn.setIcon(icon)
        self.gp_btn.setIconSize(QtCore.QSize(30, 30))
        self.gp_btn.setObjectName("gp_btn")
        self.horizontalLayout_2.addWidget(self.gp_btn)
        self.all_btn = QtGui.QPushButton(self.widget_4)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/n/img/Worldwide Location-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.all_btn.setIcon(icon3)
        self.all_btn.setIconSize(QtCore.QSize(30, 30))
        self.all_btn.setObjectName("all_btn")
        self.horizontalLayout_2.addWidget(self.all_btn)
        self.verticalLayout_3.addWidget(self.widget_4)
        self.widget_5 = QtGui.QWidget(self.widget_2)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.end_dt = QtGui.QDateTimeEdit(self.widget_5)
        self.end_dt.setCalendarPopup(True)
        self.end_dt.setObjectName("end_dt")
        self.horizontalLayout_3.addWidget(self.end_dt)
        self.start_dt = QtGui.QDateTimeEdit(self.widget_5)
        self.start_dt.setCalendarPopup(True)
        self.start_dt.setObjectName("start_dt")
        self.horizontalLayout_3.addWidget(self.start_dt)
        self.verticalLayout_3.addWidget(self.widget_5)
        self.tableView = QtGui.QTableView(self.widget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_3.addWidget(self.tableView)
        self.horizontalLayout.addWidget(self.widget_2)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Form)
        self.report_w.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.exm_btn.setText(QtGui.QApplication.translate("Form", "الاختبارات", None, QtGui.QApplication.UnicodeUTF8))
        self.gp_btn.setText(QtGui.QApplication.translate("Form", "المجموعات", None, QtGui.QApplication.UnicodeUTF8))
        self.all_btn.setText(QtGui.QApplication.translate("Form", "الكل", None, QtGui.QApplication.UnicodeUTF8))

import source_rc
