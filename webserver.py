#!/usr/bin/env python3

import socket
import sys

TCP_IP = ''
TCP_PORT = 80
BUFFER_SIZE = 1024

def runWebServer():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # set up tcp and not udp
	s.bind((TCP_IP, TCP_PORT))
	s.listen(5)

	print("Running Webserver", socket.gethostbyname(socket.gethostname()))

	while True:
		conn, addr = s.accept() #get IP and port for connecting application

		data = conn.recv(BUFFER_SIZE)
		print("Received data:\n", data, "\n")

		httpResponse = """HTTP/1.1 200 OK
		Server: Apache/2.2.8 (Ubuntu)
		Accept-Ranges: bytes
		Content-Length: 50
		Connection: close
		Content-Type: text/html

Secret Black Site: """

		## data is the ip address
		httpResponse += str(addr[0])

		conn.send(httpResponse.encode())

		conn.close()


def main(args):
	runWebServer()

if __name__ == "__main__":
    main(sys.argv)