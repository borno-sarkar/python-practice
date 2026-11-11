def print_elem(lst, idx):
	if idx == len(lst):
		return
	print(lst[idx])
	print_elem(lst, idx +1)

heroes = ["Batman", "Superman", "Spiderman"]
print_elem(heroes, 0)