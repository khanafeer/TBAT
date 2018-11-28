# -*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
from model.Model import Model
from model.table_model import MyTableModel
import datetime
import operator
from printing import print_doc
from views.mony_dw import Ui_Form as mony_dw
from views.students_dw import Ui_Form as students_dw
from views.students_add import Ui_Form as student
from views.course_select_dw import Ui_Form as gp_dw
from views.students_info import Ui_Form as st_info
from views.st_gp_switch import Ui_Form as st_gp_switch
from ctrls.bc_num import bc_num
class st_gp_switch(QWidget, st_gp_switch):
    st_bc = None
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        for i in self.findChildren(QWidget):
            i.setAttribute(Qt.WA_StyledBackground, True)
class students_dw(QWidget, students_dw):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.setWindowTitle(u'بيانات الطالب')
        for i in self.findChildren(QWidget):
            i.setAttribute(Qt.WA_StyledBackground, True)
class gp_dw(QWidget, gp_dw):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.setWindowTitle(u'المجموعة')
        for i in self.findChildren(QWidget):
            i.setAttribute(Qt.WA_StyledBackground, True)
class mony_dw(QWidget, mony_dw):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.setWindowTitle(u'دفع مالية')
        self.baid_spn.setRange(0,10000000)
        for i in self.findChildren(QWidget):
            i.setAttribute(Qt.WA_StyledBackground, True)

