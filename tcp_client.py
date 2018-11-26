#!/usr/bin/env python3

# for SDR must have pkg-config and libusb
# and pyrtlsdr
# https://witestlab.poly.edu/blog/capture-and-decode-fm-radio/

import socket
import sys

TCP_IP = ''
TCP_PORT = 4000
BUFFER_SIZE = 1024 #might want this to be larger

def runTCPClient():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # set up tcp and not udp
	s.connect((TCP_IP, TCP_PORT))

	print("Running TCP Client", socket.gethostbyname(socket.gethostname()))
	s.send("New connection.".encode())
	command = ""
	while command != "exit":
		command = input("Please enter a command: ")
		s.send(command.encode())
		message = s.recv(1024).decode()
		print(message)		
    
	s.close()


def main(args):
	TCP_IP = args[1]
	runTCPClient()

if __name__ == "__main__":
    main(sys.argv)