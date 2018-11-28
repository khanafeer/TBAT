# -*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
from model.Model import Model
from model.table_model import MyTableModel
import datetime
import sys
from printing import print_doc
from views.course_add import Ui_Form as course
from views.course_dw import Ui_Form as course_dw
from views.day_select_dw import Ui_Form as day_select_dw
from views.date_select import Ui_Form as date_select
from views.mony_dw import Ui_Form as mony_dw
from views.students_dw import Ui_Form as students_dw
from views.course_info import Ui_Form as course_info
from ctrls.bc_num import bc_num
from views.st_gp_switch import Ui_Form as st_gp_switch
from views.specisal_price import Ui_Form as special_price

class Special_Price(QWidget, special_price):
    st_bc = None
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        for i in self.findChildren(QWidget):
            i.setAttribute(Qt.WA_StyledBackground, True)
        self.price_spn.setRange(0,9999999)
        self.setWindowTitle(u'تغير سعر المجموعة للطالب')

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
class course_dw(QWidget, course_dw):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.setWindowTitle(u'بيانات المجموعة')
        for i in self.findChildren(QWidget):
            i.setAttribute(Qt.WA_StyledBackground, True)
class mony_dw(QWidget, mony_dw):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.baid_spn.setRange(0,10000000)
        for i in self.findChildren(QWidget):
            i.setAttribute(Qt.WA_StyledBackground, True)
class day_select_dw(QWidget, day_select_dw):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.setWindowTitle(u'اختر المواعيد')
        for i in self.findChildren(QWidget):
            i.setAttribute(Qt.WA_StyledBackground, True)
class date_select(QWidget, date_select):
    date_id = None
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.setWindowTitle(u'اختر تاريخ الموعد')
        for i in self.findChildren(QWidget):
            i.setAttribute(Qt.WA_StyledBackground, True)
