# -*- coding: utf-8 -*-
from login import Login
from main_window import Main_code
from PySide.QtGui import *
from model.Model import Model
import threading
class First_step():
    def __init__(self):
        self.login = Login()
        self.login.showMaximized()
        self.db = Model()
        self.db2 = Model()
        self.centerx(self.login)
        self.login.login_btn.clicked.connect(self.log_in)
        self.login.pass_lbl.returnPressed.connect(self.log_in)
        self.main_code = Main_code()
        self.main_code.logout_btn_5.clicked.connect(self.log_out)
        db1 = Model()
        db1.th_course()
        db2 = Model()
        db2.th_exam()
    def log_out(self):
        self.login.user_lbl.clear()
        self.login.pass_lbl.clear()
        self.main_code.hide()
        self.login.show()
    def log_in(self):
        x = self.login.log_in()
        if x[0]:
            self.login.hide()
            self.db.set_id(x[2][0])
            self.main_code.set_info(x[2])
            self.centerx(self.main_code)
            self.show_all()
            if x[1] != 'A':
                self.set_permissions(Model.ID)
            self.main_code.showMaximized()
        else:
            self.login.wrong_pass.show()
            self.login.pass_lbl.selectAll()
    def show_all(self):
        for i in self.main_code.findChildren(QToolButton):
            i.setVisible(True)
        self.main_code.h.clear()
    def centerx(self,x):
        frameGm = x.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        x.move(frameGm.topLeft())
    def set_permissions(self,uid):
        access = self.db.get_users_access(uid)
        print access
        for i in self.main_code.findChildren(QToolButton):

            if i.text() in access:
                i.setVisible(True)
            else:
                i.setVisible(False)