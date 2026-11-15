class Account:
	def __init__(self, balance, acc_no):
		self.balance = balance
		self.acc_no = acc_no
	def credit(self, amount):
			self.balance += amount
	def debit(self, amount):
			self.balance -= amount
	def show_balance(self):
			print("Account", self.acc_no, "balance: ", self.balance)
			
a1 = Account(1000, 12345)
a1.credit(500)
a1.debit(200)
a1.show_balance()