class course(QWidget, course):
    barcode = None
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.cs_dw = course_dw()
        self.course_info = course_info()
        self.db = Model()
        self.pr=print_doc()
        self.special_price=Special_Price()
        self.search_edt.setFocus()
        self.centerx(self.cs_dw)
        self.centerx(self.course_info)
        self.cs_dw.nm_lbl.hide()
        for i in self.cs_dw.findChildren(QSpinBox):
            i.setRange(0,100000)
        for i in self.cs_dw.findChildren(QDoubleSpinBox):
            i.setRange(0,sys.float_info.max)
        self.add_btn.clicked.connect(self.st_sh_add)
        self.connect(self.all_courses, SIGNAL("doubleClicked(const QModelIndex&)"), self.sh_st)
        self.connect(self.all_courses, SIGNAL("clicked(const QModelIndex&)"), self.sh_st_edt)
        self.render_all_courses()
        self.cs_dw.add_btn.clicked.connect(self.add_course)
        self.cs_dw.edite_btn.clicked.connect(self.edite_course)
        self.cs_dw.del_btn.clicked.connect(self.del_course)
        self.print_btn.clicked.connect(self.print_f)

    def print_f(self):
        x = []
        x.append(self.all_courses.model().header[:-1])
        x.extend([aax[:-1] for aax in self.all_courses.model().mylist])
        self.pr.print_info(x, u'تقرير المجموعة')

    def focusInEvent(self, *args, **kwargs):
        self.completer_set()
    def sh_st_edt(self,index):
        if index.column() == 11:
            row = index.row()
            barcode = self.all_courses.model().get_data(row, 1)
            self.barcode = barcode
            if self.barcode:
                self.cs_dw.add_btn.hide()
                self.cs_dw.details_btn.hide()
                self.cs_dw.edite_btn.show()
                self.cs_dw.del_btn.show()
                self.cs_dw.showNormal()
                self.fill_dw()

    def sh_st(self,index):
        row = index.row()
        barcode = self.all_courses.model().get_data(row, 1)
        self.barcode = barcode
        if self.barcode:
            self.course_info.set_cs_id(self.barcode)
            self.course_info.showNormal()
            self.course_info.raise_()
            self.course_info.activateWindow()
            self.course_info.setFocus()





    def completer_set(self):
        completer = QCompleter()
        completer.setCompletionMode(QCompleter.PopupCompletion)
        completer.activated.connect(self.get_course)
        model = QStringListModel()
        completer.setModel(model)
        self.db.get_courses(model)
        self.search_edt.setCompleter(completer)
    def st_sh_add(self):
        self.cs_dw.add_btn.showNormal()
        self.cs_dw.edite_btn.hide()
        self.cs_dw.del_btn.hide()
        self.cs_dw.details_btn.hide()
        self.cs_dw.showNormal()
        self.cs_dw.raise_()
        self.cs_dw.activateWindow()
        self.cs_dw.nm_edt.setFocus()
        self.clear_course()
    def get_course(self):
        barcode = self.search_edt.text()
        self.barcode = barcode
        if self.barcode:
            self.cs_dw.nm_lbl.setText(self.barcode)
            self.cs_dw.add_btn.hide()
            self.cs_dw.edite_btn.showNormal()
            self.cs_dw.del_btn.showNormal()
            self.cs_dw.details_btn.hide()
            self.cs_dw.showNormal()
            self.cs_dw.activateWindow()
            self.fill_dw()
    def st_sh_edt(self,index):
        row = index.row()
        barcode = self.all_courses.model().get_data(row, 1)
        self.barcode = barcode
        if self.barcode:
            self.cs_dw.nm_lbl.setText(self.barcode)
            self.cs_dw.add_btn.hide()
            self.cs_dw.edite_btn.showNormal()
            self.cs_dw.del_btn.showNormal()
            self.cs_dw.details_btn.showNormal()
            self.cs_dw.showNormal()
            self.cs_dw.activateWindow()
            self.fill_dw()
        else:
            self.dialoge_only(u'لا يوجد دورة',u'اختر المجموعة اولا')
    def del_course(self):
        if self.barcode:
            if self.dialoge_only(u'سيتم حذف المجموعة وكل العمليات المتعلقة بها',u'هل انت متاكد من الحذف') == QMessageBox.Ok:
                self.cs_dw.hide()
                if self.db.delete_course(self.barcode):
                    self.render_all_courses()
                else:
                    self.dialoge_only(u'لم تتم عملية الحذف',u'راجع الاتصال بالشبكة')
        else:
            self.dialoge_only(u'لا يوجد دورة', u'اختر المجموعة اولا')
    def fill_dw(self):
        cs = self.db.get_course_by_name(self.barcode)
        if cs:
            self.cs_dw.nm_lbl.setText(cs[1])
            self.cs_dw.nm_edt.setText(cs[1])
            self.cs_dw.day_spn.setValue(int(cs[2]))
            self.cs_dw.hours_spn.setValue(float(cs[3]))
            self.cs_dw.price_spn.setValue(float(cs[4]))
            self.cs_dw.inst_edt.setText(cs[5])
            self.cs_dw.details_edt.setText(cs[6])
            self.cs_dw.absence.setValue(int(cs[8]))
            self.cs_dw.allow.setValue(float(cs[9]))
            self.cs_dw.allow_before.setValue(float(cs[10]))

            for i in self.cs_dw.findChildren(QRadioButton):
                if i.text() == cs[7]:
                    i.setChecked(True)
    def centerx(self, x):
        frameGm = x.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        x.move(frameGm.topLeft())
    def render_all_courses(self):
        courses = self.db.get_all_courses()
        if courses:
            table_model = MyTableModel(self, courses,
                                       [u'رقم المجموعة',u'الاسم', u'عدد المحاضرات', u'عدد ساعات المحاضرة', u'السعر', u'المحاضر',
                                        u'تفاصيل', u'نظام الدفع',u'ع مرات الغياب',u'وقت السماح',u'وقت السماح قبل المجموعة',u'حذف - تعديل'])
            self.all_courses.setModel(table_model)
            self.all_courses.resizeColumnsToContents()
            table_model.col_num = 11
            table_model.data = table_model.data_col_column
        else:
            self.all_courses.setModel(None)
        self.setFocus()
    def clear_course(self):
        self.cs_dw.nm_lbl.clear()
        self.cs_dw.nm_edt.clear()
        self.cs_dw.day_spn.setValue(0)
        self.cs_dw.hours_spn.setValue(0)
        self.cs_dw.price_spn.setValue(0)
        self.cs_dw.inst_edt.clear()
        self.cs_dw.details_edt.clear()
        self.cs_dw.absence.setValue(0)
        self.cs_dw.allow.setValue(0)
        self.cs_dw.allow_before.setValue(0)
    def add_course(self):
        name = self.cs_dw.nm_edt.text()
        days = self.cs_dw.day_spn.value()
        hours = self.cs_dw.hours_spn.value()
        price = self.cs_dw.price_spn.value()
        inst = self.cs_dw.inst_edt.text()
        absence = self.cs_dw.absence.value()
        allow = self.cs_dw.allow.value()
        allow_before = self.cs_dw.allow_before.value()
        det = self.cs_dw.details_edt.toPlainText()
        t = ''
        for i in self.cs_dw.findChildren(QRadioButton):
            if i.isChecked():
                t = i.text()
        if name:
            if not self.db.get_course_by_name(name):
                if not self.db.add_course(name,days,hours,price,inst,det,t , absence,allow  , allow_before):
                    self.dialoge_only(u'خطأ فى اضافة المجموعة',u'يرجى اعادة ادخال القيم الصحيحة')
                else:
                    self.clear_course()
                    self.cs_dw.hide()
                    self.render_all_courses()
            else:
                self.dialoge_only(u'اسم المجموعة موجود من قبل', u'يرجى ادخال اسم مختلف')
        else:
            self.dialoge_only(u'البيانات غير كاملة',u'ادخل الاسم على الاقل')
    def edite_course(self):
        id_gp = self.cs_dw.nm_lbl.text()
        #old_name = self.cs_dw.nm_lbl.text()
        name = self.cs_dw.nm_edt.text()
        days = self.cs_dw.day_spn.value()
        hours = self.cs_dw.hours_spn.value()
        price = self.cs_dw.price_spn.value()
        inst = self.cs_dw.inst_edt.text()
        absence = self.cs_dw.absence.value()
        allow = self.cs_dw.allow.value()
        allow_before = self.cs_dw.allow_before.value()
        det = self.cs_dw.details_edt.toPlainText()
        t = ''
        for i in self.cs_dw.findChildren(QRadioButton):
            if i.isChecked():
                t = i.text()
        if name:
            if not self.db.edite_course(id_gp,name,days,hours,price,inst,det,t , absence,allow , allow_before):
                self.dialoge_only(u'خطأ فى تحديث المجموعة',u'يرجى اعادة ادخال القيم الصحيحة')
            else:
                self.clear_course()
                self.cs_dw.hide()
                self.render_all_courses()
        else:
            self.dialoge_only(u'البيانات غير كاملة',u'ادخل الاسم على الاقل')
    def dialoge_only(self, x, y):
        msgBox = QMessageBox()
        msgBox.setFixedSize(150, 100)
        msgBox.setWindowTitle(u'تحذير')
        msgBox.setText(unicode(x))
        msgBox.setInformativeText(y)
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        return msgBox.exec_()
class course_info(QWidget, course_info):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.setWindowTitle(u'تفاصيل المجموعة')
        self.gp_id = None
        self.db = Model()
        self.pr = print_doc()
        self.bc_num = bc_num()
        self.special_price=Special_Price()
        self.st_gp_switch = st_gp_switch()
        self.centerx(self.st_gp_switch)
        self.centerx(self.bc_num)
        self.stackedWidget.setCurrentIndex(1)
        self.day_select = day_select_dw()
        self.date_select = date_select()
        self.mony_dw = mony_dw()
        self.st_dw = students_dw()
        self.centerx(self.day_select)
        self.centerx(self.date_select)
        self.centerx(self.mony_dw)
        self.centerx(self.st_dw)
        self.start_dt.setDate(datetime.date.today())
        self.date_select.date_edt.setDate(datetime.date.today())
        for i in self.findChildren(QWidget):
            i.setAttribute(Qt.WA_StyledBackground, True)
        self.attend_btn.clicked.connect(self.times_f)
        self.course_time_finish_btn.clicked.connect(self.course_time_finish)
        self.course_time_btn.clicked.connect(self.course_time)
        self.date_select.add_btn.clicked.connect(self.add_course_time)
        self.day_select.add_btn.clicked.connect(self.add_course_time_st)
        self.add_btn_dates.clicked.connect(self.date_select_show)
        self.add_btn_days.clicked.connect(self.day_select_show)
        self.finish_days.clicked.connect(self.convert_days_to_dates)
        self.students_btn.clicked.connect(self.get_st_cs)
        self.st_edt_2.returnPressed.connect(self.get_st)
        self.st_attend_btn.clicked.connect(self.show_st_attend)
        self.st_attend_search_btn.clicked.connect(self.fill_st_attend)
        self.attend_day.currentIndexChanged.connect(self.fill_st_attend)
        self.bill_search_btn.clicked.connect(self.fill_st_mony)
        self.bill_day.currentIndexChanged.connect(self.fill_st_mony)
        self.bill_print_btn.clicked.connect(self.print_mony)
        self.st_attend_print_btn.clicked.connect(self.print_attend)
        self.mony_btn.clicked.connect(self.get_mony)
        self.table_dates.cellClicked.connect(self.del_course_time)
        self.table_days.cellClicked.connect(self.del_course_time_st)
        self.st_cs_table.cellClicked.connect(self.del_st_cs)
        self.bill_table.cellClicked.connect(self.buy_mony)
        self.mony_dw.put_mony_btn.clicked.connect(self.buy_mony_db)
        self.st_dw.add_btn.clicked.connect(self.add_st)
        self.add_student_btn.clicked.connect(self.add_incurrent)
        self.date_select.edt_btn.clicked.connect(self.edite_time)
        self.st_dw.barcode_get_btn.clicked.connect(lambda: self.st_dw.bc_edt.setText(self.db.generate_barcode()))
        self.connect(self.st_attend_table, SIGNAL("doubleClicked(const QModelIndex&)"), self.change_st_status)
        self.print_btn.clicked.connect(lambda :self.bc_num.pre_show(self.get_data()))
        self.st_gp_switch.pushButton.clicked.connect(self.switch)
        self.sw_btn.clicked.connect(self.show_sw)
        self.all_rd.clicked.connect(self.fill_st_attend)
        self.attend_rd.clicked.connect(self.fill_st_attend)
        self.absent_rd.clicked.connect(self.fill_st_attend)
        self.att_btn.clicked.connect(lambda: self.attend_abs_all(True))
        self.abs_btn.clicked.connect(lambda: self.attend_abs_all(False))
        self.print_students.clicked.connect(self.print_f)
        self.special_price.add_btn.clicked.connect(self.update_price)
        self.special_price.close_btn.clicked.connect(self.special_price.close)

    def print_f(self):
        x=[]
        hea=[]
        for i in range(3):
                hea.append(self.st_cs_table.horizontalHeaderItem(i).text())
        x.append(hea)
        for m in range(self.st_cs_table.rowCount()):
            z=[]
            for j in range(3):
                    teext = unicode(self.st_cs_table.item(m, j).text())
                    z.append(teext)
            x.append(z)
        self.pr.print_info(x, u'تقرير الطالب')


    def focusInEvent(self, *args, **kwargs):
        indx = self.stackedWidget.currentIndex()
        if indx == 0:
            self.get_course_times()
        elif indx == 1:
            self.get_st_cs()
        elif indx == 2:
            self.fill_st_attend()
        elif indx == 3:
            self.fill_st_mony()
        self.completer_set()
    def show_sw(self):
        self.st_gp_switch.st_bc = 'all'
        self.st_gp_switch.showNormal()
        self.st_gp_switch.raise_()
        self.st_gp_switch.activateWindow()
        self.st_gp_switch.label_3.setText(self.gp_id)
        self.st_gp_switch.comboBox.clear()
        for i in self.db.get_all_courses():
            if i[1] != self.gp_id:
                self.st_gp_switch.comboBox.addItem(i[1])
    def switch(self):
        if self.st_gp_switch.st_bc == 'all':
            for i in self.db.get_all_stu(self.gp_id):
                self.db.student_group_swift(i[0],self.st_gp_switch.label_3.text(),self.st_gp_switch.comboBox.currentText())
            self.get_st_cs()
            self.st_gp_switch.hide()
        else:
            if self.db.student_group_swift(self.st_gp_switch.st_bc, self.st_gp_switch.label_3.text(),
                                           self.st_gp_switch.comboBox.currentText()):
                self.get_st_cs()
                self.st_gp_switch.hide()
    def get_data(self):
        l =[]
        for  i in range(self.st_cs_table.rowCount()):
            l.append([self.st_cs_table.item(i,2).text(),self.st_cs_table.item(i,1).text()])
        return l
    def color_btn(self):
        if type(self.sender()) is QPushButton:
            try:
                for i in self.widget_4.findChildren(QPushButton):
                    i.setStyleSheet("background:#05B963;")
                self.sender().setStyleSheet("background:#A8B1B2;")
            except:
                self.students_btn.setStyleSheet("background:#A8B1B2;")

    def set_cs_id(self,gp_id):
        self.gp_id = gp_id
    def add_incurrent(self):
        self.st_dw.edite_btn.hide()
        self.st_dw.showNormal()
    def day_select_show(self):
        self.day_select.showNormal()
        self.day_select.activateWindow()
        self.day_select.raise_()
    def date_select_show(self):
        self.date_select.add_btn.show()
        self.date_select.edt_btn.hide()
        self.date_select.showNormal()
        self.date_select.activateWindow()
        self.date_select.raise_()
    def get_mony(self):
        self.color_btn()
        if self.gp_id:
            self.stackedWidget.setCurrentIndex(3)
            self.get_mony_id()
        else:
            self.dialoge_only(u'لا يوجد اسم', u'ادخل الاسم اولا')
    def fill_st_mony(self):
        mony_id = self.bill_day.currentText()
        tottal = 0
        baid = 0
        if mony_id:
            x = self.db.get_st_cs(self.gp_id)
            self.bill_table.setRowCount(0)
            if x:
                for i in x:
                    n = self.bill_table.rowCount()
                    self.bill_table.insertRow(n)
                    self.bill_table.setItem(n, 0, QTableWidgetItem(i[0]))
                    self.bill_table.setItem(n, 1, QTableWidgetItem(i[1]))
                    self.bill_table.setItem(n, 2, QTableWidgetItem(i[2]))
                    self.bill_table.setItem(n, 3, QTableWidgetItem(unicode(i[3])))
                    x = self.db.get_st_mony(i[2],self.gp_id,mony_id)
                    self.bill_table.setItem(n, 4, QTableWidgetItem(unicode(x)))
                    self.bill_table.setItem(n, 5, QTableWidgetItem(unicode(i[3]-x)))
                    self.bill_table.setItem(n, 6, QTableWidgetItem(u'دفع'))
                    self.bill_table.item(n, 6).setBackground(QColor(20, 200, 10))
                    tottal += i[3]
                    baid += x
                self.tottal.setText(unicode(tottal))
                self.baid.setText(unicode(baid))
                self.rest.setText(unicode(tottal-baid))
            else:
                self.bill_table.setRowCount(0)
                self.tottal.setText("0")
                self.baid.setText("0")
                self.rest.setText("0")
    def fill_st_attend(self):
        if self.attend_day.currentText():
            x = self.db.get_st_cs(self.gp_id)
            self.st_attend_table.setRowCount(0)
            info = self.attend_day.currentText().split(" : ")
            if x:
                for i in x:
                    checked = self.db.check_attend(i[2],info[0],info[1],info[2])
                    if self.all_rd.isChecked():
                        self.tbl_checked_add(i,checked)
                    elif self.attend_rd.isChecked() and checked:
                        self.tbl_checked_add(i,checked)
                    elif self.absent_rd.isChecked() and not checked:
                        self.tbl_checked_add(i, checked)
    def tbl_checked_add(self,i,checked):
        n = self.st_attend_table.rowCount()
        self.st_attend_table.insertRow(n)
        self.st_attend_table.setItem(n, 0, QTableWidgetItem(i[0]))
        self.st_attend_table.setItem(n, 1, QTableWidgetItem(i[1]))
        self.st_attend_table.setItem(n, 2, QTableWidgetItem(i[2]))
        if checked:
            self.st_attend_table.setItem(n, 3, QTableWidgetItem(u'حاضر'))
        else:
            self.st_attend_table.setItem(n, 3, QTableWidgetItem(u'غائب'))
    def attend_abs_all(self,attend):
        if self.dialoge_only(u'هل انت متاكد من هذة العملية',u'سيتم تغير حالة الطلاب الحاليين فى هذا اليوم') == QMessageBox.Ok:
            info = self.attend_day.currentText().split(" : ")
            for col in range(self.st_attend_table.rowCount()):
                st = self.st_attend_table.item(col, 2).text()
                dt_st = self.st_attend_table.item(col, 3).text()
                gpid = self.db.get_course_by_name(self.gp_id)[0]
                if attend:
                    self.db.attend_st_gp(st, gpid, info[0], info[1], info[2], u'حضور')
                    self.st_attend_table.setItem(col, 3, QTableWidgetItem(u'حاضر'))
                else:
                    self.db.attend_st_gp(st, gpid, info[0], info[1], info[2], u'غياب')
                    self.st_attend_table.setItem(col, 3, QTableWidgetItem(u'غائب'))
    def change_st_status(self,indx):
        col = indx.row()
        st = self.st_attend_table.item(col,2).text()
        info = self.attend_day.currentText().split(" : ")
        dt_st = self.st_attend_table.item(col,3).text()
        gpid = self.db.get_course_by_name(self.gp_id)[0]
        if dt_st == u'غائب':
            if self.db.attend_st_gp(st,gpid,info[0],info[1],info[2],u'حضور'):
                self.st_attend_table.setItem(col, 3, QTableWidgetItem(u'حاضر'))
        else:
            if self.db.attend_st_gp(st,gpid,info[0],info[1],info[2],u'غياب'):
                self.st_attend_table.setItem(col, 3, QTableWidgetItem(u'غائب'))

    def show_st_attend(self):
        self.color_btn()
        bill = []
        back = []
        index = []
        today = datetime.date.today()
        if self.gp_id:
            self.stackedWidget.setCurrentIndex(2)
            v = self.db.get_course_dates(self.gp_id)
            self.attend_day.clear()
            for i in v:
                self.attend_day.addItem(str(i[0])+" : "+str(i[1])+" : "+str(i[2]))
                bill.append(i[0])
            if v:
                self.fill_st_attend()
            if bill:
                for i in bill:
                    if (i <= today ) :
                        diff = today - i
                        back.append(diff)
                        index.append(bill.index(i))

                target = min(back)
                inx = back.index(target)
                final = bill[inx]
                self.attend_day.setCurrentIndex(inx)
        else:
            self.dialoge_only(u'لا يوجد اسم', u'ادخل الاسم اولا')
    def get_st(self):
        st = self.st_edt_2.text()
        self.st_edt_2.clear()
        if st:
            barcode = self.db.get_student(st) #select * from student
            if barcode:
                course = self.gp_id
                price = self.db.get_course_price(self.gp_id)
                if self.db.st_gp_not_exist(barcode[0], course):
                    if self.db.add_st_gp(barcode[0], course,price):
                        self.get_st_cs()
                        self.st_edt_2.selectAll()
                    else:
                        self.dialoge_only(u'لم تتم عملية الاضافة بنجاح', u'حاول مرة اخرى')
                else:
                    self.dialoge_only(u'الطالب موجود فى المجموعة بالفعل', u'اختر مجموعة اخرى')

            else:
                self.dialoge_only(u'لا توجد بيانات لهذا المتدرب', u'ادخل الاسم الصحيح')

    def convert_days_to_dates(self):
        self.get_times_from_structure()
        self.course_time_finish()
    def get_times_from_structure(self):
        if self.dialoge_only(u'سيتم حذف المواعيد الاخرى واضافة مواعيد جديدة', u'هل انت متاكد من الحذف') == QMessageBox.Ok:
            if self.db.del_course_time_all(self.gp_id):
                st_date = self.start_dt.date().toPython()
                structures = self.db.get_course_structure(self.gp_id)
                num_days = self.db.get_course_num_days(self.gp_id)
                rest_days = 0
                while rest_days < num_days:
                    day = st_date.strftime('%A')
                    for i in structures:
                        if i[1] == day and rest_days < num_days:
                            self.db.add_course_time(self.gp_id, st_date, day, i[2], i[3])
                            rest_days += 1
                    try:
                        st_date = st_date + datetime.timedelta(days=1)
                    except:
                        pass
            else:
                self.dialoge_only(u'لم تتم عملية حذف المواعيد',u'لنن تتم عملية تغير المواعيد')
    def completer_set(self):
        completer2 = QCompleter()
        completer2.setCompletionMode(QCompleter.PopupCompletion)
        completer2.activated.connect(self.get_st)
        m = QStringListModel()
        completer2.setModel(m)
        self.db.get_students(m)
        self.st_edt_2.setCompleter(completer2)
    def times_f(self):
        self.course_time()
        self.color_btn()
        if self.gp_id:
            self.stackedWidget.setCurrentIndex(0)
            self.get_course_times_structure()
            self.fill_days()
        else:
            self.dialoge_only(u'لا يوجد دورة',u'اختر دورة اولا')
    def add_course_time_st(self):
        d = self.day_select.day_cmb.currentText()
        st = self.day_select.t1.time().toString("hh:mm:ss")
        end = self.day_select.t2.time().toString("hh:mm:ss")
        if self.db.add_course_time_structure(self.gp_id,d,st,end):
            self.get_course_times_structure()
            self.day_select.hide()
    def add_course_time(self):
        d = self.date_select.date_edt.date().toString("yyyy-MM-dd")
        day = self.date_select.date_edt.date().toPython().strftime("%A")
        st = self.date_select.t1.time().toString("hh:mm:ss")
        end = self.date_select.t2.time().toString("hh:mm:ss")
        if self.db.add_course_time(self.gp_id,d,day,st,end):
            self.get_course_times()
            self.date_select.hide()
    def get_course_times_structure(self):
        x = self.db.get_course_structure(self.gp_id)
        self.table_days.setRowCount(0)
        for i in x:
            n = self.table_days.rowCount()
            self.table_days.insertRow(n)
            self.table_days.setItem(n, 0, QTableWidgetItem(unicode(i[1])))
            self.table_days.setItem(n, 1, QTableWidgetItem(unicode(i[2])))
            self.table_days.setItem(n, 2, QTableWidgetItem(unicode(i[3])))
            self.table_days.setItem(n, 3, QTableWidgetItem(u'حذف'))
            self.table_days.item(n, 3).setBackground(QColor(231, 76, 62))
    def fill_days(self):
        self.day_select.day_cmb.clear()
        self.day_select.day_cmb.addItems(['Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday'])
    def get_course_times(self):
        x = self.db.get_course(self.gp_id)
        self.table_dates.setRowCount(0)
        if x:
            for i in x:
                n = self.table_dates.rowCount()
                self.table_dates.insertRow(n)
                xx = QTableWidgetItem(unicode(i[2]))
                xx.setStatusTip(unicode(i[0]))
                self.table_dates.setItem(n, 0, xx)
                self.table_dates.setItem(n, 1, QTableWidgetItem(unicode(i[3])))
                self.table_dates.setItem(n, 2, QTableWidgetItem(unicode(i[4])))
                self.table_dates.setItem(n, 3, QTableWidgetItem(unicode(i[5])))
                self.table_dates.setItem(n, 4, QTableWidgetItem(u'حذف'))
                self.table_dates.setItem(n, 5, QTableWidgetItem(u'تعديل'))
                self.table_dates.item(n, 4).setBackground(QColor(231, 76, 62))
                self.table_dates.item(n, 5).setBackground(QColor(45, 136, 45))
        db = Model()
        db.th_course()
    def buy_mony(self, row, column):
        if column == 6:
            self.mony_dw.showNormal()
            self.mony_dw.activateWindow()
            self.mony_dw.raise_()
            self.mony_dw.name_lbl.setText(self.bill_table.item(row, 0).text())
            self.mony_dw.phone_lbl.setText(self.bill_table.item(row, 1).text())
            self.mony_dw.barcode_lbl.setText(self.bill_table.item(row, 2).text())
            index = self.mony_dw.mid.findText(self.bill_day.currentText(), Qt.MatchFixedString)
            if index >= 0:
                self.mony_dw.mid.setCurrentIndex(index)
            self.mony_dw.gp_lbl.setText(self.gp_id)
            self.mony_dw.tottal_lbl.setText(self.bill_table.item(row, 3).text())
            self.mony_dw.baid_spn.setRange(0, float(self.bill_table.item(row, 5).text()))
            self.mony_dw.baid_spn.setValue(float(self.bill_table.item(row, 5).text()))
    def del_course_time_st(self,row, column):
        if column == 3:
            if self.dialoge_only(u'سيتم حذف معاد هذة المجموعة', u'هل انت متاكد من الحذف') == QMessageBox.Ok:
                if self.db.del_course_time_st(self.gp_id,self.table_days.item(row,0).text(), self.table_days.item(row,1).text(), self.table_days.item(row,2).text()):
                    self.get_course_times_structure()
    def del_course_time(self,row, column):
        if column == 4:
            self.del_course_time_func(self.gp_id, self.table_dates.item(row,0).text(), self.table_dates.item(row,2).text(), self.table_dates.item(row,3).text())
        elif column == 5:
            self.date_select.date_id = self.table_dates.item(row,0).statusTip()
            self.date_select.edt_btn.show()
            self.date_select.add_btn.hide()
            self.date_select.showNormal()
            info = self.db.get_time_by_id(self.date_select.date_id)
            if info:
                self.date_select.date_edt.setDate(info[2])
                self.date_select.t1.setTime((datetime.datetime.min + info[4]).time())
                self.date_select.t2.setTime((datetime.datetime.min + info[5]).time())
    def edite_time(self):
        dt = self.date_select.date_edt.date().toPython()
        t1 = self.date_select.t1.time().toString("hh:mm:ss")
        t2 = self.date_select.t2.time().toString("hh:mm:ss")
        self.db.edt_time_course(self.date_select.date_id,dt,t1,t2)
        self.get_course_times()
        self.date_select.hide()
    def del_course_time_func(self,course,date,t1,t2):
        if self.dialoge_only(u'سيتم حذف معاد هذة المجموعة', u'هل انت متاكد من الحذف') == QMessageBox.Ok:
            if self.db.del_course_time(course,date,t1,t2):
                self.get_course_times()
    def course_time(self):
        self.stackedWidget_2.setCurrentIndex(1)
        self.get_course_times_structure()
        self.stackedWidget_2.setStyleSheet('.QWidget{background:#35485F;color:#fff;}.QLabel{color:#fff;}.QPushButton{color:#fff;}')
        self.widget_7.setStyleSheet('.QWidget{background:#35485F;color:#fff;}.QLabel{color:#fff;}.QPushButton{color:#fff;}')
    def course_time_finish(self):
        self.stackedWidget_2.setCurrentIndex(0)
        self.get_course_times()
        self.stackedWidget_2.setStyleSheet('.QWidget{background:#09C18D;color:#fff;}.QLabel{color:#fff;}.QPushButton{color:#fff;}')
        self.widget_7.setStyleSheet('.QWidget{background:#09C18D;color:#fff;}.QLabel{color:#fff;}.QPushButton{color:#fff;}')
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
    def get_course(self):
        name = self.search_edt.text()
        if name:
            self.get_course_fill(name)
        else:
            self.dialoge_only(u'لا يوجد اسم',u'ادخل الاسم اولا')
    def get_course_fill(self,name):
        info = self.db.get_course_by_name(name)
        if info:
            self.id_lbl.setText(unicode(info[0]))

            self.name_lbl.setText(unicode(info[1]))
            self.course_name.setText(unicode(info[1]))
            self.days_lbl.setText(unicode(info[2]))
            self.course_days.setText(unicode(info[2]))
            self.hours_lbl.setText(unicode(info[3]))
            self.course_hours.setText(unicode(info[3]))
            self.price_lbl.setText(unicode(info[4]))
            self.inst_lbl.setText(unicode(info[5]))
            self.course_inst.setText(unicode(info[5]))
            self.details_lbl.setText(unicode(info[6]))
            self.bill_method.setText(unicode(info[7]))
            self.absence_lbl.setText(unicode(info[8]))
            self.allow_lbl.setText(unicode(info[9]))
            self.allow_lbl_2.setText(unicode(info[10]))

            self.get_course_times_structure()
        else:
            self.dialoge_only(u'لا توجد بيانات لهذة المجموعة', u'ادخل الاسم الصحيح')
    def get_st_cs(self):
        self.color_btn()
        if self.gp_id:
            self.stackedWidget.setCurrentIndex(1)
            x = self.db.get_st_cs(self.gp_id)
            self.st_cs_table.setRowCount(0)
            if x:
                for i in x:
                    n = self.st_cs_table.rowCount()
                    self.st_cs_table.insertRow(n)
                    self.st_cs_table.setItem(n, 0, QTableWidgetItem(i[0]))
                    self.st_cs_table.setItem(n, 1, QTableWidgetItem(i[1]))
                    self.st_cs_table.setItem(n, 2, QTableWidgetItem(i[2]))
                    self.st_cs_table.setItem(n,3,QTableWidgetItem(str(i[3])))
                    self.st_cs_table.setItem(n, 4, QTableWidgetItem(u'حذف'))
                    self.st_cs_table.item(n, 4).setBackground(QColor(231, 76, 62))
                    self.st_cs_table.setItem(n, 5, QTableWidgetItem(u'طباعة'))
                    self.st_cs_table.item(n, 5).setBackground(QColor(136, 45, 136))
                    self.st_cs_table.setItem(n, 6, QTableWidgetItem(u'نقل'))
                    self.st_cs_table.item(n, 6).setBackground(QColor(45, 150, 45))
        else:
            self.dialoge_only(u'لا يوجد دورة', u'اختر دورة اولا')
    def del_st_cs(self, row, column):
        if column == 4:
            if self.dialoge_only(u'سيتم حذف الطالب من هذة المجموعة', u'هل انت متاكد من الحذف') == QMessageBox.Ok:
                if self.db.del_st_cs(self.st_cs_table.item(row,2).text(),self.gp_id):
                    self.get_st_cs()
                else:
                    self.dialoge_only(u'لم تتم عملية الحذف', u'راجع الاتصال بالشبكة')
        elif column == 5:
            self.bc_num.pre_show([[self.st_cs_table.item(row,2).text(),self.st_cs_table.item(row,0).text()]])
        elif column == 6:
            self.st_gp_switch.st_bc = self.st_cs_table.item(row,2).text()
            self.st_gp_switch.showNormal()
            self.st_gp_switch.raise_()
            self.st_gp_switch.activateWindow()
            self.st_gp_switch.label_3.setText(self.gp_id)
            self.st_gp_switch.comboBox.clear()
            for i in self.db.get_all_courses():
                if i[1] != self.gp_id:
                    self.st_gp_switch.comboBox.addItem(i[1])
        elif column==3:
            self.special_price.show()
            self.special_price.raise_()
            self.special_price.activateWindow()
            self.barcode = self.st_cs_table.item(row,2).text()
    def update_price(self):
        new_price=self.special_price.price_spn.value()
        self.db.edite_price(new_price,self.gp_id,self.barcode)
        self.get_st_cs()
        self.special_price.close()


    def print_attend(self):
        course = self.cmb.text()
        day = self.attend_day.currentText()
        if course and day:
            self.pr.print_attend(self.get_data_attend(),course,day)
        else:
            self.dialoge_only(u'لا يوجد بيانات للطباعة',u'راجع بيانات البحث')
    def print_mony(self):
        course = self.gp_id
        day = self.bill_day.currentText()
        tottal = self.tottal.text()
        baid = self.baid.text()
        rest = self.rest.text()
        if course and day:
            self.pr.print_attend(self.get_data_attend(),course,day,tottal,baid,rest)
        else:
            self.dialoge_only(u'لا يوجد بيانات للطباعة',u'راجع بيانات البحث')
    def get_data_attend(self):
        s = []
        a = []
        n = self.st_attend_table.columnCount()
        for i in range(n):
            s.append(self.st_attend_table.horizontalHeaderItem(i).text())
        a.append(s)
        x = self.st_attend_table.rowCount()
        for i in range(x):
            s = []
            for j in range(n):
                s.append(self.st_attend_table.item(i,j).text())
            a.append(s)
        return a
    def get_data_mony(self):
        s = []
        a = []
        n = self.bill_table.columnCount()
        for i in range(n):
            s.append(self.bill_table.horizontalHeaderItem(i).text())
        a.append(s)
        x = self.bill_table.rowCount()
        for i in range(x):
            s = []
            for j in range(n):
                s.append(self.bill_table.item(i,j).text())
            a.append(s)
        return a
    def buy_mony_db(self):
        if self.db.put_st_mony(self.mony_dw.barcode_lbl.text(),self.mony_dw.gp_lbl.text(),self.db.get_method_price(self.mony_dw.gp_lbl.text())[0],self.mony_dw.mid.currentText(),self.mony_dw.baid_spn.value()):
            self.mony_dw.hide()
            self.get_mony()
    def get_mony_id(self):
        c = 0
        indx = 0
        course_name = self.db.get_course_bill(self.gp_id)  #method of payment
        if course_name == u'بالحصة':
            v = self.db.get_course_days(self.gp_id)
            self.bill_day.clear()
            d = datetime.date.today()
            self.mony_dw.mid.clear()
            for i in v:
                if d == i[0]:
                    indx = c
                c += 1
                self.bill_day.addItem(str(i[0]) + " : " + str(i[1]) + " : " + str(i[2]))
                self.mony_dw.mid.addItem(str(i[0]) + " : " + str(i[1]) + " : " + str(i[2]))
            self.bill_day.setCurrentIndex(indx)
        elif course_name == u'بالشهر':
            v = self.db.get_course_months(self.gp_id)  #get dates of course
            self.bill_day.clear()
            self.mony_dw.mid.clear()
            self.bill_day.addItems(v)
            self.mony_dw.mid.addItems(v)
            d = datetime.date.today()
            indx = self.bill_day.findText(unicode(d.month) + " - " + unicode(d.year))
            if indx >= 0:
                self.bill_day.setCurrentIndex(indx)
            else:
                self.bill_day.setCurrentIndex(0)
        else:
            self.bill_day.clear()
            self.mony_dw.mid.clear()
            self.bill_day.addItem(self.gp_id)
            self.mony_dw.mid.addItem(self.gp_id)

    def add_st(self):
        barcode = self.st_dw.bc_edt.text()
        nm = self.st_dw.nm_edt.text()
        school = self.st_dw.school_edt.text()
        sph = self.st_dw.ph_edt.text()
        fph = self.st_dw.fphon_edt.text()
        add = self.st_dw.address_edt.text()
        mail = self.st_dw.mail_edt.text()
        det = self.st_dw.details_edt.toPlainText()
        if barcode and nm:
            s_exist = self.db.student_exist(barcode, nm)  #checking the existance of student.  if it exist it will return 2 or 3 and if  it does not exist it will return 1
            if s_exist == 1:  #this is mean that the student does not exist
                if not self.db.add_student(barcode,nm,school,sph,fph,mail,add,det): #insert student info in student table
                    self.dialoge_only(u'خطأ فى اضافة الطالب',u'يرجى اعادة ادخال القيم الصحيحة')
                else:
                    self.get_st_current(barcode)
                    self.clear_st()
                    self.st_dw.hide()
            elif s_exist == 2:
                self.dialoge_only(u'الباركود موجود من قبل', u'راجع البيانات وادخل بيانات جديدة')
            elif s_exist == 3:
                self.dialoge_only(u'الاسم موجود من قبل', u'راجع البيانات وادخل بيانات جديدة')
        else:
            self.dialoge_only(u'البيانات غير كاملة', u'ادخل الاسم والباركود على الاقل')
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
    def get_st_current(self ,st ):
        if st:
            barcode = self.db.get_student(st)  #select student info from student table by brcode
            if barcode:
                course = self.gp_id
                price=self.db.get_course_price(course)
                if self.db.st_gp_not_exist(barcode[0], course):
                    if self.db.add_st_gp(barcode[0], course,price):
                        self.get_st_cs()
                        self.st_edt_2.selectAll()
                    else:
                        self.dialoge_only(u'لم تتم عملية الاضافة بنجاح', u'حاول مرة اخرى')
                else:
                    self.dialoge_only(u'الطالب موجود فى المجموعة بالفعل', u'اختر مجموعة اخرى')

            else:
                self.dialoge_only(u'لا توجد بيانات لهذا المتدرب', u'ادخل الاسم الصحيح')
        else:
            self.dialoge_only(u'لا يوجد اسم',u'ادخل الاسم اولا')