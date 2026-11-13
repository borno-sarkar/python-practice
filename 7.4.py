def check_for_line():
	word = "learning"
	line_no = 1
	with open("practice.txt", "r") as f:
		while True:
			line = f.readline()
			if word in line:
				print("Line number: ", line_no)
				return
			line_no += 1
	return -1
				
check_for_line()