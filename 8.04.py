class Employee:
	def __init__(self, role, department,salary):
		
	    self.role = role
	    self.department = department
	    self. salary = salary
	    
	def showDetails(self):
		print("role: ", self.role)
		print("department: ", self.department)
		print("salary: ", self.salary)
		
class Engineer(Employee):
	def __init__(self, name, age):
		self.name = name
		self.age = age
		super().__init__("Engineer", "Development", "75,000")
		
engg1 = Engineer("Elon musk", 40)
print("Name: ", engg1.name)
print("Age: ", engg1.age)
engg1.showDetails()
		
