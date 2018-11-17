#!/usr/bin/env python3

import socket
import sys
import sounddevice as sd
import numpy as np

TCP_IP = ''
TCP_PORT = 4000
BUFFER_SIZE = 1024 #might want this to be larger

def runWebServer():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # set up tcp and not udp
	s.bind((TCP_IP, TCP_PORT))
	s.listen(5) #arbitrary value I think

	print("Running Webserver", socket.gethostbyname(socket.gethostname()))

	while True:
		conn, addr = s.accept() #get IP and port for connecting application

		data = bytearray(conn.recv(BUFFER_SIZE))

		## play bytes on sound card
		print(data)
		sd.play(data)


        
		conn.close()


def main(args):
	runWebServer()

if __name__ == "__main__":
    main(sys.argv)

#gotta figure out how this works
# def sendToSound(data):
    