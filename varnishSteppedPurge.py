#!/usr/bin/python

import telnetlib
import time
"""
SAMPLE OUTPUT:
        telnet varnish1.mydomain.com 8909
        PURGE /articles/* HTTP/1.1
        Host: www.mydomain.com
"""
print "========== VARNISH STEPPED PURGE SCRIPT ==============="
print "    This program makes purging Varnish easier   "

strTelnetHost = raw_input("Enter Telnet Host: ")
strTelnetPort = raw_input("Enter Telnet Port: ")
print "Telnet Host: %s   Port: %s " % (strTelnetHost, strTelnetPort)
strTargetHost = 'www.mydomain.com'

nWaitMinutes = 60

listPurgeDirs = [
	'/articles/*',
	'/news/*',
	'/blog/*',
	'/forum/*'
]

for strPathToPurge in listPurgeDirs:
	print ">>>>>>> Purging: " + strPathToPurge
	
	tn = telnetlib.Telnet(strTelnetHost, strTelnetPort)
	strPurgeCommand = "PURGE %s HTTP/1.1 \n" % (strPathToPurge)
	print strPurgeCommand[:-1]
	tn.write(strPurgeCommand)
	strHostCommand = "Host: %s \n" % (strTargetHost)
	print strHostCommand[:-1]
	tn.write(strHostCommand)
	print "\n\nexit"
	tn.write("\n\nexit\n")

	print "%%%%%%% Response %%%%%%%%%%"
	print tn.read_all()
	print "%%%%%%%%%%%%%%%%%%%%%%%%%%%"
	tn.close()
	
	print "Sleeping for %d minutes .... " % (nWaitMinutes)
	time.sleep(nWaitMinutes * 60 )
