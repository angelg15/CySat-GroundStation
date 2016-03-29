"""stuff will go here"""
import ephem

def readingTLE(file):
    TLEfile = open(file,'r')
    line1 = TLEfile.readline()
    line2 = TLEfile.readline()
    line3 = TLEfile.readline()
    print line1
    print line2
    print line3


readingTLE('randomfile.txt')
