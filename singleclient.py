import socket
import os
import sys
import struct
import time
import cgi
import cgitb;

def size_format(size):
    if size < 1000:
        return '%i' % size + 'size'
    elif 1000 <= size < 1000000:
        return '%.1f' % float(size/1000) + 'KB'
    elif 1000000 <= size < 1000000000:
        return '%.1f' % float(size/1000000) + 'MB'
    elif 1000000000 <= size < 1000000000000:
        return '%.1f' % float(size/1000000000) + 'GB'
    elif 1000000000000 <= size:
        return '%.1f' % float(size/1000000000000) + 'TB'

def socket_client():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('server.geni.ch-geni-net.genirack.nyu.edu',1218))
    except socket.error as msg:
        print(msg)
        sys.exit(1)

    linkStart = time.time();
    while 1:
        # send first picture
        filepath = os.path.join(os.path.dirname(__file__) + '/image/obama.jpg')
        if os.path.isfile(filepath):
            size1 = os.path.getsize(filepath)
            print(size_format(size1))
            fileinfo_size = struct.calcsize('128sl')
            fhead = struct.pack('128sl', bytes(os.path.basename(filepath).encode('utf-8')), os.stat(filepath).st_size)
            s.send(fhead)
            #print('client filepath: {0}'.format(filepath))
            fp = open(filepath, 'rb')
            while 1:
                data = fp.read(1024)
                if not data:
                    print('{0} file send over...'.format(filepath))
                    break
                s.send(data)
            firstFileTime = time.time()
        s.close()
        break