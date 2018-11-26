#!/usr/bin/env python3

import socket
import sys
import sounddevice as sd
import numpy as np
import random

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
		data = conn.recv(BUFFER_SIZE)
		message = data.decode()
		print(message)

		while message != "exit":
			
			# this is the bytes
			data = conn.recv(BUFFER_SIZE)

			# this is the string 
			message = data.decode()

			if message == "exit":
				break
			print(message)
			
			conn.send("Message recieved.".encode())

			#Mansoor's shit 

			# create header 
			# encrypt the data 
			# bit by bit, create sound 
			# create the array of tones
			# play out loud 

			

			#Mansoor's shit ends 
			data = ''.join(format(x, 'b') for x in bytearray(data))
			# generate one time pad 

			print('data in binary:\n', data)

			sd.play(bytearray(data.encode()))





		conn.close()


def main(args):
	runWebServer()

if __name__ == "__main__":
    main(sys.argv)

#gotta figure out how this works
# def sendToSound(data):
    