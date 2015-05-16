""" Validator takes in arguments passed and validates.
	Data is read in from a file to validate stations against
	if the data validates a request object and created 
	and passed back """

import request

""" validates data and creates request object """
def validate(input):
	if (len(input) == 3):
		# location time
		print "location time"
		locations = readfile()
		#print locations
		for item in locations:
			#print item
			if (input[1] in item and valid_time(input[2])):
				req = request.request(input[1], input[2])
				return req
			else:
				return None
	elif (len(input) == 4):
		# location day time
		print "location day time"
	elif (len(input) == 7):
		# location n day(s) from day_specified time
		print "location n day(s) from day_specified time"
	else:
		print "invalid input"
		return None

""" Reads in stops file and returns list of strings 
	column headings is removed from top of the file """
def readfile():
	print "reading"
	fp = open("stops.txt", "r")
	temp = fp.read()
	stops = temp.split("\n")
	stops.remove(stops[0])
	fp.close()
	return stops

""" calculates future date """
def calculate_date():
	print "calculating"


def valid_time(time):
	mid = time.index(":")
	hour = int(time[:mid])
	if (len(time[mid + 1:]) == 4):
		min = int(time[mid + 1:-2])
		am_pm = time[-2:]
	else:
		min = int(time[mid + 1:])
		am_pm = None

	if (am_pm == None):
		if (hour < 1 or hour > 24):
			#print "failed 24 time"
			return False
		else:
			return True
	elif ((hour < 1) or (hour > 12)):
		#if (hour < 1):
		#	print "%i < 1",hour
		#if (hour > 12):
		#	print "%i > 12",hour
		#print "failed am pm - %i < 1 or %i > 12",hour,hour
		return False
	else:
		return True