import socket

IP_LIST = []

for ip in range(255):
		addr = socket.gethostbyname("192.168.1."+str(ip))
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(0.2)
		result = sock.connect_ex((addr, 80))
		if result == 0:
			IP_LIST.append(addr)
		sock.close()

print(IP_LIST)

