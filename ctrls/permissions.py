# -*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
from model.Model import Model
import datetime
from math import ceil
from views.permissions import Ui_Form as permissions
from views.perm_set import Ui_Form as perm_set
from views.user_widget import Ui_Form as add_user
class add_user(QWidget, add_user):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.tot_w_2.setAttribute(Qt.WA_StyledBackground, True)
class perm_set(QWidget, perm_set):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.widget.setAttribute(Qt.WA_StyledBackground, True)
class permissions(QWidget, permissions):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.uid.hide()
        self.db = Model()
        self.perm_set = perm_set()
        self.centerx(self.perm_set)
        self.usr = add_user()
        self.centerx(self.usr)
        self.widget.setAttribute(Qt.WA_StyledBackground, True)
        #self.uadd.clicked.connect(self.add_user)
        self.uadd.clicked.connect(self.a_user)
        self.uedite.clicked.connect(self.edite_user)
        self.udelet.clicked.connect(self.delete_user)
        self.usr.add_save.clicked.connect(self.save)
        self.usr.cancel_save.clicked.connect(self.cancel)
        self.permissions_btn.clicked.connect(self.perm_set.show)
        self.perm_set.perm_set_btn.clicked.connect(self.update_permissions)
        self.fill_users()
        self.uid.setText("0")
    def a_user(self):
        self.usr.show()
    def fill_access_check(self):
        n = self.perm_set.perm_table.rowCount()
        times = self.db.get_user_time(int(self.perm_set.user_id.text()))
        if times:
            t1 = QTime.fromString(unicode(times[1]) ,u"hh:mm:ss")
            t2 = QTime.fromString(unicode(times[2]) ,u"hh:mm:ss")
            if times[3] == 1:
                self.perm_set.times_ck.setChecked(True)
            else:
                self.perm_set.times_ck.setChecked(False)
        else:
            self.perm_set.times_ck.setChecked(True)
            t1 = QTime.fromString("00:00:00", u"hh:mm:ss")
            t2 = QTime.fromString("23:59:00", u"hh:mm:ss")
        self.perm_set.st_dt.setTime(t1)
        self.perm_set.end_dt.setTime(t2)
        access = self.db.get_users_access(int(self.perm_set.user_id.text()))
        for x in range(n):
            chkBoxItem = QTableWidgetItem()
            chkBoxItem.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            self.perm_set.perm_table.setItem(x,1,chkBoxItem)
            if self.perm_set.perm_table.item(x,0).text() in access:
                chkBoxItem.setCheckState(Qt.Checked)
            else:
                chkBoxItem.setCheckState(Qt.Unchecked)
            self.perm_set.perm_table.resizeColumnsToContents()
    def update_permissions(self):
        t1 = self.perm_set.st_dt.time().toPython()
        t2 = self.perm_set.end_dt.time().toPython()
        uid = int(self.perm_set.user_id.text())
        if self.perm_set.times_ck.isChecked():
            self.db.set_user_time(t1, t2, "1", uid)
        else:
            self.db.set_user_time(t1, t2, "0", uid)
        n = self.perm_set.perm_table.rowCount()
        for x in range(n):
            if self.perm_set.perm_table.item(x,1).checkState() == Qt.CheckState.Checked:
                tf = 1
            else:
                tf = 0
            self.db.set_user_access(uid,self.perm_set.perm_table.item(x,0).text(),tf)
    def delete_user(self):
        name = self.uname.text()
        if not name :
            self.dialoge_only(u'رجاء اختيار العنصر ',u'')
        else:
            if self.dialoge_only( u'هل انت متاكد من هذة العملية',u"سيتم مسح المستخدم نهائيا") == QMessageBox.Ok:
                ufname = self.ufname.text()
                uid = self.uid.text()
                if (self.uname.text() == 'admin' and ufname == 'admin') or int(uid) ==1 :
                    self.dialoge_only(u'احترس',u'لا يمكن حذف حساب المدير الافتراضى')

                else:
                    if self.db.delete_user(ufname):
                        self.fill_users()
                    else:
                        self.dialoge_only(u'لا يمكن حذف العميل', u'هذا العميل مرتبط بعمليات بيع وشراء')
    def add_user(self):
        uid = self.uid.text()
        fname = unicode(self.ufname.text())
        name = unicode(self.uname.text())
        pas = unicode(self.upass.text())
        if self.uadminradio.isChecked():
            type = u"A"
        elif self.userradio.isChecked():
            type = u"U"
        if self.check_length(fname, name , pas):
            if self.db.add_user(fname, name, pas, type):
                self.fill_users()
            else:
                if self.dialoge_only(u'المستخدم موجود من قبل',
                                     u'سيتم تغير اسم المستخدم وكلمة السر اذا كنت موافق اكمل العملية') == QMessageBox.Ok:
                    self.db.update_user(fname, name, pas, type, uid)
                    self.fill_users()
        else:
            self.dialoge_only(u'راجع بياناتك', u'املا كل الخانات واجعل اقل طول للرقم السرى 6')
    def edite_user(self):
        uid = self.uid.text()
        if int(uid) == 0 :
            self.dialoge_only(u'رجاء اختيار مستخدم للتعديل',u'')

        else:
            fname = unicode(self.ufname.text())
            name = unicode(self.uname.text())
            pas = unicode(self.upass.text())
            if self.uadminradio.isChecked():
                type = u"A"
            elif self.userradio.isChecked():
                type = u"U"

            if int(uid) == 1 and type == "U" :
                self.dialoge_only(u'تحذير',u'لا يمكن تحويل هذا المدير الى مستخدم ')
            else:
                if self.check_length(fname, name , pas):
                    self.db.update_user(fname, name, pas, type, uid)
                    #self.dialoge_only(u'اختر العنصر اولا',u'')
                    self.fill_users()
                else:
                    self.dialoge_only(u'راجع بياناتك', u'املا كل الخانات واجعل اقل طول للرقم السرى 6')

        self.uid.setText("0")
    def check_length(self,fname,name,pas):
        if len(fname) > 1 and len(name) > 1 and len(pas) > 5:
            return True
        else:
            return False

    def fill_users(self):
        users = self.db.get_all_users()
        if users:
            self.show_users(users)
        else:
            self.empty_user_layout()
        self.empty_users()
    def empty_users(self):
        self.ufname.clear()
        self.uname.clear()
        self.upass.clear()
    def show_users(self, list):
        pos = self.create_grid_pos(list)
        self.empty_user_layout()
        x = 0
        for item,more in self.lookahead(list):
            self.i = QPushButton(item)
            self.i.setObjectName("abtn_" + item)
            self.i.setCheckable(True)
            sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
            self.i.setSizePolicy(sizePolicy)
            self.bottom_w.layout().addWidget(self.i, pos[x][0], pos[x][1])
            x += 1
            if not more:
                self.set_user_info(self.i.text())
        self.add_user_items()
    def lookahead(self,iterable):
        """Pass through all values from the given iterable, augmented by the
        information if there are more values to come after the current one
        (True), or if it is the last value (False).
        """
        # Get an iterator and pull the first value.
        it = iter(iterable)
        last = next(it)
        # Run the iterator to exhaustion (starting from the second value).
        for val in it:
            # Report the *previous* value (more to come).
            yield last, True
            last = val
        # Report the last value.
        yield last, False
    def create_grid_pos(self, list):
        """create the position of grid items"""
        pos = []
        mul = self.get_multiply(len(list))
        i = int(mul[0])
        j = int(mul[1])
        for x in range(j):
            for y in range(i):
                pos.append((x, y))
        return pos
    def get_multiply(self, count, i=1):
        """return the two multiplies"""
        res = count / i
        if res > 5:
            i += 1
            return self.get_multiply(count, i)
        else:
            if ceil(res) * i < count:
                return (ceil(res) + 1, i)
            else:
                return (ceil(res), i)
    def add_user_items(self):
        """for the bottom widget buttons"""
        self.places_group = QButtonGroup(self)
        for btt in self.bottom_w.findChildren(QPushButton):
            self.places_group.addButton(btt)
        self.places_group.buttonClicked.connect(self.users_btn_clk)
    def users_btn_clk(self,bt):
        self.set_user_info(unicode(bt.text()))
    def set_user_info(self,name):
        uid = self.db.get_user_id(name)
        x = self.db.get_user_info(uid)
        if x:
            self.uid.setText(unicode(x[0]))
            self.perm_set.user_id.setText(unicode(x[0]))
            self.ufname.setText(unicode(x[1]))
            self.perm_set.user_full_name.setText(unicode(x[1]))
            self.uname.setText(unicode(x[2]))
            self.upass.setText(unicode(x[3]))
            if x[4] == 'A':
                self.uadminradio.setChecked(True)
            else:
                self.userradio.setChecked(True)
            self.fill_access_check()
    def empty_user_layout(self):
        for bt in self.bottom_w.findChildren(QPushButton):
            bt.deleteLater()
    def dialoge_only(self, x, y):
        msgBox = QMessageBox()
        msgBox.setFixedSize(150, 100)
        msgBox.setWindowTitle(u'تحذير')
        msgBox.setText(unicode(x))
        msgBox.setInformativeText(y)
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        return msgBox.exec_()
    def centerx(self,x):
        frameGm = x.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        x.move(frameGm.topLeft())
    def save(self):
        name = self.usr.name.text()
        u_name = self.usr.u_name.text()
        passwd  = self.usr.passwd.text()
        if self.usr.manage.isChecked():
            type = u"A"
        elif self.usr.user.isChecked():
            type = u"U"
        if self.check_length(name, u_name , passwd):
            if self.db.add_user(name, u_name, passwd, type):
                self.fill_users()
                self.usr.passwd.clear()
                self.usr.name.clear()
                self.usr.u_name.clear()
                self.usr.hide()
            else:
                self.usr.alerm.setText("this user is found ")
                self.fill_users()
        else:
            self.dialoge_only(u'راجع بياناتك', u'املا كل الخانات واجعل اقل طول للرقم السرى 6')
    def cancel(self):
        self.usr.alerm.clear()
        self.usr.u_name.clear()
        self.usr.name.clear()
        self.usr.passwd.clear()
        self.usr.user.setChecked(False)
        self.usr.manage.setChecked(False)
        self.usr.hide()