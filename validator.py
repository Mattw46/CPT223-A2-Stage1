""" Validator takes in arguments passed and validates.
	Data is read in from a file to validate stations against
	if the data validates a request object and created 
	and passed back """

import request
import locations
import day

""" validates data and creates request object """
def validate(input):
	destination = input[1].title()
	if (locations.valid_location(destination)): #valid location
		print "valid location"
		if (input[2].isdigit()): # arg is int
			""" 
				Handle format:
				 Hallam 2 days from tomorrow 5:20pm
			"""
			print "is a number"
			# determine day
			#validate time
			print input
			print len(input)
			print input[len(input) -1]
			time = input[len(input) - 1]
			#print "time: " + time
			if (day.valid_time(time)):
				print "valid time"
			else:
				return None
			#create request
			req = request.request("Geelong", "5:00pm")
			return req
		elif (day.valid_day(input[2].title())):
			"""
				Handle Format:
				 "melbourne central" wednesday 5:20pm
			"""
			print "Valid day"
			day_of_week = input[2].title()
			#validate time
			print input
			print len(input)
			print input[len(input) -1]
			time = input[len(input) - 1]
			#print "time: " + time
			if (day.valid_time(time)):
				print "valid time"
			else:
				return None
			#create and return req obj
			req = request.request("Geelong", "5:00pm")
			return req
		elif (day.valid_specifier(input[2].title())):
			"""
				Handle Format:
				 "melbourne central" tomorrow 5:20pm
			"""
			print "Valid specifier"
			day_of_week = input[2].title()
			#validate time
			print input
			print len(input)
			print input[len(input) -1]
			time = input[len(input) - 1]
			#print "time: " + time
			if (day.valid_time(time)):
				print "valid time"
			else:
				return None
			#create and return req obj
			req = request.request("Geelong", "5:00pm")
			return req
		elif (day.valid_time(input[2])):
			"""
				Handle Format:
				 "melbourne central" 5:20pm
			"""
			print "basic request"
			time = input[2]
			req = request.request("Geelong", "5:00pm")
			return req
		else:
			"""
				Catches all remaining request that 
				did not meet above criteria.
				request caught here a invalid hence 
				return None
			"""
			print "invalid input"
			return None
	else:
		print "invalid location"
		return None