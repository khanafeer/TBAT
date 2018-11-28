# -*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
from model.Model import Model
import datetime
import sys
from printing import print_doc
from views.report import Ui_Form as report
class report(QWidget, report):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.pr = print_doc()
        for i in self.findChildren(QWidget):
            i.setAttribute(Qt.WA_StyledBackground, True)
        self.db = Model()
        self.gp_name=None
        #self.all_items.hide()
        self.all_btn.clicked.connect(self.get_student_report_info)
        self.st_dt.setDateTime(datetime.datetime.now())
        self.end_dt.setDateTime(datetime.datetime.now())





    def get_student_report_info(self):
        d1 = self.st_dt.date().toString("yyyy-MM-dd")
        d2 = self.end_dt.date().toString("yyyy-MM-dd")
        num_day=self.db.get_specific_course_days(self.gp_name,d1,d2)
        month=self.db.get_specific_course_months(self.gp_name,d1,d2)


        l=[]
        students=self.db.get_students_name()
        for st in students:
            groups=self.db.get_student_report_info(st)
            for i in list(groups):
                self.gp_name=i[2]
                if i[4]==u'بالحصة':
                    max=num_day * i[3]
                elif i[4]==u'بالشهر':
                    max=len(month) * i[3]
                else:
                    max=i[3]
            l.append([i[0],i[1],i[2],i[4],max])
            final_list=[]
            for i in l:
                gp_name=i[2]
                st_bc=i[0]
                paid_date=self.db.get_paid_date(st_bc,gp_name)

                gps_months=self.db.get_specific_course_months(gp_name,d1,d2)
                print "this is month",gps_months
                for j in gps_months:
                    print type(i)
                    print type(gps_months)
                    print type(paid_date)


                    final_list.append(i+gps_months+paid_date)


            self.all_items.setRowCount(0)
            print 11111111
            for i in final_list:
                print 2222222222
                for j in i:
                    print 3333333333333
                    n = self.all_items.rowCount()
                    self.all_items.insertRow(n)
                    self.all_items.setItem(n, 0, QTableWidgetItem(unicode(j[0])))
                    self.all_items.setItem(n, 1, QTableWidgetItem(unicode(j[1])))
                    self.all_items.setItem(n, 2, QTableWidgetItem(unicode(j[2])))
                    self.all_items.setItem(n, 3, QTableWidgetItem(unicode(j[3])))

                    self.all_items.setItem(n, 4, QTableWidgetItem(unicode(j[5])))
                    self.all_items.setItem(n, 5, QTableWidgetItem(unicode(j[4])))
                    self.all_items.setItem(n, 6, QTableWidgetItem(unicode(j[6])))
                    self.all_items.setItem(n, 7, QTableWidgetItem(unicode(j[7])))


































        '''self.search_btn.clicked.connect(self.get_all_mony)
        self.all_btn.clicked.connect(self.sh_hd)
        self.st_dt.setDateTime(datetime.datetime.now())
        self.end_dt.setDateTime(datetime.datetime.now())
        self.print_btn.clicked.connect(self.print_choose)
    def sh_hd(self):
        if self.all_items.isHidden():
            self.print_btn.clicked.connect(self.print_choose)
            self.all_items.show()
        else:
            self.all_items.hide()
    def get_all_mony(self):
        d1 = self.st_dt.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        d2 = self.end_dt.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        values = self.db.get_all_mony(d1,d2)

        t = 0
        b = 0
        self.all_items.setRowCount(0)
        for i in values:
            t += i[5]
            b += i[6]
            n = self.all_items.rowCount()
            self.all_items.insertRow(n)
            x = 0
            for j in i:
                self.all_items.setItem(n,x,QTableWidgetItem(unicode(j)))
                x += 1
        self.all_items.resizeColumnsToContents()
        self.all_lbl.setText(unicode(t))
        self.baid_lbl.setText(unicode(b))
        self.rest_lbl.setText(unicode(t-b))
        self.tottal_lbl.setText(unicode(b))
    def print_choose(self):
        d1 = self.st_dt.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        d2 = self.end_dt.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        if self.all_items.isHidden():
            self.pr.print_tottal(d1,d2,self.all_lbl.text(),self.baid_lbl.text(),self.rest_lbl.text())
        else:
            self.pr.print_tottal_log(self.get_data(),d1,d2,self.all_lbl.text(),self.baid_lbl.text(),self.rest_lbl.text())
    def get_data(self):
        s = []
        a = []
        n = self.all_items.columnCount()
        for i in range(n):
            s.append(self.all_items.horizontalHeaderItem(i).text())
        a.append(s)
        x = self.all_items.rowCount()
        for i in range(x):
            s = []
            for j in range(n):
                s.append(self.all_items.item(i,j).text())
            a.append(s)'''
        #return a