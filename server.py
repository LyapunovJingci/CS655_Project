# -*- coding=utf-8 -*-
import socket
import threading
import sys
import os
import struct
import face_recognition as fr

def compare_faces(file1, file2):
    #fp1 = os.path.join(os.path.dirname(__file__) + file1)
    #fp2 = os.path.join(os.path.dirname(__file__) + file2)
    #fp1 = open(file1, 'wb')

	image1 = fr.load_image_file(file1)
	image2 = fr.load_image_file(file2)

	image1_encoding = fr.face_encodings(image1)[0]
	image2_encoding = fr.face_encodings(image2)[0]

	results = fr.compare_faces([image1_encoding], image2_encoding)
	return results[0]

def socket_service():
    try:
        HOST = socket.gethostname()
        print(HOST)
        PORT = 1218
        print(PORT)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(10)
    except socket.error as msg:
        print(msg)
        sys.exit(1)
    print ("Waiting...")

    while 1:
        conn, addr = s.accept()
        t = threading.Thread(target=deal_data, args=(conn, addr))
        t.start()

def deal_data(conn, addr):
    print ('Accept new connection from {0}'.format(addr))
    while 1:
        fileinfo_size = struct.calcsize('128sq')
        buf = conn.recv(fileinfo_size)
        if buf:
            filename1, filesize = struct.unpack('128sq', buf)
            fn1 = filename1.strip(str.encode('\00'))
            new_filename1 = os.path.join(str.encode('./receive/'), str.encode('new_') + fn1)
            fp1 = str.encode('./receive/new_') + fn1
            print('file new name is {0}, filesize if {1}'.format(new_filename1, filesize))

            recvd_size = 0  # the size of the file has been received
            fp = open(new_filename1, 'wb')
            print("start receiving...")
            while not recvd_size == filesize:
                print(recvd_size)
                if filesize - recvd_size > 1024:
                    data = conn.recv(1024)
                    recvd_size += len(data)
                else:
                    data = conn.recv(filesize - recvd_size)
                    recvd_size = filesize
                fp.write(data)
            fp.close()
            print("end receive...")
            break

    while 1:
        fileinfo_size = struct.calcsize('128sq')
        buf = conn.recv(fileinfo_size)
        if buf:
            filename2, filesize = struct.unpack('128sq', buf)
            fn2 = filename2.strip(str.encode('\00'))
            new_filename2 = os.path.join(str.encode('./receive/'), str.encode('new_') + fn2)
            fp2 = str.encode('./receive/new_') + fn2
            print('file new name is {0}, filesize if {1}'.format(new_filename2, filesize))

            recvd_size = 0  # the size of the file has been received
            fp = open(new_filename2, 'wb')
            print("start receiving...")
            while not recvd_size == filesize:
                if filesize - recvd_size > 1024:
                    data = conn.recv(1024)
                    recvd_size += len(data)
                else:
                    data = conn.recv(filesize - recvd_size)
                    recvd_size = filesize
                fp.write(data)
            fp.close()
            print("end receive...")
            break

    # fp2 = open(nfn2, 'wb')
    # print(fp1)
    if(compare_faces(fp1, fp2)):
        result = "same people!"
    else:
        result = "not same"
    print(result)
    msg = result.encode("utf-8")
    conn.send(msg)
    conn.close()


if __name__ == '__main__':
    socket_service()