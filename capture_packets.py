from winpcapy import WinPcapUtils
from winpcapy import WinPcapDevices
import time
import numpy as np
import multiprocessing

flag = np.zeros((len(list(WinPcapDevices.list_devices().values()))))
# flag = 0


def show_flag():
    global flag
    while True:
        print(flag)


def packet_callback3(win_pcap, param, header, pkt_data):
    global flag
    flag[3] += 1
    print(flag)


def packet_callback4(win_pcap, param, header, pkt_data):
    global flag
    flag[4] += 1
    print(flag)


def packet_callback5(win_pcap, param, header, pkt_data):
    global flag
    flag[5] += 1
    print(flag)


def device_show():
    # 这里要判断从哪一张网卡上抓包
    # 显示各网卡上有多少数据包流过
    print('本机网卡列表如下：')
    device_name = list(WinPcapDevices.list_devices().values())
    print(device_name)


def device_packets_num(i):
    # 显示各网卡上有多少数据包流过
    # 使用多线程技术
    device_true_name = list(WinPcapDevices.list_devices().keys())
    WinPcapUtils.capture_on_device_name(device_true_name[i], eval('packet_callback'+str(i)))


if __name__ == '__main__':
    device_show()
    # p3 = multiprocessing.Process(target=device_packets_num, args=(3,))
    # p4 = multiprocessing.Process(target=device_packets_num, args=(4,))
    p5 = multiprocessing.Process(target=device_packets_num, args=(5,))

    # p3.start()
    # p4.start()
    p5.start()

