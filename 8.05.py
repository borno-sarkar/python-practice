class Order:
	def __init__(self, item, prize):
		self.item = item
		self.prize = prize
		
	def __gt__(self, other):
		return self.prize > other.prize
		
Order1 = Order ("Chips", 50)
Order2 = Order ("Tea ", 20)

print(Order1 > Order2)