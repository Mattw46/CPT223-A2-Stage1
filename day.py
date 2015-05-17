""" Helper functions to valid_day """
def return_true():
	print "day is true"
	return True

def return_false():
	print "day is false"
	return False


""" checks day is a valid day """
def valid_day(day):
	options = {
		"Monday" : return_true,
		"Tuesday" : return_true,
		"Wednesday" : return_true,
		"Thursday" : return_true,
		"Friday" : return_true,
		"Saturay" : return_true,
		"Sunday" : return_true,
		"Mon" : return_true,
		"Tue" : return_true,
		"Wed" : return_true,
		"Thu" : return_true,
		"Fri" : return_true,
		"Sat" : return_true,
		"Sun" : return_true
	}

	return validate(day,options)


""" checks day is a day specifier """
def valid_specifier(specifier):
	options = {
		"Tomorrow" : return_true,
		"Next Week" : return_true,
		"Today" : return_true,
		"Now" : return_true
	}
	print specifier + ": "
	return validate(specifier,options)
	
""" A generic validator that validates value day
	against a list of options [options]"""
def validate(day, options):
	try:
		opt = options[day]
		result = opt()
	except KeyError, e:
		#print "Day is invalid - return False"
		result = return_false()

	return result

""" checks that the supplied time is valid """
def valid_time(time):
	mid = time.index(":")
	print "mid: "
	print mid
	hour = int(time[:mid])
	print "hour: "
	print hour
	minute = time[mid + 1:]
	if (len(minute) == 4):
		minute = int(minute[:2])
		am_pm = time[-2:]
	else:
		return None
	print "minute: "
	print minute
	print am_pm
	#am_pm = time[-2:]
	#print hour + ":" + min + am_pm

	if (hour < 1 or hour > 12):
		return None
	if (minute < 0 or minute >= 60):
		return None
	if (am_pm != "am" and am_pm != "pm"):
		return None

	return True