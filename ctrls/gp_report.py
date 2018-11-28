from PySide.QtGui import *
from PySide.QtCore import *
from model.Model import Model
import datetime
import sys
from views.gp_report import Ui_Form as repo
class repo(QWidget, repo):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        for i in self.findChildren(QWidget):
            i.setAttribute(Qt.WA_StyledBackground, True)
        self.db = Model()
        self.st_dt.setDateTime(datetime.datetime.now())
        self.end_dt.setDateTime(datetime.datetime.now())
        self.groups()
        self.search_fun()
        self.course_cmb.currentIndexChanged.connect(self.search_fun)
        self.search_btn.clicked.connect(self.search_fun)

    def groups(self):
        out = self.db.get_groups()
        self.course_cmb.clear()
        self.course_cmb.addItems(out)

    def search_fun(self):
        gp = self.course_cmb.currentText()
        date_s = self.st_dt.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        date_d = self.end_dt.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        students = self.db.get_all_stu(gp)
        self.all_items.setRowCount(0)
        for i in students :
            n = self.all_items.rowCount()
            self.all_items.insertRow(n)
            self.all_items.setItem(n, 0, QTableWidgetItem(i[0]))
            name = self.db.get_name(i[0])
            self.all_items.setItem(n, 1, QTableWidgetItem(name[0]))
            att = self.db.get_st_rep_att(date_s,date_d,gp,i[0])
            self.all_items.setItem(n, 2, QTableWidgetItem(att))
            att_ex = self.db.get_st_rep_ex(date_s,date_d,gp,i[0])
            self.all_items.setItem(n, 3, QTableWidgetItem(att_ex))
            degree = self.db.get_st_rep_ex_deg(date_s,date_d,gp,i[0])
            self.all_items.setItem(n, 4, QTableWidgetItem(degree))
            mony = self.db.get_st_rep_mony(date_s,date_d,gp,i[0])
            self.all_items.setItem(n, 5, QTableWidgetItem(mony))
            value = float(
                self.db.get_st_rep_att(date_s,date_d,gp, i[0]).split("/")[0]) + float(
                self.db.get_st_rep_ex(date_s,date_d,gp, i[0]).split("/")[0]) + float(
                self.db.get_st_rep_ex_deg(date_s,date_d,gp, i[0]).split("/")[0])
            max = float(
                self.db.get_st_rep_att(date_s,date_d,gp, i[0]).split("/")[1]) + float(
                self.db.get_st_rep_ex(date_s,date_d,gp, i[0]).split("/")[1]) + float(
                self.db.get_st_rep_ex_deg(date_s,date_d,gp, i[0]).split("/")[1])

            try:
                ratio = (value / max) * 100
            except:
                ratio = 0
            self.all_items.setItem(n, 6, QTableWidgetItem(str("%.2f" % ratio) + " %"))