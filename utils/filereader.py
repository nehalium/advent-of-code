class FileReader:

	file_to_read = ""
	lines = []

	def __init__(self, file_to_read):
		self.file_to_read = file_to_read

	def get_lines(self):
		with open(self.file_to_read) as file:
			self.lines = file.readlines()
		return self.lines
