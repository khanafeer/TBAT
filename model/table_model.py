from PySide.QtCore import *
from PySide.QtGui import *
import operator
class MyTableModel(QAbstractTableModel):
    col_num = None
    def __init__(self, parent, mylist, header, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.mylist = mylist
        self.header = header
    def rowCount(self, parent):
        return len(self.mylist)
    def columnCount(self, parent):
        return len(self.header)
    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        try:
            return unicode(self.mylist[index.row()][index.column()])
        except:return ''
    def get_data(self,row,colm):
        return unicode(self.mylist[row][colm])
    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        return None
    def sort(self, col, order):
        """sort table by given column number col"""
        self.emit(SIGNAL("layoutAboutToBeChanged()"))
        self.mylist = sorted(self.mylist,
            key=operator.itemgetter(col))
        if order == Qt.DescendingOrder:
            self.mylist.reverse()
        self.emit(SIGNAL("layoutChanged()"))

    def data_col_column(self,index, role):
        if not index.isValid():
            return None

        if role == Qt.BackgroundRole and index.column() == self.col_num:
            return QBrush(QColor(238, 49, 36))
        elif role == Qt.BackgroundRole and index.column() == self.col_num+1:
            return QBrush(QColor(255,212,100))
        elif role != Qt.DisplayRole:
            return None
        return unicode(self.mylist[index.row()][index.column()])