class student_info(QWidget, st_info):
    BC = 0
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.setWindowTitle(u'تفاصيل الطالب')
        self.db = Model()
        self.pr = print_doc()
        self.gp_dw = gp_dw()
        self.st_gp_switch = st_gp_switch()
        self.centerx(self.st_gp_switch)
        self.mony_dw = mony_dw()
        self.centerx(self.gp_dw)
        self.centerx(self.mony_dw)
        for i in self.findChildren(QWidget):
            i.setAttribute(Qt.WA_StyledBackground, True)
        self.groups_btn.clicked.connect(self.student_group)
        self.add_group_btn.clicked.connect(self.show_gp_get)
        self.gp_dw.add_btn.clicked.connect(self.add_st_course)
        self.table_st_course.cellClicked.connect(self.del_st_course)
        self.attend_btn.clicked.connect(self.fill_courses_att)
        self.mony_btn.clicked.connect(self.fill_courses_mn)
        self.course_cmb.currentIndexChanged.connect(self.fill_att_months)
        self.att_search_btn.clicked.connect(self.attend_st_fill)
        self.month_cmb.currentIndexChanged.connect(self.attend_st_fill)
        self.mn_search_btn.clicked.connect(self.mony_st_fill)
        self.course_mn_cmb.currentIndexChanged.connect(self.mony_st_fill)
        self.mn_table.cellClicked.connect(self.buy_mony)
        self.mony_dw.put_mony_btn.clicked.connect(self.buy_mony_db)
        self.att_print_btn.clicked.connect(self.print_attend)
        self.mn_print_btn.clicked.connect(self.print_mony)
        self.connect(self.att_table, SIGNAL("doubleClicked(const QModelIndex&)"), self.change_st_status)
        self.color_btn()
        self.st_gp_switch.pushButton.clicked.connect(self.switch)



    def focusInEvent(self, *args, **kwargs):
        indx = self.stackedWidget.currentIndex()
        if indx == 0:
            self.student_group()
        elif indx == 1:
            self.fill_courses_att()
        else:
            self.fill_courses_mn()
    def switch(self):
        if self.db.student_group_swift(self.BC,self.st_gp_switch.label_3.text(),self.st_gp_switch.comboBox.currentText()):
            self.show_st_courses()
            self.st_gp_switch.hide()
    def color_btn(self):
        try:
            for i in self.widget_4.findChildren(QPushButton):
                i.setStyleSheet("background:#05B963;")
            self.sender().setStyleSheet("background:#A8B1B2;")
        except:
            self.mony_btn.setStyleSheet("background:#A8B1B2;")
    def set_bc(self,bc):
        self.BC = bc
    def buy_mony(self, row, column):
        self.get_mony_id()
        if column == 4:
            self.mony_dw.show()
            self.mony_dw.activateWindow()
            self.mony_dw.raise_()
            self.mony_dw.barcode_lbl.setText(self.BC)
            index = self.mony_dw.mid.findText(self.mn_table.item(row, 0).text(), Qt.MatchFixedString)
            if index >= 0:
                self.mony_dw.mid.setCurrentIndex(index)
            self.mony_dw.gp_lbl.setText(self.course_mn_cmb.currentText())
            self.mony_dw.tottal_lbl.setText(self.mn_table.item(row, 1).text())
            self.mony_dw.baid_spn.setValue(float(self.mn_table.item(row, 3).text()))
            self.mony_dw.baid_spn.setRange(0, float(self.mn_table.item(row, 3).text()))

    def get_mony_id(self):
        cname = self.course_mn_cmb.currentText()
        course_name = self.db.get_course_by_name(cname)[7]
        if course_name == u'بالحصة':       #fill  mony_dw with  the days of the course
            v = self.db.get_course_days(cname)
            self.mony_dw.mid.clear()
            for i in v:
                self.mony_dw.mid.addItem(str(i[0]) + " : " + str(i[1]) + " : " + str(i[2]))
        elif course_name == u'بالشهر':      #fill mony_dw with the monthes of the course
            v = self.db.get_course_months(cname)
            self.mony_dw.mid.clear()
            self.mony_dw.mid.addItems(v)
        else:
            self.mony_dw.mid.clear()
            self.mony_dw.mid.addItem(cname)

    def print_attend(self):
        course = self.course_cmb.currentText()
        month = self.month_cmb.currentText()
        if course and month:
            self.pr.print_attend_st(self.get_data_attend(), course, month, self.name_lbl.text(), self.ph_lbl.text(),
                                    self.fph_lbl.text())
        else:
            self.dialoge_only(u'لا يوجد بيانات للطباعة', u'راجع بيانات البحث')
    def print_mony(self):
        course = self.course_mn_cmb.currentText()
        if course:
            self.pr.print_mony_st(self.get_data_mony(), course, self.name_lbl.text(), self.ph_lbl.text(),
                                  self.fph_lbl.text())
        else:
            self.dialoge_only(u'لا يوجد بيانات للطباعة', u'راجع بيانات البحث')
    def get_data_attend(self):
        s = []
        a = []
        n = self.att_table.columnCount()
        for i in range(n):
            s.append(self.att_table.horizontalHeaderItem(i).text())
        a.append(s)
        x = self.att_table.rowCount()
        for i in range(x):
            s = []
            for j in range(n):
                s.append(self.att_table.item(i, j).text())
            a.append(s)
        return a
    def get_data_mony(self):
        s = []
        a = []
        n = self.mn_table.columnCount()
        for i in range(n - 1):
            s.append(self.mn_table.horizontalHeaderItem(i).text())
        a.append(s)
        x = self.mn_table.rowCount()
        for i in range(x):
            s = []
            for j in range(n - 1):
                s.append(self.mn_table.item(i, j).text())
            a.append(s)
        return a
    def buy_mony_db(self):
        self.color_btn()
        if self.db.put_st_mony(self.mony_dw.barcode_lbl.text(), self.mony_dw.gp_lbl.text(),
                               self.db.get_method_price(self.mony_dw.gp_lbl.text())[0], self.mony_dw.mid.currentText(),
                               self.mony_dw.baid_spn.value()):
            self.mony_dw.hide()
            self.mony_st_fill()
    def show_gp_get(self):
        self.gp_dw.show()
        self.gp_dw.activateWindow()
        self.gp_dw.raise_()
        self.gp_dw.course_cmb.clear()
        self.gp_dw.course_cmb.addItems(self.db.get_groups())
    def fill_courses_att(self):
        self.color_btn()
        if self.BC:
            cs = self.db.get_groups_st(self.BC)
            self.course_cmb.clear()
            self.course_cmb.addItems(cs)
            self.stackedWidget.setCurrentIndex(1)
        else:
            self.dialoge_only(u'لا يوجد طالب', u'اختر طالب اولا')
    def fill_courses_mn(self):
        self.color_btn()
        if self.BC:
            cs = self.db.get_groups_st(self.BC)
            self.course_mn_cmb.clear()
            self.course_mn_cmb.addItems(cs)
            self.stackedWidget.setCurrentIndex(2)
        else:
            self.dialoge_only(u'لا يوجد طالب', u'اختر طالب اولا')
    def fill_att_months(self):
        name = self.course_cmb.currentText()
        if name:
            mn = self.db.get_course_months(name)
            self.month_cmb.clear()
            self.month_cmb.addItems(mn)
    def student_group(self):
        self.color_btn()
        if self.BC:
            self.stackedWidget.setCurrentIndex(0)
            self.show_st_courses()
        else:
            self.dialoge_only(u'لا يوجد طالب', u'اختر طالب اولا')
    def show_st_courses(self):
        x = self.db.get_st_gp(self.BC)
        self.table_st_course.setRowCount(0)
        for i in x:
            n = self.table_st_course.rowCount()
            self.table_st_course.insertRow(n)
            self.table_st_course.setItem(n, 0, QTableWidgetItem(unicode(i[0])))
            self.table_st_course.setItem(n, 1, QTableWidgetItem(unicode(i[1])))
            self.table_st_course.setItem(n, 2, QTableWidgetItem(unicode(i[2])))
            self.table_st_course.setItem(n, 3, QTableWidgetItem(u'حذف'))
            self.table_st_course.item(n, 3).setBackground(QColor(231, 76, 62))
            self.table_st_course.setItem(n, 4, QTableWidgetItem(u'تبديل'))
            self.table_st_course.item(n, 4).setBackground(QColor(45, 180, 45))
    def del_st_course(self, row, column):
        if column == 3:
            if self.dialoge_only(u'سيتم حذف الطالب من هذة الدورة', u'هل انت متاكد من الحذف') == QMessageBox.Ok:
                if self.db.del_st_course(self.BC, self.table_st_course.item(row, 0).text()):
                    self.show_st_courses()
        elif column == 4:
            self.st_gp_switch.st_bc = self.BC
            self.st_gp_switch.showNormal()
            self.st_gp_switch.raise_()
            self.st_gp_switch.activateWindow()
            self.st_gp_switch.setFocus()
            self.st_gp_switch.label_3.setText(self.table_st_course.item(row, 0).text())
            self.st_gp_switch.comboBox.clear()
            for i in self.db.get_all_courses():
                if i[1] != self.st_gp_switch.label_3.text():
                    self.st_gp_switch.comboBox.addItem(i[1])
    def add_st_course(self):
        if self.gp_dw.course_cmb.currentText():
            course = self.gp_dw.course_cmb.currentText()
            st_phone = self.BC
            if self.db.st_gp_not_exist(st_phone, course):
                if self.db.add_st_gp(st_phone, course):
                    self.gp_dw.hide()
                    self.show_st_courses()
                else:
                    self.dialoge_only(u'لم تتم عملية الاضافة بنجاح', u'حاول مرة اخرى')
            else:
                self.dialoge_only(u'الطالب موجود فى المجموعة بالفعل', u'جرب مجموعة اخرى')
    def centerx(self, x):
        frameGm = x.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        x.move(frameGm.topLeft())
    def dialoge_only(self, x, y):
        msgBox = QMessageBox()
        msgBox.setFixedSize(150, 100)
        msgBox.setWindowTitle(u'تحذير')
        msgBox.setText(unicode(x))
        msgBox.setInformativeText(y)
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        return msgBox.exec_()
    def mony_st_fill(self):
        cname = self.course_mn_cmb.currentText()

        method_price = self.db.get_method_price(cname)
        if cname:
            price_for_studetn=self.db.get_course_price_by_name(cname,self.BC)

        tottal = 0
        baid = 0
        if method_price:
            self.mn_table.setRowCount(0)
            if method_price[0] == u'بالحصة':
                v = self.db.get_course_days(cname)
                for i in v:
                    n = self.mn_table.rowCount()
                    self.mn_table.insertRow(n)
                    x = self.db.get_st_mony(self.BC, cname,str(i[0]) + " : " + str(i[1]) + " : " + str(i[2]))
                    self.mn_table.setItem(n, 0, QTableWidgetItem(str(i[0]) + " : " + str(i[1]) + " : " + str(i[2])))
                    self.mn_table.setItem(n, 1, QTableWidgetItem(unicode(price_for_studetn)))
                    self.mn_table.setItem(n, 2, QTableWidgetItem(unicode(x)))
                    self.mn_table.setItem(n, 3, QTableWidgetItem(unicode(price_for_studetn - x)))
                    self.mn_table.setItem(n, 4, QTableWidgetItem(u'دفع'))
                    self.mn_table.item(n, 4).setBackground(QColor(20, 200, 10))
                    tottal += method_price[1]
                    baid += x
            elif method_price[0] == u'بالشهر':
                v = self.db.get_course_months(cname)
                for i in v:
                    n = self.mn_table.rowCount()
                    self.mn_table.insertRow(n)
                    x = self.db.get_st_mony(self.BC, cname, i)
                    self.mn_table.setItem(n, 0, QTableWidgetItem(i))
                    self.mn_table.setItem(n, 1, QTableWidgetItem(unicode(price_for_studetn)))
                    self.mn_table.setItem(n, 2, QTableWidgetItem(unicode(x)))
                    self.mn_table.setItem(n, 3, QTableWidgetItem(unicode(price_for_studetn - x)))
                    self.mn_table.setItem(n, 4, QTableWidgetItem(u'دفع'))
                    self.mn_table.item(n, 4).setBackground(QColor(20, 200, 10))
                    tottal += method_price[1]
                    baid += x
            else:
                n = self.mn_table.rowCount()
                self.mn_table.insertRow(n)
                x = self.db.get_st_mony(self.BC, cname, cname)
                self.mn_table.setItem(n, 0, QTableWidgetItem(cname))
                self.mn_table.setItem(n, 1, QTableWidgetItem(unicode(price_for_studetn)))
                self.mn_table.setItem(n, 2, QTableWidgetItem(unicode(x)))
                self.mn_table.setItem(n, 3, QTableWidgetItem(unicode(price_for_studetn - x)))
                self.mn_table.setItem(n, 4, QTableWidgetItem(u'دفع'))
                self.mn_table.item(n, 4).setBackground(QColor(20, 200, 10))
                tottal += method_price[1]
                baid += x
            self.tottal_mony.setText(unicode(tottal))
            self.baid_mony.setText(unicode(baid))
            self.rest_mony.setText(unicode(tottal - baid))
        else:
            self.mn_table.setRowCount(0)
            self.tottal_mony.setText("0")
            self.baid_mony.setText("0")
            self.rest_mony.setText("0")

    def change_st_status(self, indx):
        col = indx.row()
        st = self.BC
        info = self.att_table.item(col, 0).text().split(" : ")
        gpid = self.db.get_course_by_name(self.course_cmb.currentText())[0]
        dt_st = self.att_table.item(col, 1).text()
        if dt_st == u'غائب':
            if self.db.attend_st_gp(st, gpid, info[0], info[1], info[2], u'حضور'):
                self.att_table.setItem(col, 1, QTableWidgetItem(u'حاضر'))
        else:
            if self.db.attend_st_gp(st, gpid, info[0], info[1], info[2], u'غياب'):
                self.att_table.setItem(col, 1, QTableWidgetItem(u'غائب'))
    def attend_st_fill(self):
        v = self.db.get_course_dates(self.course_cmb.currentText())
        if self.month_cmb.currentText():
            mon = self.month_cmb.currentText().split(" - ")[0]
            year = self.month_cmb.currentText().split(" - ")[1]
            self.att_table.setRowCount(0)
            att = 0
            aps = 0
            for i in v:
                if str(i[0].month) == mon and str(i[0].year) == year:
                    n = self.att_table.rowCount()
                    self.att_table.insertRow(n)
                    self.att_table.setItem(n, 0, QTableWidgetItem(str(i[0]) + " : " + str(i[1]) + " : " + str(i[2])))
                    if self.db.check_attend(self.BC, i[0],i[1],i[2]):
                        att += 1
                        self.att_table.setItem(n, 1, QTableWidgetItem(u'حاضر'))
                    else:
                        aps += 1
                        self.att_table.setItem(n, 1, QTableWidgetItem(u'غائب'))
            if self.month_cmb.currentText():
                self.att_table.resizeColumnsToContents()
                self.attend.setText(unicode(att))
                self.absent.setText(unicode(aps))
                try:
                    self.ratio.setText(unicode((att / (att + aps)) * 100))
                except:
                    self.ratio.setText(unicode(0))
