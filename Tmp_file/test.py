from winpcapy import WinPcapUtils
from winpcapy import WinPcapDevices
import sys
import base64


# 这里要判断从哪一张网卡上抓包
# print(WinPcapDevices.list_devices())
# print(WinPcapDevices.get_matching_device("*Ethernet*"))

def packet_callback(win_pcap, param, header, pkt_data):
    # Assuming IP (for real parsing use modules like dpkt)
    ip_frame = pkt_data[14:]
    # Parse ips
    src_ip = ".".join([str(ord(b)) for b in ip_frame[0xc:0x10]])
    dst_ip = ".".join([str(ord(b)) for b in ip_frame[0x10:0x14]])
    print("%s -> %s" % (src_ip, dst_ip))


def easy_packet_callback(win_pcap, param, header, pkt_data):
    ip_frame = pkt_data[14:]
    src_ip = ".".join([str(int(base64.b16encode(ip_frame[12:16])[2 * i:2 * (i + 1)].decode(), 16)) for i in range(4)])
    dst_ip = ".".join([str(int(base64.b16encode(ip_frame[16:20])[2 * i:2 * (i + 1)].decode(), 16)) for i in range(4)])
    print(src_ip + ' -> ' + dst_ip)
    # sys.exit(0)


def start():
    # 实现了实时抓包并打印每个包的源和目的ip
    WinPcapUtils.capture_on_device_name('\\Device\\NPF_{2603A7A3-97D9-408D-B688-30747C2C5B27}', easy_packet_callback)


if __name__ == '__main__':
    start()
