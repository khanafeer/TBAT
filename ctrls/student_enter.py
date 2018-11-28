# -*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
from model.Model import Model
import datetime
from views.student_enter import Ui_Form as student_enter
from views.mony_dw import Ui_Form as mony_dw
from views.degree_dw import Ui_Form as degree_dw
from views.alerm import Ui_alerm as alerm
from views.re_alerm import Ui_alerm as re_alerm
from views.replace_gp import Ui_Form as replace_gp
class replace(QWidget , replace_gp):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        for i in self.findChildren(QWidget):
            i.setAttribute(Qt.WA_StyledBackground, True)
class degree_dw(QWidget, degree_dw):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.setWindowTitle(u'الدرجة')
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
class alerm(QWidget , alerm):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        for i in self.findChildren(QWidget):
            i.setAttribute(Qt.WA_StyledBackground, True)
class re_alerm(QWidget , re_alerm):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        for i in self.findChildren(QWidget):
            i.setAttribute(Qt.WA_StyledBackground, True)
class student_enter(QWidget, student_enter):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        for i in self.findChildren(QWidget):
            i.setAttribute(Qt.WA_StyledBackground, True)
        self.db = Model()
        self.mony_dw = mony_dw()
        self.alerm = alerm()
        self.re_alerm = re_alerm()
        self.degree_dw = degree_dw()
        self.re_gp = replace()
        self.centerx(self.re_gp)
        self.centerx(self.degree_dw)
        self.centerx(self.mony_dw)
        self.centerx(self.alerm)
        self.centerx(self.re_alerm)
        self.attend_btn.hide()
        self.exam_btn.hide()
        self.exam_cmb.hide()
        self.exams_dw.hide()
        self.one_more = 1
        self.auto_attend.clicked.connect(self.sh_att)
        self.completer_set()
        self.search_btn.clicked.connect(self.attend_f)
        self.st_search.returnPressed.connect(self.attend_f)
        self.attend_btn.clicked.connect(self.attend_f)
        self.st_search.setFocus()
        self.mony_dw.put_mony_btn.clicked.connect(self.buy_mony_db)
        self.mony_btn.clicked.connect(self.buy_mony)
        self.mony_dw.mid.currentIndexChanged.connect(self.change_price)
        self.degree_dw.put_degree_btn.clicked.connect(self.buy_degree_db)
        self.exam_btn.clicked.connect(self.degree_exam)
        self.degree_dw.mid.currentIndexChanged.connect(self.change_degree)
        self.gp_rd.clicked.connect(self.sh_gp_w)
        self.ex_rd.clicked.connect(self.sh_ex_w)
        self.alerm.ok_bun.clicked.connect(self.allow)
        self.alerm.cancel.clicked.connect(self.not_allow)
        self.re_alerm.ok_bun.clicked.connect(self.allow_re)
        self.re_gp.ok_btn.clicked.connect(self.add_another)
        self.re_alerm.cancel.clicked.connect(self.not_allow_re)
        self.re_gp.cancel_btn.clicked.connect(self.cancel_another)
        self.re_gp.month_cmb.currentIndexChanged.connect(self.fill_class)
    def allow_re(self):
        ph = self.re_gp.label_10.text()
        id_att = self.re_gp.month_cmb_2.currentText()
        id = int(id_att.split(':')[0])
        course = self.re_gp.month_cmb.currentText()
        absence = self.absence_times(course, ph)
        if absence == 1 or absence == 2:
            x = self.db.attend_course(ph, id,datetime.datetime.now())
            if x == 1:
                self.result_lbl.setText(u'تم حضور الطالب')
                self.result_lbl.setStyleSheet("background:#638CA6;color:#fff;")
            elif x == 2:
                self.result_lbl.setText(u'الطالب حاضر من قبل')
                self.result_lbl.setStyleSheet("background:#EFCD61;color:#fff;")
        self.re_gp.hide()
        self.re_alerm.hide()

    def add_another(self):
        ph = self.re_gp.label_10.text()
        id_att = self.re_gp.month_cmb_2.currentText()
        id = int(id_att.split(':')[0])


        course = self.re_gp.month_cmb.currentText()
        date  = self.db.get_date_course(id , course)
        f = '%m'
        time_month = date[0].strftime(f)
        print time_month
        ch, baid = self.db.get_baid_mony(course, ph, id, int(time_month[0]))
        out = self.db.get_course_mony(course)
        mony_course = out[0][0]
        type = out[0][1]
        print baid
        print mony_course
        print ch
        if ch:
            if baid < mony_course:
                self.re_alerm.show()
                n = self.db.get_name(ph)
                self.re_alerm.name_lbl.setText(n[0])
                self.re_alerm.phone_lbl.setText(ph)
                self.re_alerm.barcode_lbl.setText(course)
                self.re_alerm.gp_lbl.setText(u'لم يتم الدفع كامل ')
                self.re_alerm.gp_type.setText(u'المبلغ المتبقى')
                self.re_alerm.raist.setText(str(mony_course - baid))
            else :
                absence = self.absence_times(course, ph)
                if absence == 1 or absence == 2:
                    x = self.db.attend_course(ph, id,datetime.datetime.now())
                    if x == 1:
                        self.result_lbl.setText(u'تم حضور الطالب')
                        self.result_lbl.setStyleSheet("background:#638CA6;color:#fff;")

                    elif x == 2:
                        self.result_lbl.setText(u'الطالب حاضر من قبل')
                        self.result_lbl.setStyleSheet("background:#EFCD61;color:#fff;")


        else:
            self.re_alerm.show()
            n = self.db.get_name(ph)

            self.re_alerm.name_lbl.setText(n[0])
            self.re_alerm.phone_lbl.setText(ph)
            self.re_alerm.barcode_lbl.setText(course)
            self.re_alerm.gp_type.setText(u'طريقه الدفع ')
            self.re_alerm.raist.setText(unicode(type))
        self.fill_course(course)

        self.re_gp.hide()
    def cancel_another(self):
        self.re_gp.hide()
    def fill_class(self):
        bill = []
        back = []
        index = []
        today = datetime.date.today()

        cs_name = self.re_gp.month_cmb.currentText()
        v = self.db.get_course_dates(cs_name)
        self.re_gp.month_cmb_2.clear()
        for i in v:
            self.re_gp.month_cmb_2.addItem(str(i[0]) + " : " + str(i[1]) + " : " + str(i[2]))
            bill.append(i[1])
        for i in bill:
            if (i <= today):
                diff = today - i
                print diff
                back.append(diff)
                index.append(bill.index(i))
        target = min(back)
        inx = back.index(target)
        final = bill[inx]
        self.re_gp.month_cmb_2.setCurrentIndex(inx)

    def buy_mony(self):
        if self.name_lbl_2.text():
            print self.price_lbl.text()
            try:
                price = float(self.price_lbl.text())
            except:
                price = 0
            self.get_mony_id()
            self.mony_dw.show()
            self.mony_dw.activateWindow()
            self.mony_dw.raise_()
            self.courses_dw.show()
            self.exams_dw.hide()
            self.gp_rd.clicked.connect(self.sh_gp_w)
            self.ex_rd.clicked.connect(self.sh_ex_w)
            self.mony_dw.name_lbl.setText(self.name_lbl.text())
            self.mony_dw.phone_lbl.setText(self.ph_lbl.text())
            self.mony_dw.barcode_lbl.setText(self.bc_label.text())
            self.mony_dw.gp_lbl.setText(self.name_lbl_2.text())
            self.mony_dw.tottal_lbl.setText(self.price_lbl.text())
            x = self.db.get_st_mony(self.bc_label.text(), self.name_lbl_2.text(), self.mony_dw.mid.currentText())
            self.mony_dw.baid_spn.setValue(price-x)
            self.mony_dw.baid_spn.setRange(0,price-x)
        else:
            self.result_lbl.setText(u'لا توجد مجموعة حالية للطالب لدفع مصاريفها')
            self.result_lbl.setStyleSheet("background:#E45F56;color:#fff;")
    def degree_exam(self):
        if self.name_lbl_3.text():
            self.get_ex_id()
            try:
                price = float(self.max_lbl.text())
            except:
                price = 0
            self.get_mony_id()
            self.degree_dw.show()
            self.degree_dw.activateWindow()
            self.degree_dw.raise_()
            self.gp_rd.clicked.connect(self.sh_gp_w)
            self.ex_rd.clicked.connect(self.sh_ex_w)
            self.degree_dw.name_lbl.setText(self.name_lbl.text())
            self.degree_dw.phone_lbl.setText(self.ph_lbl.text())
            self.degree_dw.barcode_lbl.setText(self.bc_label.text())
            self.degree_dw.ex_lbl.setText(self.name_lbl_3.text())
            self.degree_dw.tottal_lbl.setText(self.max_lbl.text())
            x = self.db.get_st_degree(self.bc_label.text(), self.degree_dw.mid.currentText().split(" : ")[0])
            self.degree_dw.baid_spn.setRange(0,price-x)
            self.degree_dw.baid_spn.setValue(price-x)
        else:
            self.result_lbl.setText(u'لا توجد مجموعة حالية للطالب لدفع مصاريفها')
            self.result_lbl.setStyleSheet("background:#E45F56;color:#fff;")
    def sh_gp_w(self):
        self.exams_dw.hide()
        self.courses_dw.show()
        self.exam_btn.hide()
        self.mony_btn.show()
        if self.auto_attend.isChecked():
            self.attend_btn.hide()
        else:
            self.attend_btn.show()
        self.attend_f()
    def sh_ex_w(self):
        self.exams_dw.show()
        self.courses_dw.hide()
        self.exam_btn.show()
        if self.auto_attend.isChecked():
            self.attend_btn.hide()
        else:
            self.attend_btn.show()
        self.mony_btn.hide()
        self.attend_f()
    def change_price(self):
        self.mony_dw.tottal_lbl.setText(self.price_lbl.text())
        x = self.db.get_st_mony(self.bc_label.text(), self.name_lbl_2.text(), self.mony_dw.mid.currentText())
        try:
            price = float(self.price_lbl.text())
        except:
            price = 0
        self.mony_dw.baid_spn.setRange(0, price - x)
        self.mony_dw.baid_spn.setValue(price - x)
    def change_degree(self):
        self.degree_dw.tottal_lbl.setText(self.max_lbl.text())
        x = self.db.get_st_degree(self.bc_label.text(), self.degree_dw.mid.currentText().split(" : ")[0])
        try:
            price = float(self.max_lbl.text())
        except:
            price = 0
        self.degree_dw.baid_spn.setRange(0, price - x)
        self.degree_dw.baid_spn.setValue(price - x)

    def get_mony_id(self):
        course_name = self.bill_method.text()
        if course_name == u'بالحصة':
            v = self.db.get_course_days(self.name_lbl_2.text())
            self.mony_dw.mid.clear()
            for i in v:
                self.mony_dw.mid.addItem(str(i[0]) + " : " + str(i[1]) + " : " + str(i[2]))
        elif course_name == u'بالشهر':
            v = self.db.get_course_months(self.name_lbl_2.text())
            self.mony_dw.mid.clear()
            self.mony_dw.mid.addItems(v)
        else:
            self.mony_dw.mid.clear()
            self.mony_dw.mid.addItem(self.name_lbl_2.text())
    def get_ex_id(self):
        v = self.db.get_exam_dates(self.name_lbl_3.text())
        self.degree_dw.mid.clear()
        print v
        for i in v:
            self.degree_dw.mid.addItem(str(i[0]) + " : " + str(i[1]) + " : " + str(i[2]))
    def buy_mony_db(self):
        if self.db.put_st_mony(self.mony_dw.barcode_lbl.text(),self.mony_dw.gp_lbl.text(),self.db.get_method_price(self.mony_dw.gp_lbl.text())[0],self.mony_dw.mid.currentText(),self.mony_dw.baid_spn.value()):
            self.mony_dw.hide()
    def buy_degree_db(self):
        if self.db.put_st_degree(self.degree_dw.barcode_lbl.text(),self.degree_dw.mid.currentText().split(" : ")[0],self.degree_dw.baid_spn.value()):
            self.degree_dw.hide()
    def centerx(self, x):
        frameGm = x.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        x.move(frameGm.topLeft())
    def attend_f(self):
        if self.auto_attend.isChecked():
            if self.gp_rd.isChecked():
                self.attend_gp()
            else:
                self.attend_ex()
        else:
            if self.gp_rd.isChecked():
                self.attend_gp()
                self.attend_st_gp(self.bc_label.text())
            else:
                self.attend_ex()
    def attend_ex(self):
        st = self.st_search.text()
        if st:
            if self.exam_cmb.count() > 1:
                self.attend_st_exam(st)
            else:
                phone = self.db.get_bc(st)
                if phone:
                    self.fill_student(phone)
                    values = self.db.get_st_exams(phone)
                    if values:
                        self.exam_cmb.hide()
                        self.exam_cmb.clear()
                        for i in values:
                            self.exam_cmb.addItem(i[0])
                        if len(values) == 1:
                            if self.auto_attend.isChecked():
                                self.attend_st_exam(phone)
                            else:
                                self.result_lbl.setText(u'الطالب مسجل يمكنك ضغط على زر الحضور')
                                self.result_lbl.setStyleSheet("background:#EFCD61;color:#fff;")
                        elif len(values) > 1:
                            self.exam_cmb.show()
                            self.attend_btn.show()
                            self.result_lbl.setText(u'الطالب مسجل يمكنك ضغط على زر الحضور')
                            self.result_lbl.setStyleSheet("background:#EFCD61;color:#fff;")
                    else:
                        self.clear_ex()
                        self.result_lbl.setText(u'لا توجد اختبارات حالية للطالب')
                        self.result_lbl.setStyleSheet("background:#E45F56;color:#fff;")
                else:
                    self.clear_st()
                    self.result_lbl.setText(u'الطالب غير موجود')
                    self.result_lbl.setStyleSheet("background:#E45F56;color:#fff;")
        else:
            self.result_lbl.setText(u'ادخل الباركود - الاسم - الهاتف اولا')
            self.result_lbl.setStyleSheet("background:#E45F56;color:#fff;")
    def attend_st_exam(self,phone):
        exam = self.exam_cmb.currentText()
        time = datetime.datetime.now().time()
        values = self.db.get_st_exam_times(exam)
        if values:
            self.fill_exam(exam)
            start = (datetime.datetime.min + values[0]).time()
            end = (datetime.datetime.min + values[1]).time()
            if start <= time < end:
                x = self.db.attend_exam(phone, values[2], 0)
                if x == 1:
                    self.result_lbl.setText(u'تم حضور الطالب')
                    self.result_lbl.setStyleSheet("background:#638CA6;color:#fff;")
                elif x == 2:
                    self.result_lbl.setText(u'الطالب حاضر من قبل')
                    self.result_lbl.setStyleSheet("background:#EFCD61;color:#fff;")
                else:
                    self.result_lbl.setText(u'يوجد مشكلة فى مواعيد المجموعة')
                    self.result_lbl.setStyleSheet("background:#E45F56;color:#fff;")
            else:
                self.result_lbl.setText(u'معاد الاختبار ليس فى هذا الوقت')
                self.result_lbl.setStyleSheet("background:#EFCD61;color:#fff;")
        else:
            self.clear_ex()
            self.result_lbl.setText(u'لا توجد مواعيد لهذا الاختبار')
            self.result_lbl.setStyleSheet("background:#EFCD61;color:#fff;")
    def attend_gp(self):
        st = self.st_search.text()
        if st:
            phone = self.db.get_bc(st)
            if phone:
                self.fill_student(phone)
                values = self.db.get_st_course_times(phone)
                if values:
                    if self.auto_attend.isChecked():
                        self.attend_st_gp(phone)
                    else:
                        self.result_lbl.setText(u'الطالب مسجل يمكنك ضغط على زر الحضور')
                        self.result_lbl.setStyleSheet("background:#EFCD61;color:#fff;")
                else:
                    self.clear_gp()
                    self.result_lbl.setText(u'لا توجد مجموعات حالية للطالب')
                    self.result_lbl.setStyleSheet("background:#E45F56;color:#fff;")

                    val = self.db.get_course_times()
                    groups_st = self.db.get_groups_st(phone)
                    if val and groups_st :
                        for i in val:
                            course = i[0]
                            f = '%m'
                            time = datetime.datetime.now().time()
                            time_month = i[4].strftime(f)
                            allow_before = self.db.get_allow_before(course)
                            start = (datetime.datetime.min + i[1]).time()
                            start_before = (
                            datetime.datetime.min + datetime.timedelta(hours=start.hour, minutes=start.minute,
                                                                       seconds=start.second) - datetime.timedelta(
                                minutes=int(allow_before[0]))).time()

                            end = (datetime.datetime.min + i[2]).time()

                            allow_min = self.db.get_allow(course)

                            allow_time = (
                            datetime.datetime.min + datetime.timedelta(hours=start.hour, minutes=start.minute,
                                                                       seconds=start.second) + datetime.timedelta(
                                minutes=int(allow_min[0]))).time()
                            now = datetime.datetime.now().time()

                            if start_before <= time < end:
                                self.fill_course(i[0])
                                flag = 1
                                if now > allow_time:
                                    if self.dialoge_only_time(u'الطالب متأخر عن المعاد المسموح بيه',
                                                         u'تحذير') == QMessageBox.Cancel:
                                        flag = 0
                                if flag == 1 :
                                    self.re_gp.show()

                                    self.re_gp.month_cmb.clear()
                                    self.re_gp.month_cmb.addItems(groups_st)
                                    self.re_gp.label_10.setText(phone)
                                    self.re_gp.label_12.setText(course)
                                    n = self.db.get_name(phone)
                                    self.re_gp.label_9.setText(n[0])

            else:
                self.clear_st()
                self.result_lbl.setText(u'الطالب غير موجود')
                self.result_lbl.setStyleSheet("background:#E45F56;color:#fff;")
        else:
            self.result_lbl.setText(u'ادخل الباركود - الاسم - الهاتف اولا')
            self.result_lbl.setStyleSheet("background:#E45F56;color:#fff;")
    def attend_st_gp(self,phone):
        date = datetime.datetime.today()
        time = datetime.datetime.now().time()
        values = self.db.get_st_course_times(phone)
        if values:
            for i in values:
                course = i[0]
                f= '%m'
                time_month= i[4].strftime(f)
                allow_before = self.db.get_allow_before(course)
                start = (datetime.datetime.min + i[1]).time()
                start_before =  (datetime.datetime.min+datetime.timedelta(hours=start.hour, minutes=start.minute, seconds=start.second) - datetime.timedelta(minutes = int(allow_before[0]))).time()
                end = (datetime.datetime.min + i[2]).time()
                allow_min = self.db.get_allow(course)
                allow_time =  (datetime.datetime.min+datetime.timedelta(hours=start.hour, minutes=start.minute, seconds=start.second) + datetime.timedelta(minutes = int(allow_min[0]))).time()
                now =  datetime.datetime.now().time()
                if start_before <= time < end:
                    ch ,baid  = self.db.get_baid_mony(course , phone , i[3] , int(time_month))
                    out = self.db.get_course_mony(course)
                    mony_course = out[0][0]
                    type = out[0][1]
                    print "XXXX",ch,baid
                    if ch:
                        if baid < mony_course :
                            self.alerm.show()
                            n = self.db.get_name(phone)
                            self.alerm.name_lbl.setText(n[0])
                            self.alerm.phone_lbl.setText(phone)
                            self.alerm.barcode_lbl.setText(course)
                            self.alerm.gp_lbl.setText(u'لم يتم الدفع كامل ')
                            self.alerm.gp_type.setText(u'المبلغ المتبقى')
                            self.alerm.raist.setText(str(mony_course-baid))
                        else:
                            flag = 1
                            if now > allow_time:
                                if self.dialoge_only_time(u'الطالب متأخر عن المعاد المسموح بيه',u'تحذير') == QMessageBox.Cancel :
                                   flag = 0
                            if flag == 1 :
                                absence = self.absence_times(course ,phone)
                                if absence == 1 or absence == 2 :
                                    x = self.db.attend_course(phone, i[3],datetime.datetime.now())
                                    if x == 1:
                                        self.result_lbl.setText(u'تم حضور الطالب')
                                        self.result_lbl.setStyleSheet("background:#638CA6;color:#fff;")
                                        break
                                    elif x == 2:
                                        self.result_lbl.setText(u'الطالب حاضر من قبل')
                                        self.result_lbl.setStyleSheet("background:#EFCD61;color:#fff;")
                                        break
                                    else:
                                        self.result_lbl.setText(u'يوجد مشكلة فى مواعيد المجموعة')
                                        self.result_lbl.setStyleSheet("background:#E45F56;color:#fff;")
                                        break
                                else:
                                    self.result_lbl.setText(u'تعدى عدد مرات الغياب المسموح بها ')
                                    self.result_lbl.setStyleSheet("background:#E45F56;color:#fff;")
                                    break
                    else:
                        self.alerm.show()
                        n = self.db.get_name(phone)
                        self.alerm.name_lbl.setText(n[0])
                        self.alerm.phone_lbl.setText(phone)
                        self.alerm.barcode_lbl.setText(course)
                        self.alerm.gp_type.setText(u'طريقه الدفع ')
                        self.alerm.raist.setText(unicode(type))
                    self.fill_course(i[0])
                else:
                    self.result_lbl.setText(u'معاد المجموعة ليس فى هذا الوقت')
                    self.result_lbl.setStyleSheet("background:#EFCD61;color:#fff;")

                    ## another student
                    val = self.db.get_course_times()
                    groups_st = self.db.get_groups_st(phone)

                    if val and groups_st:

                        for i in val:
                            course = i[0]
                            f = '%m'
                            time = datetime.datetime.now().time()
                            time_month = i[4].strftime(f)
                            allow_before = self.db.get_allow_before(course)
                            start = (datetime.datetime.min + i[1]).time()
                            start_before = (
                                datetime.datetime.min + datetime.timedelta(hours=start.hour, minutes=start.minute,
                                                                           seconds=start.second) - datetime.timedelta(
                                    minutes=int(allow_before[0]))).time()

                            end = (datetime.datetime.min + i[2]).time()

                            allow_min = self.db.get_allow(course)

                            allow_time = (
                                datetime.datetime.min + datetime.timedelta(hours=start.hour, minutes=start.minute,
                                                                           seconds=start.second) + datetime.timedelta(
                                    minutes=int(allow_min[0]))).time()
                            now = datetime.datetime.now().time()

                            if start_before <= time < end:
                                self.fill_course(i[0])
                                flag = 1
                                if now > allow_time:
                                    if self.dialoge_only_time(u'الطالب متأخر عن المعاد المسموح بيه',
                                                              u'تحذير') == QMessageBox.Cancel:
                                        flag = 0
                                if flag == 1:
                                    self.re_gp.show()

                                    self.re_gp.month_cmb.clear()
                                    self.re_gp.month_cmb.addItems(groups_st)
                                    self.re_gp.label_10.setText(phone)
                                    self.re_gp.label_12.setText(course)
                                    n = self.db.get_name(phone)
                                    self.re_gp.label_9.setText(n[0])



    def allow(self):
        phone = self.alerm.phone_lbl.text()
        time = datetime.datetime.now().time()
        values = self.db.get_st_course_times(phone)
        print "vvv",values
        if values:
            for i in values:
                course = i[0]
                start = (datetime.datetime.min + i[1]).time()
                allow_before = self.db.get_allow_before(course)
                start_before =  (datetime.datetime.min+datetime.timedelta(hours=start.hour, minutes=start.minute, seconds=start.second) - datetime.timedelta(minutes = int(allow_before[0]))).time()

                end = (datetime.datetime.min + i[2]).time()
                allow_min = self.db.get_allow(course)
                allow_time = (datetime.datetime.min + datetime.timedelta(hours=start.hour, minutes=start.minute,
                                                                         seconds=start.second) + datetime.timedelta(
                    minutes=int(allow_min[0]))).time()
                now = datetime.datetime.now().time()
                if start_before <= time < end:
                    flag = 1
                    if now > allow_time:
                        if self.dialoge_only_time(u'الطالب متأخر عن المعاد المسموح بيه', u'تحذير') == QMessageBox.Cancel:
                            flag = 0
                    if flag == 1:
                        absence = self.absence_times(course, phone)
                        if absence == 1 or absence == 2 :

                            x = self.db.attend_course(phone, i[3],datetime.datetime.now())

                            if x == 1:
                                self.result_lbl.setText(u'تم حضور الطالب')
                                self.result_lbl.setStyleSheet("background:#638CA6;color:#fff;")
                                break
                            elif x == 2:
                                self.result_lbl.setText(u'الطالب حاضر من قبل')
                                self.result_lbl.setStyleSheet("background:#EFCD61;color:#fff;")
                                break
                        else:
                            self.result_lbl.setText(u'تعدى عدد مرات الغياب المسموح بها ')
                            self.result_lbl.setStyleSheet("background:#E45F56;color:#fff;")
                            break
                else:
                    self.result_lbl.setText(u'يوجد مشكلة فى مواعيد المجموعة')
                    self.result_lbl.setStyleSheet("background:#E45F56;color:#fff;")
                    break
        self.alerm.hide()
    def absence_times(self , gp , ph):
        times = self.db.get_times(gp)
        v = self.db.get_course_dates_before(gp)
        x = self.db.get_attend(ph)
        vl = []
        xl = []
        for i in v:
            vl.append(i[0])

        for i in x:
            if i[0] in vl:
                xl.append(i[0])
        f = 0
        deff = int(len(vl) - len(xl))
        one_more = self.db.get_allow_times(ph , gp)

        if int(deff) > int(times[0]) and not one_more:
            if self.dialoge_only_allow(u'تحذير',u'الطالب تعدى مرات الغياب المسموحه') == QMessageBox.Ok:
                one_more = 1
                self.db.put_allow_times(ph , gp , one_more)
                f = 1
        elif  (int(deff) > int(times[0])) and (one_more[0] >=  1) :

            if self.dialoge_only_allow(u'تحذير',u'الطالب تعدى مرات الغياب المسموحه من قبل وحضر سابقا') == QMessageBox.Ok:
                one_more = one_more[0] + 1
                self.db.put_allow_times(ph, gp , one_more)
                f = 1
        elif  (int(deff) <=  int(times[0])) :
            f = 2

        return f

    def not_allow(self):
        self.alerm.hide()

    def not_allow_re(self):
        self.re_alerm.hide()

    def completer_set(self):
        completer = QCompleter()
        completer.setCompletionMode(QCompleter.PopupCompletion)
        completer.activated.connect(self.attend_f)
        model = QStringListModel()
        completer.setModel(model)
        self.db.get_students(model)
        self.st_search.setCompleter(completer)
    def sh_att(self):
        if self.auto_attend.isChecked():
            self.attend_btn.hide()
        else:
            self.attend_btn.show()
    def fill_student(self,st_phone):
        info = self.db.get_student(st_phone)
        if info:
            self.bc_label.setText(info[0])
            self.name_lbl.setText(info[1])
            self.school_lbl.setText(info[2])
            self.ph_lbl.setText(info[3])
            self.fph_lbl.setText(info[4])
            self.mail_lbl.setText(info[5])
            self.add_lbl.setText(info[6])
            self.details_lbl.setText(info[7])
        else:
            self.clear_st()
    def fill_course(self,course_name):
        course_info = self.db.get_course_by_name(course_name)
        if course_info:
            self.name_lbl_2.setText(unicode(course_info[1]))
            self.days_lbl.setText(unicode(course_info[2]))
            self.hours_lbl.setText(unicode(course_info[3]))
            self.price_lbl.setText(unicode(course_info[4]))
            self.inst_lbl.setText(unicode(course_info[5]))
            self.details_lbl.setText(unicode(course_info[6]))
            self.bill_method.setText(unicode(course_info[7]))
        else:
            self.clear_gp()
    def fill_exam(self,exam):
        info = self.db.get_exam_by_name(exam)
        if info:
            self.name_lbl_3.setText(unicode(info[0]))
            self.days_lbl_2.setText(unicode(info[1]))
            self.hours_lbl_2.setText(unicode(info[2]))
            self.max_lbl.setText(unicode(info[3]))
            self.details_lbl_3.setText(unicode(info[4]))
        else:
            self.clear_ex()
    def clear_ex(self):
        self.name_lbl_3.clear()
        self.days_lbl_2.clear()
        self.hours_lbl_2.clear()
        self.max_lbl.clear()
        self.details_lbl_3.clear()
    def clear_gp(self):
        self.name_lbl_2.clear()
        self.days_lbl.clear()
        self.hours_lbl.clear()
        self.inst_lbl.clear()
        self.details_lbl.clear()
        self.price_lbl.clear()
        self.bill_method.clear()
    def clear_st(self):
        self.bc_label.clear()
        self.name_lbl.clear()
        self.school_lbl.clear()
        self.ph_lbl.clear()
        self.fph_lbl.clear()
        self.mail_lbl.clear()
        self.add_lbl.clear()
        self.details_lbl.clear()
    def dialoge_only(self, x, y):
        msgBox = QMessageBox()
        msgBox.setFixedSize(150, 100)
        msgBox.setWindowTitle(u'تحذير')
        msgBox.setText(unicode(x))
        msgBox.setInformativeText(y)
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        return msgBox.exec_()

    def dialoge_only_allow(self, x, y):
        msgBox = QMessageBox()
        msgBox.setFixedSize(150, 100)
        msgBox.setWindowTitle(u'تحذير')
        msgBox.setText(unicode(x))
        msgBox.setInformativeText(y)
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        buttonY = msgBox.button(QMessageBox.Ok)
        buttonY.setText(u'مسموح')
        buttonN = msgBox.button(QMessageBox.Cancel)
        buttonN.setText(u'غير مسوح')
        return msgBox.exec_()
    def dialoge_only_time(self, x, y):
        msgBox = QMessageBox()
        msgBox.setFixedSize(150, 100)
        msgBox.setWindowTitle(u'تحذير')
        msgBox.setText(unicode(x))
        msgBox.setInformativeText(y)
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        buttonY = msgBox.button(QMessageBox.Ok)
        buttonY.setText(u'مسموح')
        buttonN = msgBox.button(QMessageBox.Cancel)
        buttonN.setText(u'غير مسوح')
        return msgBox.exec_()