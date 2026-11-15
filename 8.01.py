class Student:
	def __init__(self, name, marks):
		self.name = name
		self.marks = marks
		
	def get_average(self):
		avg = sum(self.marks)/3
		print("Average: ", avg)
		
s1 = Student("Borno", [85, 90, 78])
s1.get_average()