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

# ==========================================
# Course: Apna College Python Tutorial
# Instructor: Shraddha Khapra
# Topic: Lecture 4 - Dictionary and set
# Solved by: Borno Sarkar
# ==========================================

# Practice Problem 1: Store following word meanings in a python dictionary :table: " a piece of furniture", " list of facts and figures" cat : " a small animal "

dictionary = {
    "table": ["a piece of furniture", "list of facts & figures"],
    "cat": "a small animal"
}
print(dictionary)

# Practice Problem 2: You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classroom are needed by the all students.  "python", "java", "C++", "python", "JavaScript","java", " python ", "java", "C++", "C"

subjects = {"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"}
print(len(subjects))

# Practice Problem 3: WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.

marks = {}
x = int(input("Enter phy: "))
marks.update({"phy": x})

x = int(input("Enter chem: "))
marks.update({"chem": x})

x = int(input("Enter math: "))
marks.update({"math": x})

print(marks)

# Practice Problem 4: Figure out a way to store 9 and 9.0 as separate values in the set. (You can take help of built-in data types)

values = {"9.0", "9"}
print(values)

# ==========================================
# Course: Apna College Python Tutorial
# Instructor: Shraddha Khapra
# Topic: Lecture 5 - loops
# Solved by: Borno Sarkar
# ==========================================
# 1. Print numbers from 1 to 100
i = 1
while i <= 100:
    print(i)
    i += 1


# 2. Print numbers from 100 to 1
i = 100
while i >= 1:
    print(i)
    i -= 1


# 3. Print the multiplication table of a number n
n = int(input("Enter number: "))
i = 1
while i <= 10:
    print(n * i)
    i += 1


# 4. Print the elements of the following list using a loop
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
i = 0
while i < len(nums):
    print(nums[i])
    i += 1


# 5. Search for a number x in this tuple/list using a loop
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x = 36  # যে সংখ্যাটি খুঁজতে চাও

i = 0
while i < len(nums):
    if nums[i] == x:
        print("Found at index:", i)
        break
    i += 1
    
# 6. Print the elements of the following list using a for loop
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for el in nums:
    print(el)


# 7. Search for a number x in this tuple/list using a for loop
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x = int(input("Enter number: "))

idx = 0
for el in nums:
    if el == x:
        print("found at index", idx)
        break
    idx += 1
    
# using for and range()
# 8. Print numbers from 1 to 100
for i in range(1, 101):
    print(i)


# 9. Print numbers from 100 to 1
for i in range(100, 0, -1):
    print(i)


# 10. Print the multiplication table of a number n
n = int(input("Enter number: "))

for i in range(1, 11):
    print(n * i)
    
# 11. WAP to find the sum of first n numbers (using while)
n = int(input("Enter number: "))

sum = 0
i = 1
while i <= n:
    sum += i
    i += 1

print("Total sum:", sum)


# 12. WAP to find the factorial of first n numbers (using for)
n = int(input("enter number: "))

fact = 1
for i in range(1, n + 1):
    fact *= i

print("Factorial:", fact)

# ==========================================
# Course: Apna College Python Tutorial
# Instructor: Shraddha Khapra
# Topic: Lecture 6 - Functions and Recursion 
# Solved by: Borno Sarkar
# ==========================================

# 1. WAF to print the length of a list. (list is the parameter)
def print_len(lst):
    print("Length of list:", len(lst))


cities = ["Dhaka", "Khulna", "Rajshahi", "Sylhet", "Chattogram"]
print_len(cities)

print("-" * 30)

# 2. WAF to print the elements of a list in a single line. (list is the parameter)
def print_list(lst):
    for item in lst:
        print(item, end=" ")
    print()  # For new line


heroes = ["Batman", "Superman", "Spiderman", "Ironman"]
print_list(heroes)

print("-" * 30)

# 3. WAF to find the factorial of n. (n is the parameter)
def calc_fact(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(f"Factorial of {n} is:", fact)


calc_fact(5)
calc_fact(10)

print("-" * 30)

# 4. WAF to convert USD to INR.
def converter(usd_val):
    inr_val = usd_val * 83  # 1 USD ≈ 83 INR
    print(f"{usd_val} USD = {inr_val} INR")


converter(5)
converter(20)
