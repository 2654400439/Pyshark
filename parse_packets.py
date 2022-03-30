from winpcapy import WinPcapUtils
from winpcapy import WinPcapDevices
import time
import base64
import sys

# 按类似wireshark格式进行包展示
# 序号，时间戳，源地址，目的地址，协议，包长度，其他信息
# 能分类tcp，udp，icmp，arp，dns，tls和ipv6
num = 0
flag = 0


def Parse_ip(pkt_data):
    time_stamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    ip_frame = pkt_data[14:]
    src_ip = ".".join([str(int(base64.b16encode(ip_frame[12:16])[2 * i:2 * (i + 1)].decode(), 16)) for i in range(4)])
    dst_ip = ".".join([str(int(base64.b16encode(ip_frame[16:20])[2 * i:2 * (i + 1)].decode(), 16)) for i in range(4)])
    protocol_num = ip_frame[9]
    try:
        protocol_num_to_protocol = {'1': 'icmp', '2': 'igmp', '6': 'tcp', '17': 'udp'}
        protocol = protocol_num_to_protocol[str(protocol_num)]
    except:
        protocol = protocol_num
    print(num, time_stamp, src_ip, dst_ip, protocol)


def Parse_arp(pkt_data):
    time_stamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    protocol = 'arp'
    src_ip = ':'.join([str(hex(pkt_data[6 + i]))[2:] for i in range(6)])
    dst_ip = 'broadcast'
    print(num, time_stamp, src_ip, dst_ip, protocol)


def Parse_ipv6(pkt_data):
    time_stamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    protocol = 'ipv6'
    src_ip = 'padding'
    dst_ip = 'padding'
    print(num, time_stamp, src_ip, dst_ip, protocol)


def Parse_packets(win_pcap, param, header, pkt_data):
    global num
    global flag
    if flag == 1:
        win_pcap.stop()
    num += 1
    eth_protocol = base64.b16encode(pkt_data[12:14]).decode()

    if eth_protocol == '0800':
        # 封装的是ip数据报文
        Parse_ip(pkt_data)
    elif eth_protocol == '0806':
        # 封装的是arp数据报文
        Parse_arp(pkt_data)
    elif eth_protocol == '86DD':
        # 封装的是ipv6数据报文
        Parse_ipv6(pkt_data)
    else:
        print('else')
        print(eth_protocol)


def device_packets():
    # 按网卡名称抓包
    global flag
    flag = 0
    device_true_name = list(WinPcapDevices.list_devices().keys())
    WinPcapUtils.capture_on_device_name(device_true_name[-1], Parse_packets)


def pause_capture():
    global flag
    flag = 1


if __name__ == '__main__':
    device_packets()
