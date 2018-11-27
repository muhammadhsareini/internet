import random

def key_gen():
	with open('key.txt', 'w+') as pad:
		key = ""
		for y in range(256):
			for x in range(128):
				key += str(random.randint(0, 1))
			key += '\n'
			pad.write(key)
			key = ""
		

key_gen()