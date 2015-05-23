""" Validator takes in arguments passed and validates.
	Data is read in from a file to validate stations against
	if the data validates a request object and created 
	and passed back """

import request
import locations
import day
import datetime

""" validates data and creates request object """
def validate(input):
	if (len(input) == 3):
		# covers location, time scenario
		#print "length 2"
		destination = input[1].title()
		time = input[2]
		if (locations.valid_location(destination) and
			day.valid_time(time)): #valid location
			#print "valid location"
			req = request.request(destination, time)
			return req
	elif(len(input) == 4):
		# covers location, day, time scenario
		print "length 3"
		destination = input[1].title()
		time = input[3]
		day_specified = input[2].title()
		if (locations.valid_location(destination)): #valid location
			print "valid location"
			if (day.valid_time(time)):
				print "valid time"
				if (day.valid_day(day_specified)):
					print "valid day"
					req = request.request(destination, time)
					
					day_of_week = day.get_specified(day_of_week)
					today = day.get_day(datetime.datetime.today().weekday()) 
					if (today != day_of_week):
						req.set_future()
						# set n days from
					return req
				elif(day.valid_specifier(day_specified)):
					print "valid day specifier"
					req = request.request(destination, time)
					return req
		# check valid day
		# check valid time
	elif(len(input) > 4):
		# covers location, n days from, time
		print "length > 3"
		destination = input[1].title()
		if (locations.valid_location(destination)): #valid location
			print "valid location"
		# check valid n days from
		# check valid time
			