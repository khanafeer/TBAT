# -*- coding: utf-8 -*-
from PySide.QtGui import *
from ctrls.tbat_init import First_step
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(':/path/imgs/home.ico'))
    app.setStyleSheet('''
    .QWidget{

background:#A8B1B2;
}
.QListWidget{
background-color: #000;
color:white;


}
.QListWidget::item:selected {
background:#A8B1B2

}

.QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{
    color: #b1b1b1;
    background-color: #323232;
    border: 0px solid #b1b1b1;
    border-radius: 1px;
}

.QRadioButton::indicator:checked
{
    background-color: qradialgradient(
        cx: 0.5, cy: 0.5,
        fx: 0.5, fy: 0.5,
        radius: 1.0,
        stop: 0.25 #00838F,
        stop: 0.3 #323232
    );
}


.QLineEdit { 
	color: rgb(0, 0, 0);
    font: 17px Helvetica, Arial, sans-serif;
    border: 1px solid #c4c4c4; 
    padding: 6px 6px 6px 6px; 
} 
 
.QLineEdit:focus { 
    outline: none; 
    border: 1px solid #7bc1f7; 
   }
.QLineEdit:hover{

    border: 1px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);
}

.QTableWidget::hover{

    border: 1px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);

}
 .QTabBar::tab {
   	background-color: #000;
	color:white;
     border: 0px;
     min-width: 28ex;
	min-height:9ex;
padding:8px;
 }
 
 .QTabBar::tab:selected, QTabBar::tab:hover {
       	background-color: #fff;
	color:#000;
     border: 0px;
     min-width: 25ex;
	min-height:9ex;
padding:8px;
 }
 
.QTabBar::tab:selected {
          	background-color: #fff;
	color:#000;
        border: 0px;
     min-width: 25ex;
	min-height:9ex;
padding:8px;
 }
    ''')
    s = First_step()
    app.exec_()