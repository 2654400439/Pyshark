from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView
from PyQt5.QtGui import QBrush, QColor

from mainwindow import *
from Tmp_file.parse_packets import *


class EmittingStr(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str)  # 定义一个发送str的信号

    # 发射信号
    def write(self, text):
        self.textWritten.emit(str(text))
        QApplication.processEvents()


class ControlBoard(QMainWindow, Ui_MainWindow, QTableWidgetItem):
    def __init__(self, parent=None):
        super(ControlBoard, self).__init__(parent)
        self.setupUi(self)
        # 下面将输出重定向到textBrowser中
        sys.stdout = EmittingStr(textWritten=self.outputTable)
        # sys.stderr = EmittingStr(textWritten=self.outputTable)
        self.pushButton_start.clicked.connect(self.print_packets)
        self.pushButton_pause.clicked.connect(self.pause)
        self.tableWidget.setHorizontalHeaderLabels(['No.', 'Time', 'Source', 'Destination', 'Protocol', 'len', 'Info'])
        # 列宽自动调整
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(5, QHeaderView.ResizeToContents)
        self.lines = []
        self.id = 0
        self.row = 0

    def outputTable(self, text):
        if self.id % 14 == 0:
            self.tableWidget.setRowCount(self.row + 1)
            self.row += 1
            # self.tableWidget.item(row+1,0).setBackground(QBrush(QColor(255, 0, 0)))
        if self.id % 2 == 0:
            self.tableWidget.setItem(int(self.id / 14), int(self.id % 14 / 2), QTableWidgetItem(text))
        if self.id % 14 == 0:
            if self.id != 0:
                if self.tableWidget.item(self.row - 2, 4).text() == 'tcp':
                    for i in range(7):
                        self.tableWidget.item(self.row - 2, i).setBackground(QBrush(QColor(228, 255, 199)))
                elif self.tableWidget.item(self.row - 2, 4).text() == 'arp':
                    for i in range(7):
                        self.tableWidget.item(self.row - 2, i).setBackground(QBrush(QColor(250, 240, 215)))
                elif self.tableWidget.item(self.row - 2, 4).text() == 'udp':
                    for i in range(7):
                        self.tableWidget.item(self.row - 2, i).setBackground(QBrush(QColor(218, 238, 255)))
        self.id += 1
        self.tableWidget.verticalScrollBar().setSliderPosition(self.row)

    def print_packets(self):
        device_packets()

    def pause(self):
        pause_capture()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = ControlBoard()
    ui.show()
    sys.exit(app.exec_())
