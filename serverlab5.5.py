import socket
import sys
import json

s = socket.socket()
print("Socket created")

port = 8088

try:
	s.bind(('', port))
	print("Socket binded to " + str(port))
except:
	print("Error in  binding")
	s.close
s.listen(5)
print("Socket listening...")

while True:
	c, addr = s.accept()
	print("Received file from " + str(addr))
	data = c.recv(1024)
	data = data.decode("utf-8")
	dataJ = json.loads(data)
	c.send(b"File received by the server.")
	file = open(dataJ.split("\n",1)[0],"w")
	file.write(dataJ.split("\n",1)[1])

c.close()
