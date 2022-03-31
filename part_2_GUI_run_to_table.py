from PyQt5 import QtCore, QtGui
import sys
from PyQt5.QtCore import QEventLoop, QTimer, QBasicTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView, QTreeWidgetItem
from PyQt5.QtGui import QBrush, QColor

from mainwindow import *
from part_2_parse_packets import *

import time
import random
from collections import Counter


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
        self.tableWidget.itemClicked.connect(self.part_2)
        self.tableWidget.setHorizontalHeaderLabels(['No.', 'Time', 'Source', 'Destination', 'Protocol', 'len', 'Info'])
        # 列宽自动调整
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(5, QHeaderView.ResizeToContents)
        # 利用定时器展示协议占比
        self.timer = QTimer()
        self.timer.start(500)
        self.timer.timeout.connect(self.set_progressBar)
        self.lines = []
        self.lines_protocol = []
        self.id = 0
        self.row = 0

    def outputTable(self, text):
        if self.id % 16 == 0:
            self.tableWidget.setRowCount(self.row + 1)
            self.row += 1
        if self.id % 2 == 0:
            if self.id % 16 == 14:
                self.lines.append(text)
            else:
                self.tableWidget.setItem(int(self.id / 16), int(self.id % 16 / 2), QTableWidgetItem(text))
                # 保存协议类型
                if self.id % 16 == 8:
                    self.lines_protocol.append(text)
        if self.id % 16 == 0:
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

    def set_progressBar(self):
        num = len(self.lines_protocol)
        if num != 0:
            protocol_count = Counter(self.lines_protocol)
            arp_num = protocol_count['arp']
            ipv6_num = protocol_count['ipv6']
            tcp_num = protocol_count['tcp']
            udp_num = protocol_count['udp']
            ip_num = tcp_num + udp_num
            self.progressBar.setValue(int(arp_num / num * 100))
            self.progressBar_3.setValue(int(ipv6_num / num * 100))
            self.progressBar_2.setValue(int(ip_num / num * 100))
            icmp_num = protocol_count['icmp']
            igmp_num = protocol_count['igmp']
            total_num = tcp_num + udp_num + icmp_num + igmp_num
            self.progressBar_4.setValue(int(tcp_num / total_num * 100))
            self.progressBar_5.setValue(int(udp_num / total_num * 100))
            self.progressBar_6.setValue(int((total_num - tcp_num - udp_num) / total_num * 100))

    def part_2(self, Item=None):
        if Item is None:
            return
        else:
            row = Item.row()  # 获取行数
            self.textBrowser.append(self.lines[row])
            raw_data = str.encode(self.lines[row][2:-1]).decode('unicode-escape').encode('ISO-8859-1')
            # 刷新树结构
            for i in range(self.treeWidget.topLevelItemCount()):
                self.treeWidget.takeTopLevelItem(0)
            # 设置最底层数据报
            frame = QTreeWidgetItem(self.treeWidget)
            frame.setBackground(0, QBrush(QColor(240, 240, 240)))
            frame_info = 'Frame:  ' + str(
                raw_data[16] * 256 + raw_data[17] + 14) + ' bytes captured on interface {padding}'
            frame.setText(0, frame_info)
            # 设置数据链路层数据报
            ethernet = QTreeWidgetItem(self.treeWidget)
            ethernet.setBackground(0, QBrush(QColor(240, 240, 240)))
            ethernet_info = 'Ethernet 2:  Src:  ' + ':'.join([str(hex(raw_data[6 + i]))[2:] for i in range(6)])
            ethernet_info += ',  Dst:  ' + ':'.join([str(hex(raw_data[i]))[2:] for i in range(6)])
            ethernet.setText(0, ethernet_info)
            # 设置链路层子节点
            eth_child1 = QTreeWidgetItem(ethernet)
            eth_child1.setText(0, 'Destination:  ' + ':'.join([str(hex(raw_data[i]))[2:] for i in range(6)]))
            eth_child2 = QTreeWidgetItem(ethernet)
            eth_child2.setText(0, 'Source:  ' + ':'.join([str(hex(raw_data[6 + i]))[2:] for i in range(6)]))
            eth_child3 = QTreeWidgetItem(ethernet)
            eth_protocol = base64.b16encode(raw_data[12:14]).decode()
            if eth_protocol == '0800':
                eth_child3.setText(0, 'Type:  IPv4(0x0800)')
            elif eth_protocol == '0806':
                eth_child3.setText(0, 'Type:  ARP(0x0806)')
            elif eth_protocol == '86DD':
                eth_child3.setText(0, 'Type:  IPv6(0x86DD)')
            # 设置网络层数据报
            network = QTreeWidgetItem(self.treeWidget)
            network.setBackground(0, QBrush(QColor(240, 240, 240)))
            eth_protocol = base64.b16encode(raw_data[12:14]).decode()
            if eth_protocol == '0800':
                # 处理ip数据报
                network_info = 'Internet Protocol Version 4,  Src:  ' + '.'.join(
                    [str(raw_data[26 + i]) for i in range(4)])
                network_info += ',  Dst:  ' + '.'.join([str(raw_data[30 + i]) for i in range(4)])
                network.setText(0, network_info)
                net_child1 = QTreeWidgetItem(network)
                net_child1.setText(0, 'Version:  4')
                net_child2 = QTreeWidgetItem(network)
                header_length = str((raw_data[14] - 64) * 4)
                net_child2.setText(0, 'Header Length:  ' + header_length)
                net_child3 = QTreeWidgetItem(network)
                net_child3.setText(0, 'Total Length:  ' + str(raw_data[16] * 256 + raw_data[17]))
                net_child4 = QTreeWidgetItem(network)
                net_child4.setText(0, 'Identification:  ' + str(hex(raw_data[18])) + str(hex(raw_data[19])[2:]))
                net_child5 = QTreeWidgetItem(network)
                net_child5.setText(0, 'Time To Live:  ' + str(raw_data[22]))
                net_child6 = QTreeWidgetItem(network)
                protocol_num_to_protocol = {'1': 'icmp', '2': 'igmp', '3': 'ggp', '5': 'st', '6': 'tcp', '8': 'egp',
                                            '9': 'igp', '11': 'nvp', '17': 'udp'}
                protocol = protocol_num_to_protocol[str(raw_data[23])]
                net_child6.setText(0, 'Protocol:  ' + protocol)
                net_child7 = QTreeWidgetItem(network)
                net_child7.setText(0, 'Source Address:  ' + '.'.join([str(raw_data[26 + i]) for i in range(4)]))
                net_child8 = QTreeWidgetItem(network)
                net_child8.setText(0, 'Destination Address:  ' + '.'.join([str(raw_data[30 + i]) for i in range(4)]))
                if protocol == 'tcp':
                    # 进一步处理tcp报文
                    tcp = QTreeWidgetItem(self.treeWidget)
                    tcp.setBackground(0, QBrush(QColor(240, 240, 240)))
                    tcp_frame = raw_data[14 + int(header_length):]
                    tcp_info = 'Transmission Control Protocol,  Src Port:  ' + str(tcp_frame[0] * 256 + tcp_frame[1])
                    tcp_info += ',  Dst Port:  ' + str(tcp_frame[2] * 256 + tcp_frame[3])
                    tcp.setText(0, tcp_info)
                    tcp_child1 = QTreeWidgetItem(tcp)
                    tcp_child1.setText(0, 'Source Port:  ' + str(tcp_frame[0] * 256 + tcp_frame[1]))
                    tcp_child2 = QTreeWidgetItem(tcp)
                    tcp_child2.setText(0, 'Destination Port:  ' + str(tcp_frame[2] * 256 + tcp_frame[3]))
                    # 处理tcp_flag展示
                    tcp_flag_list = ['URG', 'ACK', 'PSH', 'RST', 'SYN', 'FIN']
                    tcp_flag = tcp_frame[13]
                    res = []
                    tcp_flag = bin(tcp_flag)
                    for i in range(len(tcp_flag) - 2):
                        if tcp_flag[i + 2] == '1':
                            res.append(tcp_flag_list[i + (8 - len(tcp_flag))])
                    res_flag = ','.join(res)
                    tcp_child3 = QTreeWidgetItem(tcp)
                    tcp_child3.setText(0, 'Flags:  ' + res_flag)
                elif protocol == 'udp':
                    # 进一步处理udp报文
                    udp = QTreeWidgetItem(self.treeWidget)
                    udp.setBackground(0, QBrush(QColor(240, 240, 240)))
                    udp_frame = raw_data[14 + int(header_length):]
                    udp_info = 'User Datagram Protocol,  Src Port:  ' + str(udp_frame[0] * 256 + udp_frame[1])
                    udp_info += ',  Dst Port:  ' + str(udp_frame[2] * 256 + udp_frame[3])
                    udp.setText(0, udp_info)
                    udp_child1 = QTreeWidgetItem(udp)
                    udp_child1.setText(0, 'Source Port:  ' + str(udp_frame[0] * 256 + udp_frame[1]))
                    udp_child2 = QTreeWidgetItem(udp)
                    udp_child2.setText(0, 'Destination Port:  ' + str(udp_frame[2] * 256 + udp_frame[3]))
                elif protocol == 'igmp':
                    # 进一步处理igmp报文
                    igmp = QTreeWidgetItem(self.treeWidget)
                    igmp.setBackground(0, QBrush(QColor(240, 240, 240)))
                    igmp.setText(0, 'Internet Group Management Protocol')
            elif eth_protocol == '0806':
                # 处理arp数据报
                network_info = 'Address Resolution Protocol '
                if raw_data[21] == 1:
                    network_info += '(request)'
                elif raw_data[21] == 2:
                    network_info += '(reply)'
                else:
                    network_info += 'unknown'
                network.setText(0, network_info)
            elif eth_protocol == '86DD':
                # 处理ipv6数据报
                network.setText(0, 'IPv6  padding')
            QApplication.processEvents()

    def print_packets(self):
        device_packets()

    def pause(self):
        pause_capture()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = ControlBoard()
    ui.show()
    sys.exit(app.exec_())
