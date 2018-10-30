import socket
import sys
import binascii

UDP_IP = ''
UDP_PORT = 53
BUFFER_SIZE = 4096

## only works in python2

def runDNS(webServerIP):

	## dns lookup table
	table = {}
	table["blacksite.secret"] = webServerIP

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # set up udp
	s.bind((UDP_IP, UDP_PORT))

	print("Running DNS Server", socket.gethostbyname(socket.gethostname()))

	while True:
		data, addr = s.recvfrom(BUFFER_SIZE)
		domain = parse_packet(data)
		# print("searching domain")
		# print(domain)
		# print(domain == "blacksitesecret")
		# if domain in table:
		# 	print("found:")
		# 	print(domain)
		# 	ip = table[domain]
		# 	response_packet(data, domain, ip)
		# else:
		# 	print("domain not found:") 
		# 	print(domain)



## parse packet and return relevant data
def parse_packet(data):
	hex_form = data.hex()
	print("hex:")
	print(hex_form)
	print("binary:")
	# print(bytes.fromhex(hex_form))
	transaction_id = hex_form[0:4]
	flags = hex_form[4:8]
	query = hex_form[26:]
	query_name = query[:-4]
	print(query_name)
	# return query_name



## craft the response packeet 
def response_packet(data, domain, ip):
	return

def main(args):
    webServerIP= args[1]
    runDNS(webServerIP)

if __name__ == "__main__":
    main(sys.argv)
