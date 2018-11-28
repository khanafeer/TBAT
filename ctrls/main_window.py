# -*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
from views.main import Ui_MainWindow as main_w
from model.Model import Model
#start of controllers import
from course import course
from exam import exam
from gp_report import repo
from permissions import permissions
from report import report
from st_report import st_report
from student import student
from student_enter import student_enter
from report_all import Report_all

class Main_code(QMainWindow, main_w):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.db = Model()
        self.tabes_data = {u'حضور الطلاب':student_enter(),u'الطالب':student(),u'المجموعات':course(),u'الاختبارات':exam(),u'تقرير المجموعات':Report_all(),u'تقرير الطالب':st_report(),u'تقرير الماليه':report(),u'المستخدمين':permissions()}
        for i in self.findChildren(QWidget):
            i.setAttribute(Qt.WA_StyledBackground, True)
        for i in self.widget_3.findChildren(QToolButton):
            i.clicked.connect(self.pr_lst)
        self.h.tabCloseRequested.connect(self.removeTab)
        self.h.currentChanged.connect(self.tab_select)
    def tab_select(self,indx):
        self.h.currentWidget().setFocus()
    def removeTab(self, index):
        self.h.removeTab(index)

    def set_info(self,user_data):
        self.user_name_5.setText(user_data[1])
        if user_data[4] == 'A':self.user_type_5.setText(u'مدير النظام')
        else:self.user_type_5.setText(u'مستخدم')
        self.close_btn_5.clicked.connect(self.close)
    def closeEvent(self, event):
        msgBox = QMessageBox()
        msgBox.setFixedSize(150, 100)
        msgBox.setWindowTitle(u'تحذير')
        msgBox.setText(u'سيتم اغلاق البرنامج هل انت موافق')
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        if msgBox.exec_() == msgBox.Ok:
            QCoreApplication.quit()
        else:
            event.ignore()
    def pr_lst(self):
        x = self.sender().text()
        self.open_show(self.tabes_data[x],x)
    def open_show(self,w,txt):
        t = self.h.count()
        tbs = []
        for i in range(t):
            tbs.append(self.h.tabText(i))
        if txt in tbs:
            self.h.setCurrentIndex(tbs.index(txt))
        else:
            self.h.addTab(w, txt)
            self.h.setCurrentIndex(len(tbs))
        self.h.currentWidget().setFocus()
    def ex(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(u"تاكيد")
        msg.setInformativeText(u"هل انت متاكد من الخروج")
        msg.setWindowTitle("Alert")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.button(QMessageBox.Ok).triggered.connect(self.ex_f)
        msg.exec_()
    def ex_f(self):
        self.close()
    def showdialog(self, x, y):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(x)
        msg.setInformativeText(y)
        msg.setWindowTitle("Alert")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        return msg.exec_()
