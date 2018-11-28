# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uis/main.ui'
#
# Created: Wed Jun 20 18:14:21 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(681, 653)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/n/img/home.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(".QWidget{\n"
"\n"
"background:#A8B1B2;\n"
"}\n"
".QListWidget{\n"
"background-color: #000;\n"
"color:white;\n"
"\n"
"\n"
"}\n"
".QListWidget::item:selected {\n"
"background:#A8B1B2\n"
"\n"
"}\n"
"\n"
".QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 0px solid #b1b1b1;\n"
"    border-radius: 1px;\n"
"}\n"
"\n"
".QRadioButton::indicator:checked\n"
"{\n"
"    background-color: qradialgradient(\n"
"        cx: 0.5, cy: 0.5,\n"
"        fx: 0.5, fy: 0.5,\n"
"        radius: 1.0,\n"
"        stop: 0.25 #00838F,\n"
"        stop: 0.3 #323232\n"
"    );\n"
"}\n"
"\n"
"\n"
"\n"
".QPushButton {\n"
"        color: rgb(0, 0, 0);\n"
"    font: 16px Helvetica, Arial, sans-serif;\n"
"    background-color: transparent;\n"
"    border-width: 0px;\n"
"    border-style: solid;\n"
"}\n"
"\n"
"\n"
".QLineEdit { \n"
"    color: rgb(0, 0, 0);\n"
"    font: 17px Helvetica, Arial, sans-serif;\n"
"    border: 1px solid #c4c4c4; \n"
"    padding: 6px 6px 6px 6px; \n"
"} \n"
" \n"
".QLineEdit:focus { \n"
"    outline: none; \n"
"    border: 1px solid #7bc1f7; \n"
"   }\n"
".QLineEdit:hover{\n"
"\n"
"    border: 1px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
".QTableWidget::hover{\n"
"\n"
"    border: 1px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"\n"
"}\n"
" .QTabBar::tab {\n"
"       background-color: #000;\n"
"    color:white;\n"
"     border: 0px;\n"
"     min-width: 28ex;\n"
"    min-height:9ex;\n"
"padding:8px;\n"
" }\n"
" \n"
" .QTabBar::tab:selected, QTabBar::tab:hover {\n"
"           background-color: #fff;\n"
"    color:#000;\n"
"     border: 0px;\n"
"     min-width: 25ex;\n"
"    min-height:9ex;\n"
"padding:8px;\n"
" }\n"
" \n"
".QTabBar::tab:selected {\n"
"              background-color: #fff;\n"
"    color:#000;\n"
"        border: 0px;\n"
"     min-width: 25ex;\n"
"    min-height:9ex;\n"
"padding:8px;\n"
" }\n"
"")
        MainWindow.setDocumentMode(False)
        MainWindow.setDockOptions(QtGui.QMainWindow.AllowTabbedDocks|QtGui.QMainWindow.AnimatedDocks)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.central_w = QtGui.QWidget(MainWindow)
        self.central_w.setObjectName("central_w")
        self.gridLayout = QtGui.QGridLayout(self.central_w)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtGui.QWidget(self.central_w)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtGui.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget_2 = QtGui.QWidget(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(12)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.widget_2.setFont(font)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_4 = QtGui.QGridLayout(self.widget_2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setVerticalSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.h = QtGui.QTabWidget(self.widget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.h.sizePolicy().hasHeightForWidth())
        self.h.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.h.setFont(font)
        self.h.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.h.setTabShape(QtGui.QTabWidget.Rounded)
        self.h.setElideMode(QtCore.Qt.ElideRight)
        self.h.setUsesScrollButtons(False)
        self.h.setDocumentMode(True)
        self.h.setTabsClosable(True)
        self.h.setMovable(True)
        self.h.setObjectName("h")
        self.gridLayout_4.addWidget(self.h, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.widget_2, 2, 0, 1, 1)
        self.widget_3 = QtGui.QWidget(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.widget_3.setStyleSheet(".QWidget{\n"
"background:#000;}")
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout = QtGui.QVBoxLayout(self.widget_3)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(2, 0, 2, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.toolButton = QtGui.QToolButton(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton.sizePolicy().hasHeightForWidth())
        self.toolButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.toolButton.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/n/img/report.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon1)
        self.toolButton.setIconSize(QtCore.QSize(50, 50))
        self.toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton.setObjectName("toolButton")
        self.verticalLayout.addWidget(self.toolButton)
        self.toolButton_2 = QtGui.QToolButton(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_2.sizePolicy().hasHeightForWidth())
        self.toolButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.toolButton_2.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/n/img/student.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon2)
        self.toolButton_2.setIconSize(QtCore.QSize(50, 50))
        self.toolButton_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_2.setObjectName("toolButton_2")
        self.verticalLayout.addWidget(self.toolButton_2)
        self.toolButton_3 = QtGui.QToolButton(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_3.sizePolicy().hasHeightForWidth())
        self.toolButton_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.toolButton_3.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/n/img/collaboration.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_3.setIcon(icon3)
        self.toolButton_3.setIconSize(QtCore.QSize(50, 50))
        self.toolButton_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_3.setObjectName("toolButton_3")
        self.verticalLayout.addWidget(self.toolButton_3)
        self.toolButton_4 = QtGui.QToolButton(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_4.sizePolicy().hasHeightForWidth())
        self.toolButton_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.toolButton_4.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/n/img/board.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_4.setIcon(icon4)
        self.toolButton_4.setIconSize(QtCore.QSize(50, 50))
        self.toolButton_4.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_4.setObjectName("toolButton_4")
        self.verticalLayout.addWidget(self.toolButton_4)
        self.toolButton_6 = QtGui.QToolButton(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_6.sizePolicy().hasHeightForWidth())
        self.toolButton_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.toolButton_6.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/n/img/line-chart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_6.setIcon(icon5)
        self.toolButton_6.setIconSize(QtCore.QSize(50, 50))
        self.toolButton_6.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_6.setObjectName("toolButton_6")
        self.verticalLayout.addWidget(self.toolButton_6)
        self.toolButton_7 = QtGui.QToolButton(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_7.sizePolicy().hasHeightForWidth())
        self.toolButton_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.toolButton_7.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/n/img/analytics (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_7.setIcon(icon6)
        self.toolButton_7.setIconSize(QtCore.QSize(50, 50))
        self.toolButton_7.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_7.setObjectName("toolButton_7")
        self.verticalLayout.addWidget(self.toolButton_7)
        self.toolButton_5 = QtGui.QToolButton(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_5.sizePolicy().hasHeightForWidth())
        self.toolButton_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.toolButton_5.setFont(font)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/n/img/money-bag-with-dollar-symbol.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_5.setIcon(icon7)
        self.toolButton_5.setIconSize(QtCore.QSize(50, 50))
        self.toolButton_5.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_5.setObjectName("toolButton_5")
        self.verticalLayout.addWidget(self.toolButton_5)
        self.toolButton_8 = QtGui.QToolButton(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_8.sizePolicy().hasHeightForWidth())
        self.toolButton_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.toolButton_8.setFont(font)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/n/img/clerk-with-tie (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_8.setIcon(icon8)
        self.toolButton_8.setIconSize(QtCore.QSize(50, 50))
        self.toolButton_8.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_8.setObjectName("toolButton_8")
        self.verticalLayout.addWidget(self.toolButton_8)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout_2.addWidget(self.widget_3, 0, 1, 3, 1)
        self.header = QtGui.QWidget(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy)
        self.header.setMaximumSize(QtCore.QSize(16777215, 50))
        self.header.setStyleSheet("")
        self.header.setObjectName("header")
        self.horizontalLayout_11 = QtGui.QHBoxLayout(self.header)
        self.horizontalLayout_11.setSpacing(10)
        self.horizontalLayout_11.setContentsMargins(5, 5, 10, 5)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.close_btn_5 = QtGui.QPushButton(self.header)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.close_btn_5.sizePolicy().hasHeightForWidth())
        self.close_btn_5.setSizePolicy(sizePolicy)
        self.close_btn_5.setMaximumSize(QtCore.QSize(555555, 55555))
        self.close_btn_5.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/n/img/Cancel-500.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_btn_5.setIcon(icon9)
        self.close_btn_5.setIconSize(QtCore.QSize(30, 30))
        self.close_btn_5.setFlat(True)
        self.close_btn_5.setObjectName("close_btn_5")
        self.horizontalLayout_11.addWidget(self.close_btn_5)
        self.logout_btn_5 = QtGui.QPushButton(self.header)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logout_btn_5.sizePolicy().hasHeightForWidth())
        self.logout_btn_5.setSizePolicy(sizePolicy)
        self.logout_btn_5.setMaximumSize(QtCore.QSize(555555, 55555))
        self.logout_btn_5.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/n/img/Logout Rounded Left Filled-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logout_btn_5.setIcon(icon10)
        self.logout_btn_5.setIconSize(QtCore.QSize(30, 30))
        self.logout_btn_5.setFlat(True)
        self.logout_btn_5.setObjectName("logout_btn_5")
        self.horizontalLayout_11.addWidget(self.logout_btn_5)
        self.user_type_5 = QtGui.QLabel(self.header)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.user_type_5.sizePolicy().hasHeightForWidth())
        self.user_type_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.user_type_5.setFont(font)
        self.user_type_5.setAlignment(QtCore.Qt.AlignCenter)
        self.user_type_5.setObjectName("user_type_5")
        self.horizontalLayout_11.addWidget(self.user_type_5)
        self.user_name_5 = QtGui.QLabel(self.header)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.user_name_5.sizePolicy().hasHeightForWidth())
        self.user_name_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.user_name_5.setFont(font)
        self.user_name_5.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.user_name_5.setAlignment(QtCore.Qt.AlignCenter)
        self.user_name_5.setObjectName("user_name_5")
        self.horizontalLayout_11.addWidget(self.user_name_5)
        self.notify_show_btn_5 = QtGui.QPushButton(self.header)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.notify_show_btn_5.sizePolicy().hasHeightForWidth())
        self.notify_show_btn_5.setSizePolicy(sizePolicy)
        self.notify_show_btn_5.setMinimumSize(QtCore.QSize(35, 30))
        self.notify_show_btn_5.setStyleSheet("QPushButton\n"
"{\n"
"border:0px;\n"
"border-radius:15px;\n"
"background:#fff;\n"
"color:#000;\n"
"}")
        self.notify_show_btn_5.setFlat(False)
        self.notify_show_btn_5.setObjectName("notify_show_btn_5")
        self.horizontalLayout_11.addWidget(self.notify_show_btn_5)
        self.gridLayout_2.addWidget(self.header, 0, 0, 1, 1)
        self.line = QtGui.QFrame(self.widget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.central_w)

        self.retranslateUi(MainWindow)
        self.h.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "TBAT", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton.setText(QtGui.QApplication.translate("MainWindow", "حضور الطلاب", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_2.setText(QtGui.QApplication.translate("MainWindow", "الطالب", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_3.setText(QtGui.QApplication.translate("MainWindow", "المجموعات", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_4.setText(QtGui.QApplication.translate("MainWindow", "الاختبارات", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_6.setText(QtGui.QApplication.translate("MainWindow", "تقرير المجموعات", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_7.setText(QtGui.QApplication.translate("MainWindow", "تقرير الطالب", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_5.setText(QtGui.QApplication.translate("MainWindow", "تقرير الماليه", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_8.setText(QtGui.QApplication.translate("MainWindow", "المستخدمين", None, QtGui.QApplication.UnicodeUTF8))
        self.user_type_5.setText(QtGui.QApplication.translate("MainWindow", "نوع المستخدم", None, QtGui.QApplication.UnicodeUTF8))
        self.user_name_5.setText(QtGui.QApplication.translate("MainWindow", "اسم المستخدم", None, QtGui.QApplication.UnicodeUTF8))
        self.notify_show_btn_5.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))

import source_rc
import source_rc
