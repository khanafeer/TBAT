# -*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
from views.bc_num import Ui_Form as bc_num
from ctrls.printing import print_doc
class bc_num(QWidget,bc_num):
    barcode_name = None
    bc_price = None
    data = None
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.center()
        self.one()
        self.pr = print_doc()
        self.widget.setAttribute(Qt.WA_StyledBackground, True)
        self.a4_rd.clicked.connect(self.A4)
        self.one_rd.clicked.connect(self.one)
        self.two_rd.clicked.connect(self.two)
        self.pushButton.clicked.connect(self.print_func)
    def print_func(self):
        width = self.w_sin.value()
        heihgt = self.height_spn.value()
        h_num = self.h_num_spn.value()
        v_num = self.v_num_spn.value()
        start = self.st_spn.value()
        details = self.details_edt.text()
        num_copies = self.pr_num.value()
        self.pr.print_logic(width,heihgt,num_copies,self.data,details,self.a4_rd.isChecked(),h_num,v_num,start)
        self.hide()
    def pre_show(self,data):
        self.showNormal()
        self.raise_()
        self.activateWindow()
        self.data = data
        print self.data
    def one(self):
        self.w_sin.setValue(45)
        self.height_spn.setValue(25)
        self.h_num_spn.setValue(1)
        self.v_num_spn.setValue(1)
        self.st_spn.setValue(1)
    def two(self):
        self.w_sin.setValue(45)
        self.height_spn.setValue(25)
        self.h_num_spn.setValue(1)
        self.v_num_spn.setValue(2)
        self.st_spn.setValue(1)
    def A4(self):
        self.w_sin.setValue(210)
        self.height_spn.setValue(297)
        self.h_num_spn.setValue(5)
        self.v_num_spn.setValue(13)
        self.st_spn.setValue(1)
    def center(self):
        frameGm = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())
