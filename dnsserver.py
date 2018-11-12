#!/usr/bin/env python3

import socket
import sys
import binascii

UDP_IP = ''
UDP_PORT = 53
BUFFER_SIZE = 4096



def runDNS(webServerIP):

	## dns lookup table
	table = {"google.com" : "8.8.8.8", "www.google.com" : "8.8.8.8", "blacksite.secret" : webServerIP}

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # set up udp
	s.bind((UDP_IP, UDP_PORT))

	print("Running DNS Server", socket.gethostbyname(socket.gethostname()))

	while True:
		data, addr = s.recvfrom(BUFFER_SIZE)
		# print(addr)
		domain = parse_packet(data)

		query = domain[1]
		domain = domain[0]

		if domain in table:
			print(domain + " : " + table[domain])

			## send a DNS packet response

			# the dns request
			trans_id = query[:4]
			# change flags for response
			print('original query', query)
			response_flags = "8180"
			# updated_response = trans_id + response_flags + "0001000100000000" + query
			updated_response = trans_id + response_flags + "0001000100000000" + query[24:]
			# add the "answer" part to the response

			# add all info until ip
			updated_response += "C00C0001000100000E100004"
			# updated_response += "C00C000100010000000000000E100004"
			# add ip address
			ip = table[domain]
			ip = ip.split(".")
			
			# convert ip to hex
			hex_ip = ""
			for i in ip:
				hex_num = hex(int(i)).replace("0x","")
				if len(hex_num) == 1:
					hex_num = "0" + hex_num

				hex_ip += hex_num

			# print(hex_ip)
			updated_response+=hex_ip

			updated_response = updated_response.upper()
			print('updated response', updated_response)

			packet = bytes.fromhex(updated_response)
			
			
			## send the packet
			s.sendto(packet,addr)

		else:
			print(domain + " not in DNS server")

# 192.168.18.23

## parse packet and return relevant data
def parse_packet(data):
	hex_form = data.hex()
	transaction_id = hex_form[0:4]
	flags = hex_form[4:8]
	query = hex_form[24:]
	# query += '00'
	# print(query)
	domain = []
	total = 2
	print(query)
	count = int(query[0:2], 16) * 2
	while count != 0:
		domain.append("".join(query[total:total+count]))
		total += count
		count = int(query[total:total+2], 16) * 2
		total+=2

	# join on ".", but represent in hex 
	domain = "2E".join(domain)
	domain = bytes.fromhex(domain).decode('utf-8')
	return domain, hex_form


def main(args):
    webServerIP= args[1]
    runDNS(webServerIP)

if __name__ == "__main__":
    main(sys.argv)
