with open("practice.txt", "r") as f:
	content = f.read()
	new_content = content.replace("java", "Python")
	with open("practuice.txt", "w") as f:
		f.write(new_content)

print(new_content)
