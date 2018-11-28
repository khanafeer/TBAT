# -*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
from model.Model import Model
import datetime
from printing import print_doc
from views.st_report import Ui_Form as st_report
from views.info_dw import Ui_Form as info_dw
class info_dw(QWidget, info_dw):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
class st_report(QWidget, st_report):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        for i in self.findChildren(QWidget):
            i.setAttribute(Qt.WA_StyledBackground, True)
        self.db = Model()
        self.pr = print_doc()
        self.show_info = info_dw()
        self.completer_set()
        self.centerx(self.show_info)
        self.search_btn.clicked.connect(self.get_groups)
        self.st_search_edt.returnPressed.connect(self.get_groups)
        self.gp_name.currentIndexChanged.connect(self.search_func)
        self.st_dt.setDateTime(datetime.datetime.now())
        self.end_dt.setDateTime(datetime.datetime.now())
        self.report_table.cellClicked.connect(self.show_info_f)
        self.print_btn.clicked.connect(self.print_report)
    def show_info_f(self, row, column):
        if column == 2:
            self.show_info.show()
            self.show_info.activateWindow()
            self.show_info.raise_()
    def centerx(self, x):
        frameGm = x.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        x.move(frameGm.topLeft())
    def get_groups(self):
        if self.st_search_edt.text():
            info = self.db.get_student(self.st_search_edt.text())
            if info:
                self.bc_label.setText(info[0])
                self.name_lbl.setText(info[1])
                self.school_lbl.setText(info[2])
                self.ph_lbl.setText(info[3])
                self.fph_lbl.setText(info[4])
                self.mail_lbl.setText(info[5])
                self.add_lbl.setText(info[6])
                self.details_lbl.setText(info[7])
                #fill student groups
                cs = self.db.get_groups_st(info[0])
                self.gp_name.clear()
                self.gp_name.addItems(cs)
            else:
                self.dialoge_only(u'لا توجد بيانات لهذا المتدرب', u'ادخل الاسم الصحيح')
        else:
            self.dialoge_only(u'لا يوجد طالب',u'اختر طالب اولا')
    def search_func(self):
        d1 = self.st_dt.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        d2 = self.end_dt.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        self.report_table.setRowCount(0)
        self.report_table.insertRow(0)
        self.report_table.setItem(0, 0, QTableWidgetItem(u'غياب المجموعات'))
        self.report_table.setItem(0, 1, QTableWidgetItem(self.db.get_st_rep_att(d1, d2,self.gp_name.currentText(),self.bc_label.text())))
        self.report_table.setItem(0, 2, QTableWidgetItem(u'اظهار التفاصيل'))
        # second Row
        self.report_table.insertRow(1)
        self.report_table.setItem(1, 0, QTableWidgetItem(u'غياب الاختبارات'))
        self.report_table.setItem(1, 1, QTableWidgetItem(self.db.get_st_rep_ex(d1, d2,self.gp_name.currentText(),self.bc_label.text())))
        self.report_table.setItem(1, 2, QTableWidgetItem(u'اظهار التفاصيل'))
        # third Row
        self.report_table.insertRow(2)
        self.report_table.setItem(2, 0, QTableWidgetItem(u'درجات الاختبارات'))
        self.report_table.setItem(2, 1, QTableWidgetItem(self.db.get_st_rep_ex_deg(d1, d2,self.gp_name.currentText(),self.bc_label.text())))
        self.report_table.setItem(2, 2, QTableWidgetItem(u'اظهار التفاصيل'))
        # fourth Row
        self.report_table.insertRow(3)
        self.report_table.setItem(3, 0, QTableWidgetItem(u'المعاملات المالية'))
        self.report_table.setItem(3, 1, QTableWidgetItem(self.db.get_st_rep_mony(d1, d2,self.gp_name.currentText(),self.bc_label.text())))
        self.report_table.setItem(3, 2, QTableWidgetItem(u'اظهار التفاصيل'))
        self.report_table.item(0, 2).setBackground(QColor(20, 200, 10))
        self.report_table.item(1, 2).setBackground(QColor(20, 200, 10))
        self.report_table.item(2, 2).setBackground(QColor(20, 200, 10))
        self.report_table.item(3, 2).setBackground(QColor(20, 200, 10))
        self.report_table.resizeColumnsToContents()
        value = float(self.db.get_st_rep_att(d1, d2,self.gp_name.currentText(),self.bc_label.text()).split("/")[0]) + float(self.db.get_st_rep_ex(d1, d2,self.gp_name.currentText(),self.bc_label.text()).split("/")[0]) +float(self.db.get_st_rep_ex_deg(d1, d2,self.gp_name.currentText(),self.bc_label.text()).split("/")[0])
        max_v = float(self.db.get_st_rep_att(d1, d2,self.gp_name.currentText(),self.bc_label.text()).split("/")[1]) + float(self.db.get_st_rep_ex(d1, d2,self.gp_name.currentText(),self.bc_label.text()).split("/")[1]) +float(self.db.get_st_rep_ex_deg(d1, d2,self.gp_name.currentText(),self.bc_label.text()).split("/")[1])
        try:
            x = (value / max_v) * 100
        except:
            x =0
        self.ratio_lbl.setText(str("%.2f" % x) + " %")
    def dialoge_only(self, x, y):
        msgBox = QMessageBox()
        msgBox.setFixedSize(150, 100)
        msgBox.setWindowTitle(u'تحذير')
        msgBox.setText(unicode(x))
        msgBox.setInformativeText(y)
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        return msgBox.exec_()
    def completer_set(self):
        completer = QCompleter()
        completer.setCompletionMode(QCompleter.PopupCompletion)
        completer.activated.connect(self.get_groups)
        model = QStringListModel()
        completer.setModel(model)
        self.db.get_students(model)
        self.st_search_edt.setCompleter(completer)
    def print_report(self):
        if self.report_table.rowCount():
            d1 = self.st_dt.dateTime().toString("yyyy-MM-dd hh:mm:ss")
            d2 = self.end_dt.dateTime().toString("yyyy-MM-dd hh:mm:ss")
            self.pr.print_st_report(self.get_data(),d1,d2,self.bc_label.text(),self.name_lbl.text(),\
                                    self.school_lbl.text(),self.add_lbl.text(),self.ph_lbl.text(),\
                                    self.fph_lbl.text(),self.mail_lbl.text(),self.details_lbl.text(),self.ratio_lbl.text())
        else:
            self.dialoge_only(u'لا توجد بيانات للطالب فى هذة المجموعة',u'اختر المجموعة الصحيحة والمعاد الحقيقى')
    def get_data(self):
        s = []
        a = []
        n = self.report_table.columnCount()
        for i in range(n-1):
            s.append(self.report_table.horizontalHeaderItem(i).text())
        a.append(s)
        x = self.report_table.rowCount()
        for i in range(x):
            s = []
            for j in range(n-1):
                s.append(self.report_table.item(i,j).text())
            a.append(s)
        return a