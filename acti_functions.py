from constantes import *
import datetime

def getMonth(month):
	intMonth = 0

	if month == 'Jan':
		intMonth = 1
	elif month == 'Feb':
		intMonth = 2
	elif month == 'Mar':
		intMonth = 3
	elif month == 'Apr':
		intMonth = 4
	elif month == 'May':
		intMonth = 5
	elif month == 'Jun':
		intMonth = 6
	elif month == 'Jul':
		intMonth = 7
	elif month == 'Aug':
		intMonth = 8
	elif month == 'Sep':
		intMonth = 9
	elif month == 'Oct':
		intMonth = 10
	elif month == 'Nov':
		intMonth = 11
	elif month == 'Dec':
		intMonth = 12
	
	return intMonth

def readActiFile(filename):
	print "READING ACTI FILE"
	try:
		actiFile = open(filename,'r')
	except Exception:
		actiFile = open(defDirectory+filename,'r')

	cntLines = 0
	resolution = 0
	startTime = ''
	for line in actiFile:
		cntLines += 1

		#If date line
		if cntLines == 2:
			startTime = line

		#If time line
		if cntLines == 3:
			intMonth = getMonth(startTime[3:6])
			startTime = datetime.datetime.combine(datetime.date(int(startTime[-6:-1]), intMonth, int(startTime[1:2])), datetime.time(int(line[0:2]), int(line[3:5])))

		#If resolution line
		if cntLines == 4:
			if int(line) == 2:
				resolution = 30
			if int(line) == 4:
				resolution = 60
			if int(line) == 8:
				resolution = 120
			if int(line) == 20:
				resolution = 300
	print startTime
	print resolution
	print "READING ACTI FILE - END"
