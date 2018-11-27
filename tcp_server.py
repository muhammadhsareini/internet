#!/usr/bin/env python3

import socket
import sys
import sounddevice as sd
import numpy as np
import random
import array
from pysine import sine

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

			# create header 
			packet = str(packetize(str(data)))

			#encrypt data
			with open('key.txt', 'r') as pad:
				for burn in range(loc_in_file):
					pad.next()
				line = pad.readline()
			#increment reading location in one time pad key file
			loc_in_file += 1
			key = array.array('B', line.encode('ascii'))
			packet = array.array('B', packet.encode('ascii'))
			for byte in range(len(packet)):
				packet[byte] ^= key[byte]
			
			# convert to bit by bit binary
			packet = ''.join(format(x, 'b') for x in bytearray(packet))
			print('data in binary:\n', packet)

			sd.play(bytearray(packet.encode()))

			# PLAYING SOUND 
			# pip install pysine
			play_sound(packet)

		conn.close()

def play_sound(byteString):
	# pass in the binary representation as a string (no spaces)
	for bit in byteString:
		if int(bit) == 1:
			sine(frequency=440, duration=1.0)
			print("bit: ", bit)
		if int(bit) == 0:
			sine(frequency=1000, duration=1.0)
			print("bit: ", bit)


# max payload size is 255
# first byte is number of bytes in message
# second byte is a parity byte
# next bytes are the encrypted data
def packetize(data):
    if len(data) > 255:
        print("No messages longer than 255")
    packet = '\0'+'\0'+data
    packet = array.array('B', packet.encode('ascii'))

    byte1 = packet[0]
    byte2 = packet[1]
    byte1 = len(data)
	#calculate byte parity checksum
    for i in range(len(data)):
        packet[1] ^= packet[i+2]
    print(packet)

	#set up packet
    result = array.array('B', data.encode('ascii'))
    result.insert(0,byte1)
    result.insert(1,packet[1])

    print(result, result.tostring())
    return result.tostring()
			
def main(args):
	runWebServer()

if __name__ == "__main__":
    main(sys.argv)

    