# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uis/students_add.ui'
#
# Created: Tue Jul 17 12:09:18 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(873, 409)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_5 = QtGui.QWidget(Form)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget_5)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_6 = QtGui.QWidget(self.widget_5)
        self.widget_6.setObjectName("widget_6")
        self.gridLayout_10 = QtGui.QGridLayout(self.widget_6)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.add_btn = QtGui.QPushButton(self.widget_6)
        font = QtGui.QFont()
        font.setFamily("Alarabiya Font")
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.add_btn.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/n/img/Plus-500.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_btn.setIcon(icon)
        self.add_btn.setIconSize(QtCore.QSize(25, 25))
        self.add_btn.setFlat(True)
        self.add_btn.setObjectName("add_btn")
        self.gridLayout_10.addWidget(self.add_btn, 2, 3, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem, 1, 4, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem1, 1, 0, 1, 1)
        self.print_btn = QtGui.QPushButton(self.widget_6)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/n/img/Printer Door Open Filled-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.print_btn.setIcon(icon1)
        self.print_btn.setIconSize(QtCore.QSize(25, 25))
        self.print_btn.setFlat(True)
        self.print_btn.setObjectName("print_btn")
        self.gridLayout_10.addWidget(self.print_btn, 2, 1, 1, 1)
        self.search_edt = QtGui.QLineEdit(self.widget_6)
        font = QtGui.QFont()
        font.setFamily("Alarabiya Font")
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.search_edt.setFont(font)
        self.search_edt.setAlignment(QtCore.Qt.AlignCenter)
        self.search_edt.setObjectName("search_edt")
        self.gridLayout_10.addWidget(self.search_edt, 1, 1, 1, 3)
        self.print_student_info = QtGui.QPushButton(self.widget_6)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/n/img/Conference Call Filled-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.print_student_info.setIcon(icon2)
        self.print_student_info.setIconSize(QtCore.QSize(30, 30))
        self.print_student_info.setFlat(True)
        self.print_student_info.setObjectName("print_student_info")
        self.gridLayout_10.addWidget(self.print_student_info, 2, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.widget_6)
        self.all_students = QtGui.QTableView(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("Alarabiya Font")
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.all_students.setFont(font)
        self.all_students.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.all_students.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.all_students.setObjectName("all_students")
        self.verticalLayout_2.addWidget(self.all_students)
        self.verticalLayout.addWidget(self.widget_5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.add_btn.setText(QtGui.QApplication.translate("Form", "اضافة طالب", None, QtGui.QApplication.UnicodeUTF8))
        self.print_btn.setText(QtGui.QApplication.translate("Form", "طباعة الباركود", None, QtGui.QApplication.UnicodeUTF8))
        self.search_edt.setPlaceholderText(QtGui.QApplication.translate("Form", "بحث بالاسم - الرقم", None, QtGui.QApplication.UnicodeUTF8))
        self.print_student_info.setText(QtGui.QApplication.translate("Form", "طباعه بيانات الطلاب", None, QtGui.QApplication.UnicodeUTF8))

import source_rc
