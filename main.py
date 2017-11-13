import socketserver
import time
from MySQL import MySQL

from VerbHandler import VerbHandler

class ReuseAddrTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

def main():
	PORT = 5000
	httpd = ReuseAddrTCPServer(("", PORT), VerbHandler)
	print("Listening on port: {}".format(PORT))
	httpd.serve_forever()

	

if __name__ == '__main__':
	main()