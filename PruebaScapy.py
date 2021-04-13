from scapy.layers.inet import *
from scapy.sendrecv import sniff, AsyncSniffer, send
import socket
import tkinter as tk
from scapy.utils import wrpcap, wireshark, rdpcap


# cache = []
#
p = Ether() / IP(src='192.168.1.2', dst='192.168.1.3') / TCP(sport=3000, dport=4000)
#
# for i in range(0, 10):
#     p = Ether() / IP(src='192.168.1.2', dst='192.168.1.3') / TCP(sport=3000, dport=4000)
#     cache.append(p)

# p[TCP].dport = 30
# print(p[TCP].dport)

# t = AsyncSniffer()
# t.start()


# t.join()
# p.conversations()
# send(IP(dst="192.168.2.99")/ICMP())


# print(cache)

# wireshark(cache, )
# wrpcap("./temp.cap", p)
# p.show()
# print(p.show(dump=True))

# pkt = IP()/TCP()
# wrpcap('./packlist.pcap', pkt, append=True)

scapy_cap = rdpcap('packlist.pcap')

for packet in scapy_cap:
    if 'MAC' in packet and 'IP' in packet and 'TCP' in packet or 'UDP' in packet:
        if 'TCP' in packet:
            inf = 'TCP'
        else:
            inf = 'UDP'
        print('src MAC:', packet[Ether].src, 'dst MAC', packet[Ether].dst, 'src:', packet[IP].src, 'dst:',
              packet[IP].dst, 'sport:', packet[inf].sport, 'dport:', packet[inf].sport)

# print(len(pkt))
#
# for x in range(0,len(pkt)):
#     print(pkt[x])
#
# for i in pkt:
#     print('1')
#     print(i['IP'].src)






def clicked():
    scapy_cap = rdpcap('packlist.pcap')
    for packet in scapy_cap:
        if 'LLC' in packet and 'IP' in packet and 'TCP' in packet or 'UDP' in packet:
            if 'TCP' in packet:
                inf = 'TCP'
            else:
                inf = 'UDP'
            print('src MAC:',packet['LLC'].ssap,'dst MAC',packet['LLC'].dsap,'src:', packet[IP].src, 'dst:', packet[IP].dst, 'sport:', packet[inf].sport, 'dport:', packet[inf].sport)



