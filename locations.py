""" Reads in locations from file
	returns a list of locations"""

def valid_location(destination):
	stops = readfile()
	for locations in stops:
		if (destination in locations):
			return True

	return False # default if location not found


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