# #Data Types
# #1.Strings
# s ='Hello'
# print(len(s))
# w = 'World'
# print("The two words are", s , " and ", w)
# print("The two words are " + s + " and "+ w)
# #Subspripting
# print("Hello"[0])

# #type check
# print(type(w))

# #Adding the two digit numbers 
# two_digit_number = input()
# print(type(two_digit_number))
# first_number = int(two_digit_number[0])
# second_number = int(two_digit_number[1])

# print(first_number + second_number)

# #Operators
# # + - * / **
# #Piority Rule: PEMDASLR-
#     # Parentheses
#     # Exponents
#     # Multiplication
#     # Division
#     # Addition
#     # Subtration
#     # Left to Right

#     # in short:
#     #     ()
#     #     **
#     #     *
#     #     +-
#     #     L to R
#Rounding off- round function. Example:
#print(round(8/3 , 3))
########################################################
#f string
# s = int(3)
# w = 'Hello'
# print(f"so this is the use of the f string {s} is int and {w} is string, yet both can be used in the same line!")
#Floor Division: (8 // 3)- this will directly give the int value.

###################################################
#Day 2 Project- Tip calculator
print('Hello! Welcome to the tip calculator')
#Taking inputs from the user.
total_bill = float(input("What was the total bill?"))
tip_percentage = float(input("What percentage tip you want to give like 10, 12, etc...?"))
people = int(input("How many people to split the bills?"))

total_payment = round((total_bill + (total_bill*(tip_percentage/100)))/(7),2)
print(f"Each person should pay: {total_payment}")