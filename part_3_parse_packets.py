from winpcapy import WinPcapUtils
from winpcapy import WinPcapDevices
from winpcapy import WinPcap
import time
from multiprocessing import Process
import multiprocessing
import eventlet
from func_timeout import func_set_timeout
import func_timeout

num = 0
flag = 0
flow_bool_flag = [0 for i in range(len(WinPcapDevices.list_devices()))]
now_card = 0


def flow_bool(win_pcap, param, header, pkt_data):
    i = 0
    if i == 0:
        print('有包')
    i += 1


def device_packets_bool(num):
    # 按网卡名称抓包
    global flag
    global now_card
    now_card = int(num)
    flag = 0
    device_true_name = list(WinPcapDevices.list_devices().keys())
    # WinPcapUtils.capture_on_device_name(device_true_name[num], flow_bool)
    WinPcap(device_true_name[num], None, 0)


def make_a_process(num):
    p = Process(target=device_packets_bool, args=(num,))
    p.start()
    time.sleep(2)
    if p.is_alive:
        p.terminate()
        p.join()
        print('结束进程', num)


@func_set_timeout(2)
def capture(num):
    print('执行', num)
    device_true_name = list(WinPcapDevices.list_devices().keys())
    with WinPcap(device_true_name[num]) as capture:
        capture.run(callback=flow_bool, limit=1)


if __name__ == '__main__':
    try:
        capture(0)
    except func_timeout.exceptions.FunctionTimedOut:
        print('超时')
