import sys

class Grid:
	def __init__(self, input_file):
		self.raw_grid = input_file.read()
		self.markers = []
		self.grid_array = self.raw_grid.split("\n")

	def draw_path(self, output_file):
		self.remove_empty_elements()
		self.find_markers()
		self.build_output_array()
		self.trace_markers()
		self.print_output(output_file)

	def remove_empty_elements(self):
		for row in self.raw_grid:
			if row == "":
				self.grid_array.remove(row)
		self.grid_col_length = len(self.grid_array[0])

	def find_markers(self):
		for row_index, row in enumerate(self.grid_array):
			for col_index, character in enumerate(row):
				if character == '#':
					self.markers.append( [row_index, col_index] )

	def build_output_array(self):
		for index, row in enumerate(self.grid_array):
			self.grid_array[index] = ["."] * self.grid_col_length

	def fill_path(self, marker1, marker2):
		for row_index, row in enumerate(self.grid_array):
			for col_index, character in enumerate(row):
				# going down
				if col_index == marker1[1] and row_index >= marker1[0] and row_index <= marker2[0]:
					self.grid_array[row_index][col_index] = "#"
				if marker1[1] < marker2[1]:
					if col_index >= marker1[1] and col_index <= marker2[1]:
						self.grid_array[marker2[0]][col_index] = "#"
				else:
					if col_index >= marker2[1] and col_index <= marker1[1]:
						self.grid_array[marker2[0]][col_index] = "#"

	def trace_markers(self):
		if len(self.markers) > 2:
			for mark_index, mark in enumerate(self.markers):
				if mark_index < (len(self.markers) - 1):
					self.fill_path(mark, self.markers[mark_index + 1])
		else:
			print 'There must be at least 2 markers!'

	def print_output(self, output_file):
		self.output = open("output.txt", "w")
		for row in self.grid_array:
			self.output.write ("".join(row) + "\n")
		self.output.close()

def main():
	input_file = sys.argv[1]
	output_file = sys.argv[2]
	grid1 = Grid(open(input_file))
	grid1.draw_path(output_file)

main()

