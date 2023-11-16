class BoardException(Exception):
	def __init__(self,message):
		#custom exception to be raised when there is an error with the board eg dimensions are too small
		super().__init__(message)