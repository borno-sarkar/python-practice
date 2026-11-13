with open("number.txt", "w") as f:
	f.write("12, 7, 4, 9, 10, 33, 6")
	
with open("number.txt", "r") as f:
	data = f.read()
	numbers = data.split(",")
	count = 0
	for num in numbers:
		if int(num) % 2 == 0:
			count += 1
			
print("Total even numbers: ", count)