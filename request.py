"""
	The class manages information related to a request
	A request is created when data is validated
	A request is passed to the weather module to obtain
	weather details
"""

class request():
	location = None
	time = None
	today = True
	day = None
	date = None

	def __init__(self, loc, ti):
		""" Initialise basic information"""
		self.location = loc
		self.time = ti

	def get_location(self):
		""" returns location requested """
		return self.location

	def get_time(self):
		""" returns time requested """
		return self.time

	def set_future_date(self):
		""" 
			Used for setting future date
			sets today to False to indicate
			date is in the future
		"""
		self.today = False

	def is_today(self):
		""" 
			checks if request is for current day
			True if for current day
			False for future day
		"""
		return self.today

	def set_day_of_week(self, day):
		self.day = day

	def get_day_of_week(self):
		""" 
			returns day of week requested 
			option function for future dates
		"""
		return self.day

	def set_date(self, date):
		""" 
			sets date requested 
			option function for future dates
		"""
		self.date = date

	def get_date(self):
		""" 
			returns date requested 
			option function for future dates
		"""
		return self.date

