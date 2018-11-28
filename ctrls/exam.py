# -*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
from model.Model import Model
import datetime
import sys
from model.table_model import MyTableModel
from printing import print_doc
from views.exam_info import Ui_Form as exam_info
from views.exam_add import Ui_Form as exam
from views.exam_dw import Ui_Form as exam_dw
from views.day_select_dw import Ui_Form as day_select_dw
from views.date_select import Ui_Form as date_select
from views.degree_dw import Ui_Form as degree_dw
class degree_dw(QWidget, degree_dw):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle(u'الدرجات')
        self.setupUi(self)
        for i in self.findChildren(QWidget):
            i.setAttribute(Qt.WA_StyledBackground, True)
class exam_dw(QWidget, exam_dw):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.setWindowTitle(u'الاختبار')
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
        self.setWindowTitle(u'اختر يوما')
        for i in self.findChildren(QWidget):
            i.setAttribute(Qt.WA_StyledBackground, True)
class exam(QWidget, exam):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.exam_name = None
        self.ex_dw = exam_dw()
        self.exam_info = exam_info()
        self.db = Model()
        self.search_edt.setFocus()
        self.centerx(self.ex_dw)
        self.centerx(self.exam_info)
        self.add_btn.clicked.connect(self.st_sh_add)
        self.ex_dw.nm_lbl.hide()
        self.connect(self.tableView, SIGNAL("doubleClicked(const QModelIndex&)"), self.sh_exam)
        self.connect(self.tableView, SIGNAL("clicked(const QModelIndex&)"), self.st_sh_edt)
        self.ex_dw.add_btn.clicked.connect(self.add_exam)
        self.ex_dw.edite_btn.clicked.connect(self.edite_exam)
        self.ex_dw.del_btn.clicked.connect(self.del_exam)
        for i in self.ex_dw.findChildren(QSpinBox):
            i.setRange(0,100000)
        for i in self.ex_dw.findChildren(QDoubleSpinBox):
            i.setRange(0,sys.float_info.max)
        self.search_edt.returnPressed.connect(self.get_exam)
    def focusInEvent(self, *args, **kwargs):
        self.completer_set()
    def sh_exam(self,index):
        row = index.row()
        exam_name = self.tableView.model().get_data(row, 0)
        self.exam_name = exam_name
        if self.exam_name:
            self.exam_info.showNormal()
            self.exam_info.raise_()
            self.exam_info.activateWindow()
            self.exam_info.set_ex_id(self.exam_name)
            self.exam_info.get_exam_gps()
            self.exam_info.stackedWidget.setCurrentIndex(1)
    def add_exam(self):
        name = self.ex_dw.nm_edt.text()
        days = self.ex_dw.day_spn.value()
        hours = self.ex_dw.hours_spn.value()
        max_degree = self.ex_dw.max_spn.value()
        det = self.ex_dw.details_edt.toPlainText()
        if self.ex_dw.class_rd.isChecked():
            type = u'دورى'
        if self.ex_dw.month_rd.isChecked():
            type = u'شهرى'
        if name:
            if not self.db.add_exam(name,days,hours,max_degree,det ,type ):
                self.dialoge_only(u'خطأ فى اضافة الدورة',u'يرجى اعادة ادخال القيم الصحيحة')
            else:
                self.clear_exam()
                self.ex_dw.hide()
                self.render_all_exmas()
        else:
            self.dialoge_only(u'البيانات غير كاملة',u'ادخل الاسم على الاقل')
    def completer_set(self):
        completer = QCompleter()
        completer.setCompletionMode(QCompleter.PopupCompletion)
        completer.activated.connect(self.get_exam)
        model = QStringListModel()
        completer.setModel(model)
        self.db.get_exams(model)
        self.search_edt.setCompleter(completer)
        self.render_all_exmas()
    def get_exam(self):
        self.search_edt.selectAll()
        name = self.search_edt.text()
        self.show_edt(name)

    def st_sh_add(self):
        self.ex_dw.add_btn.show()
        self.ex_dw.edite_btn.hide()
        self.ex_dw.details_btn.hide()
        self.ex_dw.del_btn.hide()
        self.ex_dw.show()
        self.ex_dw.activateWindow()
        self.ex_dw.raise_()
        self.ex_dw.nm_edt.setFocus()
        self.clear_exam()
        '''out = self.db.get_all_gp()
        for i in out:
            self.ex_dw.gp_name.addItem(i[0])'''
    def st_sh_edt(self,index):
        if index.column() == 6:
            row = index.row()
            exam_name = self.tableView.model().get_data(row, 0)
            self.show_edt(exam_name)
    def show_edt(self,exam_name):
            self.exam_name = exam_name
            if self.exam_name:
                self.ex_dw.nm_lbl.setText(self.exam_name)
                self.ex_dw.add_btn.hide()
                self.ex_dw.details_btn.hide()
                self.ex_dw.edite_btn.show()
                self.ex_dw.del_btn.show()
                self.ex_dw.show()
                self.fill_dw()
            else:
                self.dialoge_only(u'لا يوجد اسم',u'اختر اسم اولا')
    def del_exam(self):
        if self.exam_name:
            if self.dialoge_only(u'سيتم حذف الدورة وكل العمليات المتعلقة بها',u'هل انت متاكد من الحذف') == QMessageBox.Ok:
                if self.db.delete_exam(self.exam_name):
                    #self.clear_exam_w()
                    self.render_all_exmas()
                    self.ex_dw.close()
                else:
                    self.dialoge_only(u'لم تتم عملية الحذف',u'راجع الاتصال بالشبكة')
        else:
            self.dialoge_only(u'لا يوجد اسم', u'اختر اسم اولا')
    def render_all_exmas(self):
        exams = self.db.get_all_exams()
        if exams:
            table_model = MyTableModel(self, exams,
                                       [u'الاسم',u'عدد الايام', u'عدد الساعات', u'الدرجة العظمى', u'تفاصيل',u'نوع الاختبار',u'حذف - تعديل'])
            self.tableView.setModel(table_model)
            self.tableView.resizeColumnsToContents()
            table_model.col_num = 6
            table_model.data = table_model.data_col_column
        else:
            self.tableView.setModel(None)
        self.setFocus()
    def fill_dw(self):
        exam = self.db.get_exam_by_name(self.exam_name)
        self.ex_dw.nm_lbl.setText(exam[0])
        self.ex_dw.nm_edt.setText(exam[0])
        self.ex_dw.day_spn.setValue(exam[1])
        self.ex_dw.hours_spn.setValue(exam[2])
        self.ex_dw.max_spn.setValue(exam[3])
        self.ex_dw.details_edt.setText(exam[4])
        for i in self.ex_dw.findChildren(QRadioButton):
            if i.text() == exam[5]:
                i.setChecked(True)
    def clear_exam(self):
        self.ex_dw.nm_lbl.clear()
        self.ex_dw.nm_edt.clear()
        self.ex_dw.day_spn.setValue(0)
        self.ex_dw.hours_spn.setValue(0)
        self.ex_dw.max_spn.setValue(0)
        self.ex_dw.details_edt.clear()
    def edite_exam(self):
        old_name = self.ex_dw.nm_lbl.text()
        name = self.ex_dw.nm_edt.text()
        days = self.ex_dw.day_spn.value()
        hours = self.ex_dw.hours_spn.value()
        max_degree = self.ex_dw.max_spn.value()
        det = self.ex_dw.details_edt.toPlainText()
        if self.ex_dw.class_rd.isChecked():
            type = u'دورى'
        if self.ex_dw.month_rd.isChecked():
            type = u'شهرى'
        if name:
            if not self.db.edite_exam(old_name,name,days,hours,max_degree,det , type ):
                self.dialoge_only(u'خطأ فى تحديث الدورة',u'يرجى اعادة ادخال القيم الصحيحة')
            else:
                self.clear_exam()
                self.ex_dw.hide()
                self.render_all_exmas()
        else:
            self.dialoge_only(u'البيانات غير كاملة',u'ادخل الاسم على الاقل')
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
class exam_info(QWidget, exam_info):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.setWindowTitle(u'تفاصيل الاختبار')
        self.db = Model()
        self.pr = print_doc()
        self.day_select = day_select_dw()
        self.date_select = date_select()
        self.degree_dw = degree_dw()
        self.centerx(self.degree_dw)
        self.centerx(self.day_select)
        self.centerx(self.date_select)
        self.completer_set_gps()
        self.start_dt.setDate(datetime.date.today())
        self.date_select.date_edt.setDate(datetime.date.today())
        for i in self.findChildren(QWidget):
            i.setAttribute(Qt.WA_StyledBackground, True)
        self.attend_btn.clicked.connect(self.times_f)
        self.course_time_finish_btn.clicked.connect(self.exam_time_finish)
        self.course_time_btn.clicked.connect(self.exam_time)
        self.date_select.add_btn.clicked.connect(self.add_exam_time)
        self.day_select.add_btn.clicked.connect(self.add_exam_time_st)
        self.add_btn_dates.clicked.connect(self.date_select_show)
        self.add_btn_days.clicked.connect(self.day_select_show)
        self.finish_days.clicked.connect(self.convert_days_to_dates)
        self.gps_btn.clicked.connect(self.get_exam_gps)
        self.st_attend_btn.clicked.connect(self.show_st_attend)
        self.st_attend_search_btn.clicked.connect(self.fill_st_attend)
        self.exam_day.currentIndexChanged.connect(self.fill_st_attend)
        #self.st_attend_print_btn.clicked.connect(self.print_attend)
        self.stackedWidget_2.setStyleSheet('.QWidget{background:#35485F;color:#fff;}.QLabel{color:#fff;}.QPushButton{color:#fff;}')
        self.widget_7.setStyleSheet('.QWidget{background:#35485F;color:#fff;}.QLabel{color:#fff;}.QPushButton{color:#fff;}')
        self.table_dates.cellClicked.connect(self.del_exam_time)
        self.table_days.cellClicked.connect(self.del_exam_time_st)
        self.st_cs_table.cellClicked.connect(self.del_gp_ex)
        self.st_edt_2.returnPressed.connect(self.add_ex_gp)
        self.gp_name.currentIndexChanged.connect(self.get_exam_days)
        self.degree_dw.put_degree_btn.clicked.connect(self.buy_degree_db)
        self.degree_dw.mid.currentIndexChanged.connect(self.change_degree)
        self.st_attend_table.cellClicked.connect(self.degree_change)
        self.date_select.edt_btn.clicked.connect(self.edite_time)
        self.color_btn()
    def color_btn(self):
        try:
            for i in self.widget_4.findChildren(QPushButton):
                i.setStyleSheet("background:#05B963;")
            self.sender().setStyleSheet("background:#A8B1B2;")
        except:
            self.gps_btn.setStyleSheet("background:#A8B1B2;")
    def set_ex_id(self,exam_name):
        self.exam_name = exam_name
        self.exam_type = self.db.get_exam_type(self.exam_name)
    def degree_change(self,row, column):
        if column == 6:
            self.get_ex_id()
            try:
                price = float(self.st_attend_table.item(row,4).text())
            except:
                price = 0
            self.degree_dw.show()
            self.degree_dw.activateWindow()
            self.degree_dw.raise_()
            self.degree_dw.name_lbl.setText(self.st_attend_table.item(row,0).text())
            self.degree_dw.phone_lbl.setText(self.st_attend_table.item(row,1).text())
            self.degree_dw.barcode_lbl.setText(self.st_attend_table.item(row,2).text())
            self.degree_dw.ex_lbl.setText(self.exam_name)
            self.degree_dw.tottal_lbl.setText(self.st_attend_table.item(row,4).text())
            index = self.degree_dw.mid.findText(self.exam_day.currentText(), Qt.MatchFixedString)
            if index >= 0:
                self.degree_dw.mid.setCurrentIndex(index)
            inf = self.exam_day.currentText().split(" : ")
            x = self.db.get_st_degree(self.st_attend_table.item(row,2).text(), inf[0],inf[1],inf[2])
            self.degree_dw.baid_spn.setValue(x)
            self.degree_dw.baid_spn.setRange(0, price)
    def change_degree(self):
        nu =  self.degree_dw.mid.currentText().split(" : ")
        print nu
        x = self.db.get_st_degree(self.degree_dw.barcode_lbl.text(), nu[0], nu[1], nu[2])
        try:
            price = float(self.degree_dw.tottal_lbl.text())
        except:
            price = 0
        self.degree_dw.baid_spn.setValue(x)
        self.degree_dw.baid_spn.setRange(0, price)
    def get_ex_id(self):
        v = self.db.get_exam_dates_2(self.exam_name)
        self.degree_dw.mid.clear()
        #print v
        for i in v:
            self.degree_dw.mid.addItem(str(i[0]) + " : " + str(i[1]) + " : " + str(i[2]))
    def buy_degree_db(self):
        inf = self.degree_dw.mid.currentText().split(" : ")
        out = self.db.attend_st_exam(self.degree_dw.barcode_lbl.text(),self.exam_name,inf[0],inf[1],inf[2],u'حضور',self.degree_dw.baid_spn.value())
        #print out
        if out:
            self.degree_dw.hide()
            self.fill_st_attend()
    def all_exams_fill(self):
        self.all_exams.setRowCount(0)
        students = self.db.get_all_exams()
        for i in students:
            n = self.all_exams.rowCount()
            self.all_exams.insertRow(n)
            x = 0
            for j in i:
                self.all_exams.setItem(n, x, QTableWidgetItem(unicode(j)))
                x += 1
    def get_gp_names(self):
        ex_gps = self.db.get_exam_gps(self.exam_name)
        self.gp_name.clear()
        for i in ex_gps:
            self.gp_name.addItem(i[0])
    def get_exam_days(self):
        gp_name = self.gp_name.currentText()
        #print gp_name
        if gp_name:
            v = self.db.get_exam_dates_2(self.exam_name)
            #print v
            self.exam_day.clear()
            for i in v:
                self.exam_day.addItem(str(i[0]) + " : " + str(i[1]) + " : " + str(i[2]))
                #bill.append(i[1])
            if v:
                self.fill_st_attend()
    def day_select_show(self):
        self.day_select.show()
        self.day_select.activateWindow()
        self.day_select.raise_()
        self.fill_days()
    def date_select_show(self):
        self.date_select.show()
        self.date_select.add_btn.show()
        self.date_select.edt_btn.hide()
        self.date_select.activateWindow()
        self.date_select.raise_()
    def fill_st_attend(self):
        if self.gp_name.currentText():
            x = self.db.get_st_cs(self.gp_name.currentText())
            self.st_attend_table.setRowCount(0)
            if x:
                for i in x:
                    n = self.st_attend_table.rowCount()
                    self.st_attend_table.insertRow(n)
                    self.st_attend_table.setItem(n, 0, QTableWidgetItem(i[0]))
                    self.st_attend_table.setItem(n, 1, QTableWidgetItem(i[1]))
                    self.st_attend_table.setItem(n, 2, QTableWidgetItem(i[2]))
                    self.st_attend_table.setItem(n, 4, QTableWidgetItem(unicode(self.db.get_exam_max(self.exam_name))))
                    #print self.exam_day.currentText()
                    var = self.exam_day.currentText().split(" : ")
                    #if type(var) == int:
                    try:
                        x = self.db.check_attend_ex(i[2],var[0],var[1],var[2])
                    except:
                        pass

                    if x[0]:
                        self.st_attend_table.setItem(n, 3, QTableWidgetItem(u'حاضر'))
                        self.st_attend_table.setItem(n, 5, QTableWidgetItem(unicode(x[1])))
                    else:
                        self.st_attend_table.setItem(n, 3, QTableWidgetItem(u'غائب'))
                        self.st_attend_table.setItem(n, 5, QTableWidgetItem("0"))
                    self.st_attend_table.setItem(n, 6, QTableWidgetItem(u'تغيير'))
                    self.st_attend_table.item(n, 6).setBackground(QColor(20, 200, 10))
    def show_st_attend(self):
        self.color_btn()
        if self.exam_name:
            self.stackedWidget.setCurrentIndex(2)
            self.get_gp_names()
        else:
            self.dialoge_only(u'لا يوجد اسم', u'ادخل الاسم اولا')
    def add_ex_gp(self):
        gp = self.st_edt_2.text()
        print "name",gp
        if gp:
            gp_info = self.db.get_course_by_name(gp)
            if gp_info:
                exam = self.exam_name
                #print self.db.gp_exam_not_exist(gp_info[0], exam)
                if self.db.gp_exam_not_exist(gp_info[1], exam):

                    if self.set_time_ex(gp) == 0 :
                        self.dialoge_only(u'تحذير',u'الاختبار مطابق لمواعيد مجموعه ليس لها مواعيد')
                    else:
                        if self.db.add_gp_ex(gp_info[1], exam):
                            self.get_exam_gps()

                        else:
                            self.dialoge_only(u'لم تتم عملية الاضافة بنجاح', u'حاول مرة اخرى')
                else:
                    self.dialoge_only(u'الاختبار موجود فى المجموعة بالفعل', u'جرب مجموعة اخرى')

            else:
                self.dialoge_only(u'لا توجد بيانات لهذه المجموعة', u'ادخل الاسم الصحيح')
        else:
            self.dialoge_only(u'لا يوجد اسم',u'ادخل الاسم اولا')
        self.st_edt_2.clear()
    def set_time_ex(self , gp):
        type = unicode(self.exam_type)
        #print type
        if type == u'دورى' :
            out = self.db.get_time_gp(gp)
            if not out:
                print "noooooooooooo out"
                return 0
            else:
                for i in out :
                    self.db.add_exam_time(self.exam_name , i[2],i[3],i[4],i[5] , gp)

                return 1
        else:
            print "noooooooooo dwry"
            return 2
    def convert_days_to_dates(self):
        self.get_times_from_structure()
        self.exam_time_finish()
        db = Model()
        db.th_exam()
    def get_times_from_structure(self):
        if self.dialoge_only(u'سيتم حذف المواعيد الاخرى واضافة مواعيد جديدة', u'هل انت متاكد من الحذف') == QMessageBox.Ok:
            if self.db.del_exam_time_all(self.exam_name):
                st_date = self.start_dt.date().toPython()
                structures = self.db.get_exam_structure(self.exam_name)
                num_days = self.db.get_exam_num_days(self.exam_name)
                rest_days = 0
                while rest_days < num_days:
                    day = st_date.strftime('%A')
                    for i in structures:
                        if i[1] == day and rest_days < num_days:
                            self.db.add_exam_time(self.exam_name, st_date, day, i[2], i[3] , '')
                            rest_days += 1
                    st_date = st_date + datetime.timedelta(days=1)
            else:
                self.dialoge_only(u'لم تتم عملية حذف المواعيد',u'لنن تتم عملية تغير المواعيد')
    def completer_set_gps(self):
        self.completer = QCompleter()
        self.completer.setCompletionMode(QCompleter.PopupCompletion)
        self.completer.activated.connect(self.add_ex_gp)
        model = QStringListModel()
        self.completer.setModel(model)
        self.db.get_courses(model)
        self.st_edt_2.setCompleter(self.completer)
    def times_f(self):
        self.color_btn()
        if self.exam_name:
            if self.exam_type == u'دورى' :
                self.dialoge_only(u'تحذير',u'مواعيد هذا الامتحان محدده بالمجموعه')
            else:
                self.stackedWidget.setCurrentIndex(0)
                self.get_exam_times_structure()
                self.get_gp_names()
        else:
            self.dialoge_only(u'لا يوجد اسم',u'اختر اسم اولا')
    def add_exam_time_st(self):
        d = self.day_select.day_cmb.currentText()
        st = self.day_select.t1.time().toString("hh:mm:ss")
        end = self.day_select.t2.time().toString("hh:mm:ss")
        if self.db.add_exam_time_structure(self.exam_name,d,st,end):
            self.get_exam_times_structure()
            self.day_select.hide()
    def add_exam_time(self):
        d = self.date_select.date_edt.date().toString("yyyy-MM-dd")
        day = self.date_select.date_edt.date().toPython().strftime("%A")
        st = self.date_select.t1.time().toString("hh:mm:ss")
        end = self.date_select.t2.time().toString("hh:mm:ss")
        if self.db.add_exam_time(self.exam_name,d,day,st,end , ''):
            self.get_exam_times()
            self.date_select.hide()
    def get_exam_times_structure(self):
        x = self.db.get_exam_structure(self.exam_name)
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
    def get_exam_times(self):
        x = self.db.get_exam(self.exam_name)
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
                self.table_dates.item(n, 4).setBackground(QColor(231, 76, 62))
                self.table_dates.setItem(n, 5, QTableWidgetItem(u'تعديل'))
                self.table_dates.item(n, 5).setBackground(QColor(45, 135, 45))
    def del_exam_time_st(self,row, column):
        if column == 3:
            if self.dialoge_only(u'سيتم حذف معاد هذة الدورة', u'هل انت متاكد من الحذف') == QMessageBox.Ok:
                if self.db.del_exam_time_st(self.exam_name,self.table_days.item(row,0).text(), self.table_days.item(row,1).text(), self.table_days.item(row,2).text()):
                    self.get_exam_times_structure()
    def del_exam_time(self,row, column):
        if column == 4:
            self.del_exam_time_func(self.exam_name, self.table_dates.item(row,0).text(), self.table_dates.item(row,2).text(), self.table_dates.item(row,3).text())
        elif column == 5:
            self.date_select.date_id = self.table_dates.item(row, 0).statusTip()
            self.date_select.edt_btn.show()
            self.date_select.add_btn.hide()
            self.date_select.showNormal()
            info = self.db.get_exam_time_by_id(self.date_select.date_id)
            if info:
                self.date_select.date_edt.setDate(info[2])
                self.date_select.t1.setTime((datetime.datetime.min + info[4]).time())
                self.date_select.t2.setTime((datetime.datetime.min + info[5]).time())
    def edite_time(self):
        dt = self.date_select.date_edt.date().toPython()
        t1 = self.date_select.t1.time().toString("hh:mm:ss")
        t2 = self.date_select.t2.time().toString("hh:mm:ss")
        self.db.edt_time_exam(self.date_select.date_id, dt, t1, t2)
        self.get_exam_times()
        self.date_select.hide()
    def del_exam_time_func(self,course,date,t1,t2):
        if self.dialoge_only(u'سيتم حذف معاد هذة الدورة', u'هل انت متاكد من الحذف') == QMessageBox.Ok:
            if self.db.del_exam_time(course,date,t1,t2):
                self.get_exam_times()
    def exam_time(self):
        self.stackedWidget_2.setCurrentIndex(1)
        self.get_exam_times_structure()
        self.stackedWidget_2.setStyleSheet('.QWidget{background:#35485F;color:#fff;}.QLabel{color:#fff;}.QPushButton{color:#fff;}')
        self.widget_7.setStyleSheet('.QWidget{background:#35485F;color:#fff;}.QLabel{color:#fff;}.QPushButton{color:#fff;}')
    def exam_time_finish(self):
        self.stackedWidget_2.setCurrentIndex(0)
        self.get_exam_times()
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

    def get_exam_gps(self):
        self.color_btn()
        if self.exam_name:
            self.stackedWidget.setCurrentIndex(1)
            x = self.db.get_exam_gps(self.exam_name)
            self.st_cs_table.setRowCount(0)
            if x:
                for i in x:
                    n = self.st_cs_table.rowCount()
                    self.st_cs_table.insertRow(n)
                    self.st_cs_table.setItem(n, 0, QTableWidgetItem(i[0]))
                    self.st_cs_table.setItem(n, 1, QTableWidgetItem(u'حذف'))
                    self.st_cs_table.item(n, 1).setBackground(QColor(231, 76, 62))
        else:
            self.dialoge_only(u'لا يوجد اسم', u'اختر اسم اولا')
    def del_gp_ex(self, row, column):
        if column == 1:
            if self.dialoge_only(u'سيتم حذف الاختبار من هذة الدورة', u'هل انت متاكد من الحذف') == QMessageBox.Ok:
                if self.db.del_gp_ex(self.st_cs_table.item(row,0).text(),self.exam_name):
                    self.get_exam_gps()
                else:
                    self.dialoge_only(u'لم تتم عملية الحذف', u'راجع الاتصال بالشبكة')
    def print_attend(self):
        exam = self.cmb.text()
        day = self.attend_day.currentText()
        if exam and day:
            self.pr.print_attend(self.get_data_attend(),exam,day)
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