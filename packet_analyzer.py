#! /usr/bin/env python3

import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

while True: 

	print(socket.recvfrom(65565))