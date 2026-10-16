# python-practice
My Python practice solutions


# ==========================================
# Course: Apna College Python Tutorial
# Instructor: Shraddha Khapra
# Topic: Lecture 1 - Variables and Data Types
# Solved by: Borno Sarkar
# ==========================================

# Practice Problem 1: Sum of two numbers
num1 = int(input("First number: "))
num2 = int(input("Second number: "))
print("Their sum is:", num1 + num2)

# Practice Problem 2: Area of a square
side = float(input("Length of a square: "))
print("The area is:", side * side)

# Practice Problem 3: Average of two floating point numbers
a = float(input("First number: "))
b = float(input("Second number: "))
print("The average is:", (a + b) / 2)

# Practice Problem 4: Print True if 'a' is greater than or equal to 'b'
a = int(input("First number: "))
b = int(input("Second number: "))
print(a >= b)
# ==========================================
# Course: Apna College Python Tutorial
# Instructor: Shraddha Khapra
# Topic: Lecture 2 - strings and conditional statements
# Solved by: Borno Sarkar
# ==========================================

# Practice Problem 1: WAP to input user's first name and print its length 
str1 = input ("Your first name: ")
len(str1)
print(len(str1))

# Practice problem 2:  WAP to find the occurrence of '$' in a String.

str = "She spent 100$ on buying a new notebook."
print("Occurrence of '$':", str.count("$"))

# Practice Problem 3: WAP to check if a number entered by the user is odd or even.

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Practice Problem 4: WAP to find the greatest of 3 numbers entered by the user.

a = int(input("First number: "))
b = int(input("Second number: "))
c = int(input("Third number: "))

if a >= b and a >= c:
    print("First number is the greatest:", a)
elif b >= a and b >= c:
    print("Second number is the greatest:", b)
else:
    print("Third number is the greatest:", c)

# Practice Problem 5: WAP to check if a number is a multiple of 7 or not.

num = int(input("Enter number: "))
remainder = num % 7

if remainder == 0:
    print("Multiple of 7")
else:
    print("Not a multiple")
    
# ==========================================
# Course: Apna College Python Tutorial
# Instructor: Shraddha Khapra
# Topic: Lecture 3 - Lists and Tuples
# Solved by: Borno Sarkar
# ==========================================

# Practice Problem 1: WAP to ask the user to enter names of their 3 favorite movies & store them in a list.

fav_movies = []
mov1 = input("1st movie: ")
mov2 = input("2nd movie: ")
mov3 = input("3rd movie: ")
fav_movies.append(mov1)
fav_movies.append(mov2)
fav_movies.append(mov3)
print(fav_movies)

# Practice Problem 2: WAP to check if a list contains a palindrome of elements.( Hint : use copy() method)

list1 = [1,2,3,2,1]
copy_list = list1.copy()
copy_list.reverse()
if(copy_list == list1):
    print("Palindrome")
else:
    print("Not palindrome")

# Practice Problem 3: WAP to count the number of students with the "A" grade in the following tuple.
["C","D","A","A","B","B","A"]

tup = ("C","D","A","A","B","B","A")
print(tup.count("A"))

# Practice Problem 4: WAP to store the above values in a list & short them from "A" to "D".

list1 = ["C","D","A","A","B","B","A"]
list1.sort()
print(list1)

