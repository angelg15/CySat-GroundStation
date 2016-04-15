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

        storedAZEL = []

    	for p in range(3):
			tr, azr, tt, altt, ts, azs = obs.next_pass(iss)
			print tr
			print ts
			print str(math.degrees(altt)) + " |  " + str(tt)
			print """Date/Time (UTC)       Alt/Azim	  Lat/Long	Elev"""
			print """====================================================="""
			while tr < ts:
				obs.date = tr
				iss.compute(obs)
				AZEL = math.degrees(iss.az) + "" + math.degrees(iss.alt)
				storedAZEL.append(AZEL)
				print "%s | %4.1f %5.1f | %4.1f %+6.1f | %5.1f" % \
					(tr,
					 math.degrees(iss.alt),
					 math.degrees(iss.az),
					 math.degrees(iss.sublat),
					 math.degrees(iss.sublong),
					 iss.elevation/1000.)
				tr = ephem.Date(tr + 1.0 * ephem.second)
			print
			obs.date = tr + ephem.minute