class student(QWidget, student):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.db = Model()
        self.pr=print_doc()
        self.phone = None
        self.barcode = None
        self.completer_set()
        self.st_dw = students_dw()
        self.st_info = student_info()
        self.st_dw.ph_lbl.hide()
        self.st_dw.bc_lbl.hide()
        self.centerx(self.st_dw)
        self.bc_num = bc_num()
        self.centerx(self.bc_num)
        self.centerx(self.st_info)
        self.add_btn.clicked.connect(self.st_sh_add)
        self.connect(self.all_students, SIGNAL("clicked(const QModelIndex&)"), self.st_sh_edt)
        self.connect(self.all_students, SIGNAL("doubleClicked(const QModelIndex&)"), self.rep_sh)
        self.search_edt.returnPressed.connect(self.st_search)
        self.st_dw.add_btn.clicked.connect(self.add_st)
        self.st_dw.edite_btn.clicked.connect(self.edite_st)
        self.st_dw.delete_btn.clicked.connect(self.del_st)
        self.search_edt.setFocus()
        self.print_btn.clicked.connect(lambda :self.bc_num.pre_show(self.all_students.model().mylist))
        self.st_dw.barcode_get_btn.clicked.connect(lambda: self.st_dw.bc_edt.setText(self.db.generate_barcode()))

        self.print_student_info.clicked.connect(self.print_f)

    def print_f(self):
        x = []
        x.append(self.all_students.model().header[:-2])
        x.extend([aax[:-2] for aax in self.all_students.model().mylist])
        self.pr.print_info(x,u'تقرير الطالب')


    def focusInEvent(self, *args, **kwargs):
        self.completer_set()
        self.all_students_fill()
    def rep_sh(self,index):
            row = index.row()
            barcode = self.all_students.model().get_data(row, 0)
            self.barcode = barcode
            if self.barcode:
                self.st_info.set_bc(self.barcode)
                self.st_info.showNormal()
                self.st_info.raise_()
                self.st_info.activateWindow()
                self.st_info.setFocus()

    def all_students_fill(self):
        students = self.db.get_all_students()
        if students:
            table_model = MyTableModel(self, students,
            [u'الباركود', u'الاسم', u'المدرسة', u'هاتف الطالب', u'هاتف ولى الامر', u'البريد الالكترونى',u'العنوان',u'تفاصيل',u'تعديل - حذف',u'طباعة'])
            self.all_students.setModel(table_model)
            self.all_students.resizeColumnsToContents()
            table_model.col_num = 8
            table_model.data = table_model.data_col_column
        else:
            self.all_students.setModel(None)
        self.setFocus()
    def completer_set(self):
        completer = QCompleter()
        completer.setCompletionMode(QCompleter.PopupCompletion)
        completer.activated.connect(self.st_search)
        model = QStringListModel()
        completer.setModel(model)
        self.db.get_students(model)
        self.search_edt.setCompleter(completer)
    def st_sh_add(self):
        self.st_dw.add_btn.show()
        self.st_dw.edite_btn.hide()
        self.st_dw.delete_btn.hide()
        self.st_dw.reports_btn.hide()
        self.st_dw.show()
        self.st_dw.activateWindow()
        self.st_dw.raise_()
        self.clear_st()
    def st_sh_edt(self,index):
        if index.column() == 8:
            row = index.row()
            barcode = self.all_students.model().get_data(row, 0)
            self.barcode = barcode
            phone = self.all_students.model().get_data(row, 3)
            if self.barcode:
                self.st_dw.bc_lbl.setText(self.barcode)
                self.st_dw.ph_lbl.setText(phone)
                self.st_dw.add_btn.hide()
                self.st_dw.reports_btn.hide()
                self.st_dw.edite_btn.show()
                self.st_dw.delete_btn.show()
                self.st_dw.show()
                self.st_dw.activateWindow()
                self.st_dw.raise_()
                self.fill_dw(barcode)
            else:
                self.dialoge_only(u'لا يوجد طالب', u'اختر طالب اولا')
        elif index.column() == 9:
            self.bc_num.pre_show([[self.all_students.model().get_data(index.row(),0),self.all_students.model().get_data(index.row(),1)]])
    def del_st(self):
        bc = self.st_dw.bc_lbl.text()
        if bc:
            if self.dialoge_only(u'سيتم حذف الطالب وكل العمليات المتعلقة به',
                                 u'هل انت متاكد من الحذف') == QMessageBox.Ok:
                if self.db.delete_student(bc):
                    self.completer_set()
                    self.st_dw.hide()
                    self.all_students_fill()
                else:
                    self.dialoge_only(u'لم تتم عملية الحذف', u'راجع الاتصال بالشبكة')
        else:
            self.dialoge_only(u'لا يوجد طالب', u'اختر الطالب اولا')
    def st_search(self):
        barcode = self.search_edt.text()
        self.barcode = barcode
        if self.barcode:
            self.st_dw.bc_lbl.setText(self.barcode)
            self.st_dw.add_btn.hide()
            self.st_dw.edite_btn.show()
            self.st_dw.delete_btn.show()
            self.st_dw.reports_btn.show()
            self.st_dw.show()
            self.st_dw.activateWindow()
            self.st_dw.raise_()
            self.fill_dw(barcode)
    def fill_dw(self,st_bc):
        bc = self.db.get_student(st_bc)
        if bc:
            self.st_dw.bc_lbl.setText(bc[0])
            self.st_dw.ph_lbl.setText(bc[3])
            self.st_dw.bc_edt.setText(bc[0])
            self.st_dw.nm_edt.setText(bc[1])
            self.st_dw.school_edt.setText(bc[2])
            self.st_dw.ph_edt.setText(bc[3])
            self.st_dw.fphon_edt.setText(bc[4])
            self.st_dw.address_edt.setText(bc[5])
            self.st_dw.mail_edt.setText(bc[6])
            self.st_dw.details_edt.setText(bc[7])
    def add_st(self):
        bc = self.st_dw.bc_edt.text()
        nm = self.st_dw.nm_edt.text()
        school = self.st_dw.school_edt.text()
        sph = self.st_dw.ph_edt.text()
        fph = self.st_dw.fphon_edt.text()
        add = self.st_dw.address_edt.text()
        mail = self.st_dw.mail_edt.text()
        det = self.st_dw.details_edt.toPlainText()
        if bc and nm:
            s_exist = self.db.student_exist(bc, nm)
            if s_exist == 1:
                if not self.db.add_student(bc, nm, school, sph, fph, mail, add, det):
                    self.dialoge_only(u'خطأ فى اضافة الطالب', u'يرجى اعادة ادخال القيم الصحيحة')
                else:
                    self.clear_st()
                    self.st_dw.hide()
                    self.completer_set()
                    self.all_students_fill()
            elif s_exist == 2:
                self.dialoge_only(u'الباركود موجود من قبل', u'راجع البيانات وادخل بيانات جديدة')
            elif s_exist == 3:
                self.dialoge_only(u'الاسم موجود من قبل', u'راجع البيانات وادخل بيانات جديدة')
        else:
            self.dialoge_only(u'البيانات غير كاملة', u'ادخل الاسم والباركود على الاقل')
    def edite_st(self):
        oldbc = self.st_dw.bc_lbl.text()
        bc = self.st_dw.bc_edt.text()
        nm = self.st_dw.nm_edt.text()
        school = self.st_dw.school_edt.text()
        sph = self.st_dw.ph_edt.text()
        fph = self.st_dw.fphon_edt.text()
        mail = self.st_dw.mail_edt.text()
        add = self.st_dw.address_edt.text()
        det = self.st_dw.details_edt.toPlainText()
        t = ''
        for i in self.st_dw.findChildren(QRadioButton):
            if i.isChecked():
                t = i.text()
        if bc and nm:
            if not self.db.edite_student(oldbc, bc, nm, school, sph, fph, mail, add, det):
                self.dialoge_only(u'خطأ فى تحديث بيانات المتدرب', u'يرجى اعادة ادخال القيم الصحيحة')
            else:
                self.clear_st()
                self.st_dw.hide()
                self.completer_set()
                self.all_students_fill()
        else:
            self.dialoge_only(u'البيانات غير كاملة', u'ادخل الاسم والهاتف على الاقل')
    def clear_st(self):
        self.st_dw.bc_lbl.clear()
        self.st_dw.ph_lbl.clear()
        self.st_dw.bc_edt.clear()
        self.st_dw.nm_edt.clear()
        self.st_dw.school_edt.clear()
        self.st_dw.ph_edt.clear()
        self.st_dw.fphon_edt.clear()
        self.st_dw.address_edt.clear()
        self.st_dw.mail_edt.clear()
        self.st_dw.details_edt.clear()
    def centerx(self, x):
        frameGm = x.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        x.move(frameGm.topLeft())
    def dialoge_only(self, x, y):
        msgBox = QMessageBox()
        msgBox.setFixedSize(150, 100)
        msgBox.setWindowTitle(u'تحذير')
        msgBox.setText(unicode(x))
        msgBox.setInformativeText(y)
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        return msgBox.exec_()