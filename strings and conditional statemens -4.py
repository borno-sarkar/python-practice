a = int(input("First number: "))
b = int(input("Second number: "))
c = int(input("Third number: "))
if(a>=b and a>=c):
	print("First number is the greatest", a)
elif(b>=c):
	print("Second number is the greatest", b)
else:
	print("Third number is the greatest", c)