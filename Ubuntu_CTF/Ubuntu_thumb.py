import socket
import time

while 1:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_address = ('52.78.202.173',10001)
	sock.connect(server_address);

	recvdata = sock.recv(10000)
	print(recvdata)

	time.sleep(0.1)

	senddata = "\x00"*32
	sock.send(senddata)

	time.sleep(0.1)

	recvdata = sock.recv(10000)
	print(recvdata)

sock.close()