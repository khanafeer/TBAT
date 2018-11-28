# -*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
from model.Model import Model
from model.table_model import MyTableModel
import datetime
from views.report_all import Ui_Form as report_all
class Report_all(QWidget, report_all):
    st_bc = None
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        for i in self.findChildren(QWidget):
            i.setAttribute(Qt.WA_StyledBackground, True)
        self.gp_btn.setStyleSheet("background:#757780;")
        self.exm_btn.setStyleSheet("")
        self.all_btn.clicked.connect(self.all_show)
        self.gp_btn.clicked.connect(self.gp_show)
        self.exm_btn.clicked.connect(self.exm_show)
        self.db = Model()
        self.gp_show()
        self.info_tbl.setLayoutDirection(Qt.RightToLeft)
        self.connect(self.tableView, SIGNAL("clicked(const QModelIndex&)"), self.tbl_select)
        self.start_dt.setDate(datetime.datetime.now())
        self.end_dt.setDate(datetime.datetime.now())


    def all_show(self):
        self.tp="all"
        self.all_btn.setStyleSheet("background:#757780;")
        self.exm_btn.setStyleSheet("")
        self.gp_btn.setStyleSheet("")
        gps = self.db.get_group_list()
        if gps:
            table_model = MyTableModel(self, gps,
                                       [u'المجموعة', u'عدد الطلاب'])
            self.tableView.setModel(table_model)
            self.tableView.resizeColumnsToContents()
            self.tableView.setFocus()
            self.tbl_select(0)
        else:
            self.tableView.setModel(None)
    def gp_show(self):
        self.tp = "course"
        self.gp_btn.setStyleSheet("background:#757780;")
        self.exm_btn.setStyleSheet("")
        self.all_btn.setStyleSheet("")
        gps = self.db.get_group_list()
        if gps:
            table_model = MyTableModel(self, gps,
                                       [u'المجموعة',u'عدد الطلاب'])
            self.tableView.setModel(table_model)
            self.tableView.resizeColumnsToContents()
            self.tableView.setFocus()
            self.tbl_select(0)
        else:
            self.tableView.setModel(None)
    def exm_show(self):
        self.gp_btn.setStyleSheet("")
        self.all_btn.setStyleSheet("")
        self.exm_btn.setStyleSheet("background:#757780;")
        self.tp = "exam"
        gps = self.db.get_exam_list()
        if gps:
            table_model = MyTableModel(self, gps,
                                       [u'الاختبارات', u'عدد الطلاب'])
            self.tableView.setModel(table_model)
            self.tableView.resizeColumnsToContents()
            self.tableView.setFocus()
            self.tbl_select(0)
        else:
            self.tableView.setModel(None)
    def tbl_select(self,row,col=0):
        try:
            row = int(row)
        except:
            row = row.row()
        self.tableView.selectRow(row)
        gp_name = self.tableView.model().get_data(row,0)
        self.group_all_report(gp_name)
    def group_all_report(self,gp):
        d1 = self.start_dt.date().toPython()
        d2 = self.end_dt.date().toPython()
        lis=[]
        if self.tp == 'course':
            st = self.db.get_gp_att_abs(gp,d1,d2)
            h =  [u'الطالب',u'الاسم',u'الحضور',u'الغياب' ,u'نسبة الحضور']
            for i, j in st.iteritems():
                lis.append([unicode(i), self.db.get_student(i)[1], unicode(j[0]), unicode(j[1]), unicode(j[2])])
        elif self.tp=="exam":
            st = self.db.get_ex_att_abs([gp],d1,d2)

            h =  [u'الطالب',u'الاسم',u'الحضور',u'الغياب' ,u'نسبة الحضور',u'نسبة الدرجات']
            for i, j in st.iteritems():
                lis.append([unicode(i), self.db.get_student(i)[1], unicode(j[0]), unicode(j[1]), unicode(j[2]), unicode(j[3])])



        else:
            dic1 = self.db.get_gp_att_abs(gp, d1, d2) #get course info
            li=[]
            l=self.db.get_exams_of_course(gp) #get list of exams that belong to particular course
            dic2 = self.db.get_ex_att_abs(l, d1, d2)
            h=[u'الطالب',u'الاسم',u'حضور المجموعة',u'غياب المجموعة',u'نسبة حضور المجموعة',u'حضور الاختبار',u'غياب الاختبار',u'نسبة حضور الاختبار',u'نسبة الدرجات']
            d3 = {}
            for i,j in dic1.iteritems():
                d3.setdefault(i,[]).extend([unicode(i), self.db.get_student(i)[1], unicode(j[0]), unicode(j[1]), unicode(j[2])])
            for v,k in dic2.iteritems():
                d3.setdefault(v, []).extend([unicode(k[0]), unicode(k[1]), unicode(k[2]),unicode(k[3])])
            lis = d3.values()
            print lis
        if lis:
            table_model = MyTableModel(self, lis,h)
            self.info_tbl.setModel(table_model)
            self.info_tbl.resizeColumnsToContents()
            self.info_tbl.setFocus()
        else:
            self.info_tbl.setModel(None)
