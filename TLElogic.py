import sys
import math
import ephem
import serial
import Queue
import Command
import time

azelQ = Queue.Queue(0)

def readingTLE(file):
    TLEfile = open(file,'r')
    while True:
    	line1 = TLEfile.readline()
    	if not line1: break
    	line2 = TLEfile.readline()
    	line3 = TLEfile.readline()

    	iss = ephem.readtle(line1, line2, line3)
    	obs = ephem.Observer()
    	obs.lat = '42.02690'
    	obs.long = '-93.65278'

    	for p in range(3):
			tr, azr, tt, altt, ts, azs = obs.next_pass(iss)
			print """Date/Time (UTC)       Alt/Azim	  Lat/Long	Elev"""
			print """====================================================="""
			while tr < ts:
				obs.date = tr
				iss.compute(obs)
				tr = ephem.Date(tr + 1.0 * ephem.second)
				c = Command.Command(math.degrees(iss.az),math.degrees(iss.alt))
				azelQ.put_nowait(c)
			print
			obs.date = tr + ephem.minute
	print "--------------"
    moveRotor()




def moveRotor():
    #controllerSerial = serial.Serial(COM3,9600,serial.EIGHTBITS,serial.PARITY_NONE,serial.STOPBITS_ONE)
    while azelQ.empty()==False:
        #controllerSerial.write(a)
        print azelQ.get_nowait().__repr__()
        time.sleep(1)




