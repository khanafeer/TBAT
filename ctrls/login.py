# -*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
from views.login import Ui_Form as login
from model.Model import Model
class Login(QWidget, login):
    img_num = 1
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.db = Model()
        self.wrong_name.hide()
        self.wrong_pass.hide()
        self.login_w.setAttribute(Qt.WA_StyledBackground, True)
        self.exit_btn.clicked.connect(self.ex_f)
        self.user_lbl.returnPressed.connect(self.search_name)
        self.login_w.setContentsMargins(25,25,25,25)
        self.set_bg_image()
    def ex_f(self):
        self.close()
    def inform_msg(self,msg):
        self.inform_lbl.show()
        self.inform_lbl.setText(msg)
    def set_bg_image(self):
        screen_resolution = QApplication.desktop().screenGeometry()
        width, height = screen_resolution.width(), screen_resolution.height()
        try:
            img = "bg.jpg"
            palette = QPalette()
            palette.setBrush(QPalette.Background,
                             QBrush(QPixmap(img).scaled(QSize(width, height), Qt.KeepAspectRatioByExpanding)))
            self.setPalette(palette)
        except:
            pass
    def log_out_timerF(self):
        time = QTime.currentTime().secsTo(self.end)
        try:
            if time > 301 and time < 240 :
                self.showdialog(u'قاربت مدتك على الانتهاء',u'سيتم اغلاق البرنامج بعد 5 دقائق')
            if time > 59 and  time < 120:
                self.showdialog(u'لقد انتهت الوردية', u'سيتم اغلاق البرنامج بعد 1 دقيقة')
            if time < 0:
                QCoreApplication.quit()
        finally:
            QTimer.singleShot(60000, self.log_out_timerF)
    def check_permission(self,uid):
        times = self.db.get_user_time(uid)
        if times:
            t1 = QTime.fromString(unicode(times[1]), u"hh:mm:ss")
            t2 = QTime.fromString(unicode(times[2]), u"hh:mm:ss")
            now = QTime.currentTime()
            if times[3] == 1 and now >= t1 and now < t2:
                self.end = t2
                self.log_out_timerF()
                return True
            elif times[3] == 0:
                return True
            else:
                return False
        else:
            return False
    def closeEvent(self, event):
        msgBox = QMessageBox()
        msgBox.setFixedSize(150, 100)
        msgBox.setWindowTitle(u'تحذير')
        msgBox.setText(u'سيتم اغلاق البرنامج هل انت موافق')
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        if msgBox.exec_() == msgBox.Ok:
            self.db.del_all_temp()
            QCoreApplication.quit()
        else:
            event.ignore()
    def get_user_name(self):
        id = Model.ID
        x = self.db.get_user_name(id)
        if x:
            if x[1] == 'A':
                self.user_type.setText(u'مدير النظام')
            else:
                self.user_type.setText(u'مستخدم عادى')
            self.user_name.setText(unicode(x[0]))
    def ex(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(u"تاكيد")
        msg.setInformativeText(u"هل انت متاكد من الخروج")
        msg.setWindowTitle("Alert")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.button(QMessageBox.Ok).clicked.connect(self.ex_f)
        msg.exec_()
    def ex_f(self):
        self.close()
    def search_name(self):
        name = self.user_lbl.text()
        c = self.db.check_user_name(name)
        if c:
            self.pass_lbl.setEnabled(True)
            self.pass_lbl.setFocus()
            self.wrong_name.setHidden(True)
        else:
            self.wrong_pass.setHidden(True)
            self.wrong_name.setHidden(False)
            self.user_lbl.selectAll()
    def log_in(self):
        "Authentication Function"
        name = self.user_lbl.text()
        password = self.pass_lbl.text()
        c = self.db.check_name_pass(name,password)
        if c:
            if c[4] == "U":
                if self.check_permission(c[0]):
                    return [True, 'U', c]
                else:
                    return [False, '', 0]
            elif c[4] == "A":
                return [True, 'A',c]
            else:
                return [False, '',c]
        else:
            return [False, '',0]
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