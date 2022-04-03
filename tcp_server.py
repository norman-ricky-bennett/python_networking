#! /usr/bin/env python3
# This is a simple TCP server 

import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))

server.listen(5)

print("[*] listening on %s:%d" % (bind_ip,bind_port))

# client-handling thread 

def handle_client(client_socket):

	# print what the client sends
	request = client_socket.send("ACK!")

	client_socket.close()

while True:

	client,addr = server.accept()

	print("[*] Accepted connection from: %s:%d" % (addr[0],addr[1]))