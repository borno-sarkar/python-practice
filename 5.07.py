nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input(" enter number: "))
idx=0
for el in nums:
	if el == x:
		print("found at index", idx)
		break
	idx += 1