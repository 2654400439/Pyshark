from PyQt5 import QtCore, QtGui
import sys
from PyQt5.QtCore import QEventLoop, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

from mainwindow import *

import time

from parse_packets import *


class EmittingStr(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str)  # 定义一个发送str的信号

    def write(self, text):
        self.textWritten.emit(str(text))
        QApplication.processEvents()


class ControlBoard(QMainWindow, Ui_MainWindow, QTableWidgetItem):
    def __init__(self, parent=None):
        super(ControlBoard, self).__init__(parent)
        self.setupUi(self)
        # 下面将输出重定向到textBrowser中
        sys.stdout = EmittingStr(textWritten=self.outputWritten)
        sys.stderr = EmittingStr(textWritten=self.outputWritten)
        self.pushButton_start.clicked.connect(self.print_packets)
        self.pushButton_pause.clicked.connect(self.pause)
        self.tableWidget.setHorizontalHeaderLabels(['No.', 'Time', 'Source', 'Destination', 'Protocol', 'Info'])
        self.set_table()

    def outputWritten(self, text):
        cursor = self.textBrowser.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.textBrowser.setTextCursor(cursor)
        self.textBrowser.ensureCursorVisible()

    def print_packets(self):
        device_packets()

    def pause(self):
        pause_capture()

    def set_table(self):
        self.tableWidget.setItem(0, 0, QTableWidgetItem('hello'))
        self.tableWidget.setItem(0, 1, QTableWidgetItem('hello'))
        self.tableWidget.setItem(0, 2, QTableWidgetItem('hello'))
        self.tableWidget.setItem(1, 0, QTableWidgetItem('hello'))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = ControlBoard()
    ui.show()
    sys.exit(app.exec_())
