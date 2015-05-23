"""
	The class manages information related to a request
	A request is created when data is validated
	A request is passed to the weather module to obtain
	weather details
"""

class request():
	location = None
	time = None
	today = True # assumes current day
	days_from_current = 0

	def __init__(self, loc, ti):
		""" Initialise basic information"""
		self.location = loc
		self.time = ti

	def is_future(self):
		""" sets today to False
			date will be considered future date
		"""
		today = False

	def set_future(self):
		today = False


	def set_days_from_now(self, days):
		""" set number days from current day """
		days_from_current = days

	def get_days_from_now(self):
		return days_from_current

	def is_today(self):
		return today

########################################################################