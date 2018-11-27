#!/usr/bin/env python3

import socket
import sys
import sounddevice as sd
import numpy as np
import random

TCP_IP = ''
TCP_PORT = 4000
BUFFER_SIZE = 1024 #might want this to be larger
global loc_in_file

def runWebServer():
	loc_in_file = 0
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # set up tcp and not udp
	s.bind((TCP_IP, TCP_PORT))
	s.listen(5) #arbitrary value I think

	print("Running Webserver", socket.gethostbyname(socket.gethostname()))

	while True:
		conn, addr = s.accept() #get IP and port for connecting application

		data = bytearray(conn.recv(BUFFER_SIZE))

		## play bytes on sound card
		print(data)

		#custom packet structure


		#generate key file

		# with open('key.txt', 'w+') as pad:
		# 	bits = ['0', '1']
		# 	key = ""
		# 	for x in range(len(data)):
		# 		key += bits[random.randint(0, 1)]
		# 	pad.write(key)

		#encrypt data
		with open('key.text', 'r') as pad:
			for burn in range(loc_in_file):
				pad.next()
			line = pad.readline()
		loc_in_file += 1
		


		key = bytearray(key.encode('ascii'))
		newdata = []
		for byte in len(data):
			newdata.append(str(key[byte]) ^ str(data[byte]))
		newdata = "".join(newdata)
		print('data after pad', newdata)

		sd.play(newdata)


        
		conn.close()


def main(args):
	runWebServer()

if __name__ == "__main__":
    main(sys.argv)

#gotta figure out how this works
# def sendToSound(data):
    