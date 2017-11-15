import socketserver
import time
from MySQL import MySQL
import configparser

from VerbHandler import VerbHandler
from HeartbeatReaderInstance import HeartbeatReaderInstance
from SleeperInstance import SleeperInstance

from ListenerInstance import ListenerInstance

class ReuseAddrTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

def main():
	config = configparser.ConfigParser()
	config.read('./fuzzy.conf')
	PORT = config['Server Config']["PORT"]

	print(str(config['Server Config']["PORT"]))

	heartbeatReaderInstance = HeartbeatReaderInstance()
	sleeperInstance = SleeperInstance()
	listenerInstance = ListenerInstance(config)
	httpd = ReuseAddrTCPServer(("", PORT), VerbHandler)
	print("Listening on port: {}".format(PORT))
	httpd.serve_forever()


	

if __name__ == '__main__':
	main()