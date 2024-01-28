'''
Day 5- Python Loops
'''
# #For Loop concept
# fruits = ["apple", "peach", "pear"]
# # for fruit in fruits:
# #     print (fruit)
# #     print(fruit + " pie")
# nested = [fruits, ["ayush", "xyz", "abc"]]
# for decode in nested:
#     print(decode)

# #---------------------------------------------------------------------------------------------------------
# #Average height calculator using for loop
    
# Input a Python list of student heights
# student_heights = input().split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
# student_numbers = 0
# count = 0
# for num in student_heights:
#   student_numbers += num
#   count += 1
# average = round((student_numbers/count))
# print(f"total height = {student_numbers}")
# print(f"number of students = {count}")
# print(f"average height = {average}")
#--------------------------------------------------------------------------------------------------------

# #Highest score calculator using for loop:
# students_marks = input("Please enter the student scores").split()
# for n in range(0, len(students_marks)):
#   students_marks[n] = int(students_marks[n])

# max = 0
# for score in students_marks:
#   if max < score:
#     max = score
# print(f"The highest score is: {max}")
#---------------------------------------------------------------------------------------------------------

#RANGE Function
#for number in range(a,b):
#    print(number)
# for number in range(0,10,2):
#     print(number)
#----------------------------------------------------------------------------------
#addition of numbers 1 to 100
# addition = 0
# for number in range (1,101):
#     addition += number
# print(f"The sum of the numbers from 1 to 100 is: {addition}")
#--------------------------------------------------------------------------------------
#addition of all even or odd (menu driven) numbers from 0 to x  definied by user
# add = 0
# limit = (int(input("q to how many?\n")))
# choice = int(input(f"Even or Odd addtion from 0 to {limit}? 1 for Odd and 2 for Even: \n"))
# if choice == 1 or choice == 2:
#     if choice == 2:
#         for value in range (0, limit+1, 2):
#             add += value
#     elif choice == 1:
#         for value in range (1, limit+1,2):
#             add += value
#     print(f"Additon is: {add}")
# else:
#     print("Wrong option choosed!")
#--------------------------------------------------------------------------------------------------

#Question- You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:

# Your program should print each number from 1 to 100 in turn and include number 100.

# When the number is divisible by 3 then instead of printing the number it should print "Fizz".

# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`

# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

# e.g. it might start off like this:

# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
# ...etc
#--------------------------- Answer --------------------------------------------------------

# for num in range(1, 101):
#   if num%3 == 0 and num%5 == 0:
#     print("FizzBuzz")
#   elif num%3 ==0:
#     print("Fizz")
#   elif num%5 == 0:
#     print("Buzz")
#   else:
#     print(num)
#------------------------------------------------------------------------------------------------------
#------------------------ Project of Day 4 ------------------------------------------------------------
#Random Password Generator:
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
#epass = easy_passward
# epass= ""
# for l in range(1,nr_letters+1):
#     rl = random.choice(letters)
#     epass += rl
# for s in range(1,nr_symbols+1):
#     epass += random.choice(symbols)
# for n in range(1, nr_numbers+1):
#     epass += random.choice(numbers)
# print(epass)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
epass = []
password =""
for l in range(1,nr_letters+1):
    rl = random.choice(letters)
    epass += rl
for s in range(1,nr_symbols+1):
    epass += random.choice(symbols)
for n in range(1, nr_numbers+1):
    epass += random.choice(numbers)

random.shuffle(epass)
for value in epass:
    password += value
print(f"The random password is: {password}")
    