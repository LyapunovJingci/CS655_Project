# -*- coding=utf-8 -*-

import socket
import os
import sys
import struct

def socket_client():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('localhost',23456))
    except socket.error as msg:
        print(msg)
        sys.exit(1)

    #print (s.recv(1024))

    while 1:
        filepath = os.path.join(os.path.dirname(__file__) + '/image/anime.jpg')
        if os.path.isfile(filepath):
            fileinfo_size = struct.calcsize('128sl')
            fhead = struct.pack('128sl', bytes(os.path.basename(filepath).encode('utf-8')),os.stat(filepath).st_size)
            s.send(fhead)
            print ('client filepath: {0}'.format(filepath))
            fp = open(filepath, 'rb')
            while 1:
                data = fp.read(1024)
                if not data:
                    print ('{0} file send over...'.format(filepath))
                    break
                s.send(data)
        s.close()
        break

if __name__ == '__main__':
    socket_client()