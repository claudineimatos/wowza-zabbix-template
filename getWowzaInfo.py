#!/bin/env python
# Vicente Dominguez
# -a conn - Global connections
# -a appnum - Global application(streaming) num

import urllib2, base64, sys, getopt
import xml.etree.ElementTree as ET

# Default values
username = "admin"
password = "admin"
host = "localhost"
port = "8086"
getInfo = "None"

##

def Usage ():
        print "Usage: getWowzaInfo.py -u user -p password -h 127.0.0.1 -P 8086 -a [conn|appnum]"
        sys.exit(2)

def getConnectionsCurrent():
        print xmlroot.find('ConnectionsCurrent').text

def getMessagesInBytesRate():
        print xmlroot.find('MessagesInBytesRate').text

def getMessagesOutBytesRate():
        print xmlroot.find('MessagesOutBytesRate').text

def getConnectionsTotalAccepted():
        print xmlroot.find('ConnectionsTotalAccepted').text

def getConnectionsTotalRejected():
        print xmlroot.find('ConnectionsTotalRejected').text

def getCurrentStreams():
        Application =  xmlroot.findall('VHost/Application')
        print len(Application)

def unknown():
        print "unknown"

##


def main (username,password,host,port,getInfo):

	global xmlroot    
	argv = sys.argv[1:]	
    
	if (len(argv) < 1):
		Usage()   
    
	try :
			opts, args = getopt.getopt(argv, "u:p:h:P:a:")

			# Assign parameters as variables
			for opt, arg in opts :
					if opt == "-u" :
							username = arg
					if opt == "-p" :
							password = arg
					if opt == "-h" :
							host = arg
					if opt == "-P" :
							port = arg
					if opt == "-a" :
							getInfo = arg
	except :
					Usage()

	url="http://" + host + ":" + port + "/connectioncounts/"

	pwdman = urllib2.HTTPPasswordMgrWithDefaultRealm()
	pwdman.add_password(None, url, username, password)

	auth_handler = urllib2.HTTPDigestAuthHandler(pwdman)
	opener = urllib2.build_opener(auth_handler)

	res = opener.open(url)

	xmlroot = ET.fromstring(res.read())

	if ( getInfo == "conn"):
			getConnectionsCurrent()
	elif ( getInfo == "appnum"):
			getCurrentStreams()
	elif ( getInfo == "bytesin"):
			getMessagesInBytesRate()
	elif ( getInfo == "bytesout"):
			getMessagesOutBytesRate()
	elif ( getInfo == "totalconnaccepted"):
			getConnectionsTotalAccepted()
	elif ( getInfo == "totalconnrejected"):
			getConnectionsTotalRejected()
	else:
			unknown()
			sys.exit(1)



if __name__ == "__main__":

    main(username,password,host,port,getInfo)
