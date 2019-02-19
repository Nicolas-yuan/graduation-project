# -*- coding: utf-8 -*-

#本程序用于显示数据清理和流重组后的数据

import sys
from window_base import *
from cleaningData import *
from PyQt5.QtWidgets import QAbstractItemView, QHeaderView
from PyQt5.QtGui import QFont

class show_Datastream_Window(QtWidgets.QMainWindow, Ui_MainWindow):
    Packet_reassemble = ''
    def __init__(self):
        super(show_Datastream_Window, self).__init__()
        super().setupUi(self)

        # 设置垂直布局
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        # 表格控件
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(10, 20, 1001, 421))
        self.tableView.setObjectName("tableView")
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 设置表格内容不可更改
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)  # 整行选中的方式
            # 下面代码让表格100填满窗口
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 设置表格控件的缩放比
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
            # 加入布局
        self.verticalLayout.addWidget(self.tableView)
        # 文本控件
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
            # 设置文本控件的缩放比
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setFont(QFont('SansSerif', 15))
            # 加入布局
        self.verticalLayout.addWidget(self.textBrowser)
        # 布局初始化
        self.setCentralWidget(self.centralwidget)

        # 加载事件
        self.action_event()

        super().createUi(self)

    def tableView_set(self):
        # 添加表头：
        self.model = QtGui.QStandardItemModel(self.tableView)
        # 设置表头
        self.model.setHorizontalHeaderLabels(['开始时间', '结束时间', '流长度', '流数据'])

        for j in range(0, len(self.Packet_reassemble)):
            for i in range(0, 4):   # range取头不取尾
                self.model.setItem(j, i, QtGui.QStandardItem(self.Packet_cleaning[j][i]))
                # 设置字符颜色
                self.model.item(j, i).setForeground(QtGui.QBrush(QtGui.QColor(0, 0, 255)))
                # 设置字符位置
                self.model.item(j, i).setTextAlignment(QtCore.Qt.AlignCenter)

        # 显示数据
        self.tableView.setModel(self.model)

    def action_event(self):
        # 二级菜单事件
        #self.actionSeparate.triggered.connect()
        # 设置表格点击事件
        self.tableView.clicked['QModelIndex'].connect(self.textBrowser_set)

    def textBrowser_set(self):
        index = self.tableView.currentIndex()
        if index.row() >= 0:
            text = self.Packet_reassemble[index.row()][3].encode(encoding='utf-8', errors='ignore')
            self.textBrowser.clear()
            self.textBrowser.insertPlainText(text.hex())
        else:
            pass

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mywindow = show_Datastream_Window()
    mywindow.tableView_set()
    mywindow.show()
    app.exec_()
    sys.exit()