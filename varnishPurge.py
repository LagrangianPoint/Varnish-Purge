#!/usr/bin/python

import telnetlib
"""
SAMPLE OUTPUT:
        telnet varnish1.mydomain.com 8909
        PURGE /articles/* HTTP/1.1
        Host: www.mydomain.com
"""
print "========== VARNISH PURGE SCRIPT ==============="
print "    This program makes purging Varnish easier   "
strTelnetHost = raw_input("Enter Telnet Host: ")
strTelnetPort = raw_input("Enter Telnet Port: ")
print "Telnet Host: %s   Port: %s " % (strTelnetHost, strTelnetPort)
strTargetHost = raw_input("Target domain to flush cache (i.e. www.mydomain.com): ")
print "Enter which path you want to purge (i.e.  /articles/* )"
strPathToPurge = raw_input("Path to purge: ")

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
