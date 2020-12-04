import requests
import json
import numpy as np
import cv2
import base64
import os
import socket


def getByte(path):
    with open(path, 'rb') as f:
        img_byte = base64.b64encode(f.read())
    img_str = img_byte.decode('ascii')
    return img_str

def getImage(code):
    decode1 = code.encode('ascii')
    decode2 = base64.b64decode(decode1)
    img_np = np.frombuffer(decode2, np.uint8)
    img = cv2.imdecode(img_np, cv2.COLOR_RGB2BGR)
    return img

def socketConnect():
    hostname = 'localhost'
    port = 655
    addr = (hostname, port)

    clientsock = socket.socket()
    clientsock.connect(addr)

    say = input("Input message:")
    clientsock.send(bytes(say, encoding='gbk'))
    recvdata = clientsock.recv(1024)
    print(str(recvdata, encoding='gbk'))
    clientsock.close()

def sendImage(img_str):
    hostname = 'localhost'
    port = 655
    addr = (hostname,port)
    connect = socket.socket().connect(addr)
    thisStr = bytes(img_str,encoding='gbk')
    print(thisStr)
    connect.send(thisStr)
    receivedata =  connect.recv(1024)
    print(str(receivedata, encoding='gbk'))
    connect.close()

path = os.path.join(os.path.dirname(__file__) + '/image/anime.jpg')
img_str = getByte(path)

print(img_str)
img = getImage(img_str)

socketConnect()
sendImage(img_str)

# 显示图像
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()