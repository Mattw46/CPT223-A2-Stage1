""" Template for weather module 
	to be used to get the weather forcast
	and return a result.
"""

# initiates a request for weather forcast
def get_weather(req):
	print "get weather called"
	if (req == None):
		print "req is invalid"

	print req.get_time()