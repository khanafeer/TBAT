# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uis/course_dw.ui'
#
# Created: Sun Jun 24 17:21:35 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(390, 465)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_3 = QtGui.QWidget(Form)
        self.widget_3.setStyleSheet(".QWidget { background: #44D9E6; }")
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_2 = QtGui.QGridLayout(self.widget_3)
        self.gridLayout_2.setContentsMargins(9, -1, -1, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget_4 = QtGui.QWidget(self.widget_3)
        self.widget_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.class_rd = QtGui.QRadioButton(self.widget_4)
        self.class_rd.setObjectName("class_rd")
        self.horizontalLayout_3.addWidget(self.class_rd)
        self.month_rd = QtGui.QRadioButton(self.widget_4)
        self.month_rd.setChecked(True)
        self.month_rd.setObjectName("month_rd")
        self.horizontalLayout_3.addWidget(self.month_rd)
        self.course_rd = QtGui.QRadioButton(self.widget_4)
        self.course_rd.setObjectName("course_rd")
        self.horizontalLayout_3.addWidget(self.course_rd)
        self.gridLayout_2.addWidget(self.widget_4, 4, 0, 1, 1)
        self.widget = QtGui.QWidget(self.widget_3)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.del_btn = QtGui.QPushButton(self.widget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/n/img/Delete-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.del_btn.setIcon(icon)
        self.del_btn.setIconSize(QtCore.QSize(30, 30))
        self.del_btn.setObjectName("del_btn")
        self.horizontalLayout.addWidget(self.del_btn)
        self.edite_btn = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edite_btn.sizePolicy().hasHeightForWidth())
        self.edite_btn.setSizePolicy(sizePolicy)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/n/img/edit-document.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edite_btn.setIcon(icon1)
        self.edite_btn.setIconSize(QtCore.QSize(30, 30))
        self.edite_btn.setObjectName("edite_btn")
        self.horizontalLayout.addWidget(self.edite_btn)
        self.details_btn = QtGui.QPushButton(self.widget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/n/img/Settings-500.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.details_btn.setIcon(icon2)
        self.details_btn.setIconSize(QtCore.QSize(30, 30))
        self.details_btn.setObjectName("details_btn")
        self.horizontalLayout.addWidget(self.details_btn)
        self.add_btn = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_btn.sizePolicy().hasHeightForWidth())
        self.add_btn.setSizePolicy(sizePolicy)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/n/img/Plus-500.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_btn.setIcon(icon3)
        self.add_btn.setIconSize(QtCore.QSize(30, 30))
        self.add_btn.setObjectName("add_btn")
        self.horizontalLayout.addWidget(self.add_btn)
        self.gridLayout_2.addWidget(self.widget, 14, 0, 1, 2)
        self.widget_2 = QtGui.QWidget(self.widget_3)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.nm_lbl = QtGui.QLabel(self.widget_2)
        self.nm_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.nm_lbl.setObjectName("nm_lbl")
        self.horizontalLayout_2.addWidget(self.nm_lbl)
        self.gridLayout_2.addWidget(self.widget_2, 0, 0, 1, 2)
        self.price_spn = QtGui.QDoubleSpinBox(self.widget_3)
        self.price_spn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.price_spn.setAlignment(QtCore.Qt.AlignCenter)
        self.price_spn.setObjectName("price_spn")
        self.gridLayout_2.addWidget(self.price_spn, 5, 0, 1, 1)
        self.nm_edt = QtGui.QLineEdit(self.widget_3)
        self.nm_edt.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.nm_edt.setAlignment(QtCore.Qt.AlignCenter)
        self.nm_edt.setObjectName("nm_edt")
        self.gridLayout_2.addWidget(self.nm_edt, 1, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.widget_3)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 4, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.widget_3)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 9, 1, 1, 1)
        self.absence = QtGui.QSpinBox(self.widget_3)
        self.absence.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.absence.setAlignment(QtCore.Qt.AlignCenter)
        self.absence.setObjectName("absence")
        self.gridLayout_2.addWidget(self.absence, 8, 0, 1, 1)
        self.day_spn = QtGui.QSpinBox(self.widget_3)
        self.day_spn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.day_spn.setAlignment(QtCore.Qt.AlignCenter)
        self.day_spn.setObjectName("day_spn")
        self.gridLayout_2.addWidget(self.day_spn, 2, 0, 1, 1)
        self.allow = QtGui.QDoubleSpinBox(self.widget_3)
        self.allow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.allow.setAlignment(QtCore.Qt.AlignCenter)
        self.allow.setObjectName("allow")
        self.gridLayout_2.addWidget(self.allow, 9, 0, 1, 1)
        self.allow_before = QtGui.QDoubleSpinBox(self.widget_3)
        self.allow_before.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.allow_before.setAlignment(QtCore.Qt.AlignCenter)
        self.allow_before.setObjectName("allow_before")
        self.gridLayout_2.addWidget(self.allow_before, 10, 0, 2, 1)
        self.label_9 = QtGui.QLabel(self.widget_3)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 10, 1, 1, 1)
        self.inst_edt = QtGui.QLineEdit(self.widget_3)
        self.inst_edt.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.inst_edt.setAlignment(QtCore.Qt.AlignCenter)
        self.inst_edt.setObjectName("inst_edt")
        self.gridLayout_2.addWidget(self.inst_edt, 6, 0, 1, 1)
        self.label_10 = QtGui.QLabel(self.widget_3)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 11, 1, 1, 1)
        self.details_edt = QtGui.QTextEdit(self.widget_3)
        self.details_edt.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.details_edt.setObjectName("details_edt")
        self.gridLayout_2.addWidget(self.details_edt, 12, 0, 1, 1)
        self.label_11 = QtGui.QLabel(self.widget_3)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 12, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.widget_3)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 5, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.widget_3)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 6, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.widget_3)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 3, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.widget_3)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 8, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.widget_3)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 1, 1, 1)
        self.label = QtGui.QLabel(self.widget_3)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 1, 1, 1)
        self.hours_spn = QtGui.QDoubleSpinBox(self.widget_3)
        self.hours_spn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.hours_spn.setAlignment(QtCore.Qt.AlignCenter)
        self.hours_spn.setObjectName("hours_spn")
        self.gridLayout_2.addWidget(self.hours_spn, 3, 0, 1, 1)
        self.verticalLayout.addWidget(self.widget_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.nm_edt, self.day_spn)
        Form.setTabOrder(self.day_spn, self.hours_spn)
        Form.setTabOrder(self.hours_spn, self.price_spn)
        Form.setTabOrder(self.price_spn, self.inst_edt)
        Form.setTabOrder(self.inst_edt, self.add_btn)
        Form.setTabOrder(self.add_btn, self.edite_btn)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.class_rd.setText(QtGui.QApplication.translate("Form", "بالحصة", None, QtGui.QApplication.UnicodeUTF8))
        self.month_rd.setText(QtGui.QApplication.translate("Form", "بالشهر", None, QtGui.QApplication.UnicodeUTF8))
        self.course_rd.setText(QtGui.QApplication.translate("Form", "بالكورس", None, QtGui.QApplication.UnicodeUTF8))
        self.del_btn.setText(QtGui.QApplication.translate("Form", "حذف", None, QtGui.QApplication.UnicodeUTF8))
        self.edite_btn.setText(QtGui.QApplication.translate("Form", "تعديل", None, QtGui.QApplication.UnicodeUTF8))
        self.details_btn.setText(QtGui.QApplication.translate("Form", "تفاصيل", None, QtGui.QApplication.UnicodeUTF8))
        self.add_btn.setText(QtGui.QApplication.translate("Form", "اضافة", None, QtGui.QApplication.UnicodeUTF8))
        self.nm_lbl.setText(QtGui.QApplication.translate("Form", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Form", "نظام الدفع", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Form", "الوقت السماح ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Form", "الوقت الدخول ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Form", "قبل الدرس", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("Form", "تفاصيل", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "السعر", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "المحاضر", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "عدد الساعات", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Form", "عدد مرات الغياب ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "عدد الايام", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "الاسم", None, QtGui.QApplication.UnicodeUTF8))

import source_rc
