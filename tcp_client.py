#!/usr/bin/env python3

# for SDR must have pkg-config and libusb
# and pyrtlsdr
# https://witestlab.poly.edu/blog/capture-and-decode-fm-radio/

import socket
import sys
from rtlsdr import RtlSdr

TCP_IP = ''
TCP_PORT = 4000
BUFFER_SIZE = 1024 #might want this to be larger

def runWebServer():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # set up tcp and not udp
	s.bind((TCP_IP, TCP_PORT))
	s.listen(5) #arbitrary value I think

	print("Running TCP Client", socket.gethostbyname(socket.gethostname()))

	while True:
		# conn, addr = s.accept() #get IP and port for connecting application

		# data = conn.recv(BUFFER_SIZE)
		# print("Received data:\n", data, "\n")

		#this behavior is weird in a while loop
		sdr = RtlSdr()
		sdr.sample_rate = 2.048e6
		sdr.center_freq = 70e6
		sdr.freq_correction = 60
		sdr.gain = 'auto'
		print(sdr.read_samples(512))

        
		# conn.close()


def main(args):
	runWebServer()

if __name__ == "__main__":
    main(sys.argv)

#gotta figure out how this works
# def sendToSound(data):
    