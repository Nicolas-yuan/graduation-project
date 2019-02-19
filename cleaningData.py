# -*- coding: utf-8 -*-

#数据清洗和流重组，将除tcp外的报文全部清洗

import struct
from operator import itemgetter

# 测试用
from showfile import *

class cleaning_function():

    Packet_cleaning = []    # 初始化list，用于存放清洗后的数据
    Packet_reassemble = []  # 初始化list，用于存放重组后的数据

    def cleaning_Data(self,Packet):

        start_time = ''       # 流开始时间
        end_time = ''         # 流结束时间
        stream_len = ''       # 流长度
        stream_Data = ''      # 流数据

        # 清洗，非TCP、Data为空的删除，通过倒序删除，不必考虑删完后列表长度改变问题
        for i in range(len(Packet)-1, -1, -1):     # range取头不取尾，所以倒序开始为长度减一，结束为-1
            if Packet[i][5] != 'TCP' or Packet[i][9] == '':
                Packet.pop(i)
            else:
                pass

        self.Packet_cleaning = Packet

        # 流重组


if __name__ == '__main__':
    Packet = read_function().read_file('tcp.pcap')
    Packet = sorted(Packet, key=itemgetter(1, 2, 3, 4, 7))
    cleaning_function().cleaning_Data(Packet)






