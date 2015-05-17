#!/usr/bin/env python

""" Main file for Assignment 2 
	Stage 1"""

import sys
import validator

""" Main Section """

# call validator, get a request object back with valid data else None
request = validator.validate(sys.argv)

if (request == None):
	print "invalid request"
	exit

# testing
print request.get_location()
print request.get_time()

# testing scenario 2
#print request.get_day_of_week()
#print request.is_today()

# call get weather, get a weather object back, None if error getting data