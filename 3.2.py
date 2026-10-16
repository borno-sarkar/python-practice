list1 = [1,2,3,2,1]
copy_list = list1.copy()
copy_list.reverse()
if(copy_list == list1):
	print("Palindrome")
else:
	print("Not palindrome")