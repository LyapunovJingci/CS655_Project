import socket
hostname = 'localhost'
port = 655
addr = (hostname,port)
srv = socket.socket()
srv.bind(addr)
srv.listen(5)
print("waitting connect")
while True:
 connect_socket,client_addr = srv.accept()
 print(client_addr)
 recevent = connect_socket.recv(1024)
 print(str(recevent,encoding='gbk'))
 connect_socket.send(bytes("hi client",encoding='gbk'))
 connect_socket.close()