# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1310, 940)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setGeometry(QtCore.QRect(0, 0, 99, 28))
        self.pushButton_start.setObjectName("pushButton_start")
        self.pushButton_pause = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_pause.setGeometry(QtCore.QRect(130, 0, 99, 28))
        self.pushButton_pause.setObjectName("pushButton_pause")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 60, 1301, 441))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMouseTracking(False)
        self.tableWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tableWidget.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 81, 31))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(70, 30, 1151, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1220, 30, 81, 28))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 750, 1301, 301))
        self.textBrowser.setObjectName("textBrowser")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(0, 500, 811, 241))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.treeWidget.setFont(font)
        self.treeWidget.setObjectName("treeWidget")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(850, 560, 31, 111))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setOrientation(QtCore.Qt.Vertical)
        self.progressBar.setObjectName("progressBar")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(810, 500, 491, 241))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(850, 510, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.progressBar_2 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_2.setGeometry(QtCore.QRect(1010, 560, 31, 111))
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setTextVisible(False)
        self.progressBar_2.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_2.setObjectName("progressBar_2")
        self.progressBar_3 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_3.setGeometry(QtCore.QRect(930, 560, 31, 111))
        self.progressBar_3.setProperty("value", 0)
        self.progressBar_3.setTextVisible(False)
        self.progressBar_3.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_3.setObjectName("progressBar_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(850, 690, 31, 18))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(930, 690, 41, 18))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(1010, 690, 41, 18))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1070, 510, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.progressBar_4 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_4.setGeometry(QtCore.QRect(1120, 570, 161, 21))
        self.progressBar_4.setProperty("value", 0)
        self.progressBar_4.setTextVisible(False)
        self.progressBar_4.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar_4.setObjectName("progressBar_4")
        self.progressBar_5 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_5.setGeometry(QtCore.QRect(1120, 620, 161, 21))
        self.progressBar_5.setProperty("value", 0)
        self.progressBar_5.setTextVisible(False)
        self.progressBar_5.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar_5.setObjectName("progressBar_5")
        self.progressBar_6 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_6.setGeometry(QtCore.QRect(1120, 670, 161, 21))
        self.progressBar_6.setProperty("value", 0)
        self.progressBar_6.setTextVisible(False)
        self.progressBar_6.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar_6.setObjectName("progressBar_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(1080, 570, 41, 18))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(1080, 620, 41, 18))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1080, 670, 41, 18))
        self.label_9.setObjectName("label_9")
        self.textBrowser_2.raise_()
        self.pushButton_start.raise_()
        self.pushButton_pause.raise_()
        self.tableWidget.raise_()
        self.label.raise_()
        self.lineEdit.raise_()
        self.pushButton.raise_()
        self.textBrowser.raise_()
        self.treeWidget.raise_()
        self.progressBar.raise_()
        self.label_2.raise_()
        self.progressBar_2.raise_()
        self.progressBar_3.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.progressBar_4.raise_()
        self.progressBar_5.raise_()
        self.progressBar_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1310, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        self.menu_5 = QtWidgets.QMenu(self.menubar)
        self.menu_5.setObjectName("menu_5")
        self.menu_6 = QtWidgets.QMenu(self.menubar)
        self.menu_6.setObjectName("menu_6")
        self.menu_7 = QtWidgets.QMenu(self.menubar)
        self.menu_7.setObjectName("menu_7")
        self.menu_8 = QtWidgets.QMenu(self.menubar)
        self.menu_8.setObjectName("menu_8")
        self.menu_9 = QtWidgets.QMenu(self.menubar)
        self.menu_9.setObjectName("menu_9")
        self.menu_10 = QtWidgets.QMenu(self.menubar)
        self.menu_10.setObjectName("menu_10")
        self.menu_11 = QtWidgets.QMenu(self.menubar)
        self.menu_11.setObjectName("menu_11")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())
        self.menubar.addAction(self.menu_6.menuAction())
        self.menubar.addAction(self.menu_7.menuAction())
        self.menubar.addAction(self.menu_8.menuAction())
        self.menubar.addAction(self.menu_9.menuAction())
        self.menubar.addAction(self.menu_10.menuAction())
        self.menubar.addAction(self.menu_11.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_start.setText(_translate("MainWindow", "开始"))
        self.pushButton_pause.setText(_translate("MainWindow", "暂停"))
        self.tableWidget.setSortingEnabled(False)
        self.label.setText(_translate("MainWindow", "Filter"))
        self.pushButton.setText(_translate("MainWindow", "Ok"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "各层数据报"))
        self.label_2.setText(_translate("MainWindow", "网络层实时流量协议占比"))
        self.label_3.setText(_translate("MainWindow", "ARP"))
        self.label_4.setText(_translate("MainWindow", "IPv6"))
        self.label_5.setText(_translate("MainWindow", "IPv4"))
        self.label_6.setText(_translate("MainWindow", "传输层实时流量协议占比"))
        self.progressBar_4.setFormat(_translate("MainWindow", "%p%"))
        self.label_7.setText(_translate("MainWindow", "TCP"))
        self.label_8.setText(_translate("MainWindow", "UDP"))
        self.label_9.setText(_translate("MainWindow", "Else"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "编辑"))
        self.menu_3.setTitle(_translate("MainWindow", "视图"))
        self.menu_4.setTitle(_translate("MainWindow", "跳转"))
        self.menu_5.setTitle(_translate("MainWindow", "捕获"))
        self.menu_6.setTitle(_translate("MainWindow", "分析"))
        self.menu_7.setTitle(_translate("MainWindow", "统计"))
        self.menu_8.setTitle(_translate("MainWindow", "电话"))
        self.menu_9.setTitle(_translate("MainWindow", "无线"))
        self.menu_10.setTitle(_translate("MainWindow", "工具"))
        self.menu_11.setTitle(_translate("MainWindow", "帮助"))
