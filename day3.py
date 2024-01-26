'''
DAY 3 of learning python
'''

#Day 3- Conditional statments, logical operators, code blocks and scope
#There is no do while loop in python, there is only if else loop, example que: if height is greater than 150 ccm allow or deny
# print('WELCOME! To the Roller Coster Ride')
# height = int(input("Please enter your height (in cm as whole number)"))

# if height >= 150:
#     print("Welcome you are allowed to enjoy ther ride of roller coster! Welcome again!!!")
#     age = int(input("Please enter your age____"))
#     if age < 18:
#         print("Your tickect price is $10")
#     elif age >=18 and age < 25:
#         print("Your ticket price is $12")
#     else:
#         print("Your ticket price is $15")
# else: 
#     print("Grow older and come!")

# '''
# Conditional Operators
# <
# >
# >=
# <=
# ==
# !=
# '''
#-----------------------------------------------------------------------------------
#Odd even check
#number = int(input("Please enter the integer number"))
# if number%2 == 0:
#     print(f"The {number} is even number")
# else:  
#     print(f"The {number} is odd number.")
#---------------------------------------------------------------------------------
#BMI Calculator

# print('WELCOME TO BMI CALCULATOR')
# weight = (float(input("Please state your weight (in kg)")))
# height = (float(input('Please enter your height (in meters)')))
# bmi = round(((weight)/height**2),2)
# print(f"Your BMI is {bmi}")
# print(type(bmi))
# if bmi <= 18.5:
#   print(f"Your BMI is {bmi}, you are underweight.")
# elif bmi < 25:
#   print(f"Your BMI is {bmi}, you have a normal weight.")
# elif bmi >=25 and bmi <30:
#   print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif bmi >=30 and bmi <35:
#   print(f"Your BMI is {bmi}, you are obese.")
# else:
#   print(f"Your BMI is {BMI}, you are clinically obese.")
#----------------------------------------------------------------------------------------
#Checking the year is leap year or not?
# Which year do you want to check?
# year = int(input())
# if year%4 == 0:
#   if year%100 != 0:
#     print("Leap year")
#   else:
#     if year%400 == 0:
#       print("Leap year")
#     else:
#       print("Not leap year")
# else:
#   print("Not leap year")
#--------------------------------------------------------------------------------------------------------------
#code for this flowchart advanced version of the Ticket flowchart link - (https://app.diagrams.net/?lightbox=1&target=blank&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Rollercoaster%204#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1aoRTeFOb2SJO7ofMnhTCneCEboHowF2A%26export%3Ddownload)
# print("Welcome to Roller Coster Ride")
# height = int(input("Please enter your height (in cm as whole numbers)"))
# bill = 0
# if height >= 120:
#     print("You are eligible for the roller coster ride")
#     age = int(input("Please enter your AGE"))
#     if age < 12:
#         bill = 5
#         print("Your child ticket cost is ${bill}")
#     elif age >=12 and age <=18:
#         bill = 7
#         print(f"Your Teenage ticket price is ${bill}")
#     else:
#         bill = 12
#         print(f"Your adult ticket is ${bill}")
#     choice = input("You want photos, while you are on the ride? they will charge you $3 extra. Type Y for Yes and N  for No.")
#     if choice == "Y":
#         bill += 3
#         print(f"Your finial bill is ${bill}, Thank you! Enjoy your ride.")
# else: 
#     print("Sorry, you are not elegible to ride the roller coster.Thanks for co-opersting.")

#Updated flow chart for logical operators link - https://viewer.diagrams.net/index.html?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Day%203%20Logical%20Operators.drawio#R7VtZc9o6FP41zH2iY0teH0uWZpqkQy%2BZ29CXOwYrthNjUVkQyK%2BvjGWwLbEFL6HTzCSxjyVhfec7myQ68GKy%2BEKcqX%2BPXRR2gOIuOvCyA4CqAYP9SyTLVGJqXOCRwOWNNoJB8Ia4UOHSWeCiuNCQYhzSYFoUjnEUoTEtyBxC8Gux2RMOi586dTwkCAZjJxSlPwKX%2BqnUAuZGfoMCz88%2BWTXs9MnEyRrzmcS%2B4%2BLXnAhedeAFwZimV5PFBQoT8DJc0n7XW56uX4ygiB7SoR9ZTw%2FfyQD19fm%2Fc3dxF%2FzCXT6NmC6zCSOXzZ%2FfYkJ97OHICa820h7Bs8hFyagKu9u0ucN4yoQqEz4jSpdcmc6MYiby6STkT9kLk%2BVj0v%2BTAUEmGDJBV%2FmkmHomuVzwz0jvlvm7PiLBBFFEuFBEgwMU4xkZox0QZKxyiIfojnZ62i7BJ%2FcBHOsvCLO3IUvWgKDQocG8yB%2BH09Bbt%2BNdPxPiLHMNpjiIaJwbuZ8IWANuUZABthqR25Oq63mts4t0xOwu92ob0YoZR7DEbpklmqrlWaJ8TIJotRBEYICqFQlgK8UR0vfknTbMOJZohtE8zzgWcyeccXS4b01cm%2BFMGHF6Hl0pU1GZz5904LVATeLjyWjGZtl79QOKBlNnpd1XFp%2BKBNvKiDkiFC126jB7qppFlLKw9bqJFarBZX4uTpSVlld7DuPjIYRtmOr7bQscaFtq1bZ1EshA4OmAzYCKVFwDq%2B6n41MQhhc4xGTVF7o6stzE7cWU4BeUe2KBEWTWWQ2BYZHAQMJfIOGvVhd%2FNQHaCyf6J%2FEALD1EpyFcAV5QKcIlsXfLrAeuy682%2BL%2F%2FzaXPLvk%2BvOl71zdexsRzMXddNHfptD6WuesyTn4URgKzZMENUlLuqhUBrm9YgInNjhaxcMLAi9j1mGGRZG29BIOAVWKf%2BYNJ4LopgVEcvDmj1VAJhXkqw8bVex39MhmLcTZO6VsRzFYp0ENbQBlK%2FCSoDWUxVxqi%2BOxhBpa2F2etJpylnkiMR2143FwttK6OD6mEDvLUuzzwXk9tVO2p5dUIUJKZ55kBgV4cZEvd847aRA6I8lfx%2BXZWWyFa%2FtZ%2FzbLQzm4tgVKGP3%2B8PfT6PwfImj8%2BPAS9STtZKloE9DF3Pdzoid1tNJPcFFaO2laoFMLWMuJdb52LiskyepsrMcASAoQiSYQlqYNeW23Wsk9qhsD1JADHrlaqsKh8zSpthpTzCRvual9c3tzbWy8XUzXnIoYkKWUq1HTRBBuuRu3i%2Bgi0RBu0a1pOkiJlCkjdoThOHK6%2FKuElecO5lUxqGfMD%2FV5tJRNoJVN%2BvwerPJPdsnMHyhFKL6ugZrdhbXEb4iZw84tYejl6t%2B051vRpJ3qrzUTvyuuEd0VvXTkuekPNOiF6l3s3Hb3tLWYoiUVN26FmfLD4LVnmVEFXtc4%2BakNV8Hi6iLXeZNxWoYg1A1rBJPnDpnb%2BoB%2BQKpmNpkqyTH6rD1D2%2BwBhs9gYW2j0VNpejnCUqMB1Yn%2FtXCqAVzeL8AKJ91Bl%2BK6PSJwCsH3%2F%2BGI8erfgFvwKlvfPN8v%2BfVekdBtR%2FaD4vGvZJ7885M%2FnXfx0iYKv9n%2Bz5a06uDNesnnWncPqalHDh2awRx8%2BsuSZcmWnj3ZgLcRlsZxpOiwbWnthWQqVaFafPYYHUJIlCKXLfnVxLeLcooVuvm9BsYpoITXyViqSg3zXLp%2B013dVfrD2JJBbCRDZXkW2IXHkXgWofrPiJI2aH0qjorN6dSJ%2BpjRMPNKIZbbG6lzp1MfMi5x0qlTIwJTVjzwDq8BLlQ%2FqrkNyPulSbNFNWXW5Ka1VC1pbzTD3pIXdvl2u7swMSDz%2FliZG4lnjoxKjpi0FlnZtDNlhbaWmNEoKrFj9%2FQlnuMo4r9fXGjjDtcuacjA%2F%2BCgxQ0ydpPMoSMeIVzFBW5wXrVmeWoDblKSpKrCz1aZGiC3uNPwBR0ABLEVaCa8rOgPKbjdfDEzr283XK%2BHVbw%3D%3D

# print("Welcome to Roller Coster Ride")
# height = int(input("Please enter your height (in cm as whole numbers)"))
# bill = 0
# if height >= 120:
#         print("You are eligible for the roller coster ride")
#         age = int(input("Please enter your AGE"))
        
        
#         if age < 12:
#             bill = 5
#             print("Your child ticket cost is ${bill}")
#         elif age >=12 and age <=18:
#             bill = 7
#             print(f"Your Teenage ticket price is ${bill}")
#         elif age >= 45 or age <= 55:
#             print(f"Your tickect price is ${bill}.")
#         else:
#             bill = 12
#             print(f"Your adult ticket is ${bill}")
        
#         choice = input("You want photos, while you are on the ride? they will charge you $3 extra. Type Y for Yes and N  for No.")
#         if choice == "Y":
#             bill += 3
#             print(f"Your finial bill is ${bill}, Thank you! Enjoy your ride.")
            
# else: 
#         print("Sorry, you are not elegible to ride the roller coster.Thanks for co-opersting.")


#-----------------------------------------------------------------------------------------
# Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.

# Based on a user's order, work out their final bill.

# Small pizza (S): $15

# Medium pizza (M): $20

# Large pizza (L): $25

# Add pepperoni for small pizza (Y or N): +$2

# Add pepperoni for medium or large pizza (Y or N): +$3

# Add extra cheese for any size pizza (Y or N): +$1

# print("Welcome to the PYTHON PIZZA Dilivary")
# size = input("What size pizza do you wnat?Press S for Small; M for Medium; L for Large\n")
# pepperroni = input("Do you want extra pepperoni? $3 for medium and large and $2 for small sixed pizza. Press Y for Yes and N for No.\n")
# cheese = input("Do you want extra cheese? $1 for all sizes of pizza.Press Y for Yes and N for No.")
# bill = 0
# #Conditions:
# if size == "S":
#     bill = 15
#     if pepperroni == "Y":
#         bill += 2
# elif size == "M":
#     bill = 20
#     if pepperroni == "Y":
#         bill += 3
# elif size == "L":
#     bill =25
#     if pepperroni == "Y":
#         bill += 3
# if cheese == "Y":
#     bill += 1
# print(f"Thankyou for choosing Python Pizza, your, total bill is {bill}")
#--------------------------------------------------------------------------------------
# You are going to write a program that tests the compatibility between two people.

# To work out the love score between two people:

# Take both people's names and check for the number of times the letters in the word TRUE occurs.

# Then check for the number of times the letters in the word LOVE occurs.

# Then combine these numbers to make a 2 digit number.

# For Love Scores less than 10 or greater than 90, the message should be:

# "Your score is *x*, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:

# "Your score is *y*, you are alright together."
# Otherwise, the message will just be their score. e.g.:

# "Your score is *z*."
# e.g.

# name1 = "Angela Yu"
# name2 = "Jack Bauer"
# T occurs 0 times

# R occurs 1 time

# U occurs 2 times

# E occurs 2 times

# Total = 5

# L occurs 1 time

# O occurs 0 times

# V occurs 0 times

# E occurs 2 times

# Total = 3

# Love Score = 53

# Print: "Your score is 53."

# These functions will help you:
# lower() count()
#Solution: 
# print("The Love Calculator is calculating your score...")
# name1 = input("What is your name?") # What is your name?
# name2 = input("What is their name?") # What is their name?
# combine = name1 + name2
# lower = combine.lower()
# true_t = lower.count("t")
# true_r = lower.count("r")
# true_u = lower.count("u")
# true_e = lower.count("e")
# true = true_e + true_r + true_u + true_t
# love_l = lower.count("l")
# love_o = lower.count("o")
# love_v = lower.count("v")
# love_e = lower.count("e")
# love = love_l + love_o + love_v + love_e
# love_int = (true*10 + love)
# #Alternative- love_int= int(str(true)+str(ture))
# if love_int < 10 or love_int > 90:
#   print(f"Your score is {love_int}, you go together like coke and mentos.")
# elif love_int >= 40 and love_int <= 50:
#   print(f"Your score is {love_int}, you are alright together.")
# else:
#   print(f"Your score is {love_int}.")
#-------------------------------------------------------------------------------------

#DAY 3- PROJECT - TREASURE ISLAND END
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction_ = input("Which direction you would like to go; Left or Right?")
action_ = input("What is your next action; swim or wait?")
door_ = input("Which color door you want to go through?Red, Blue, Yellow or other?")

direction = direction_.lower()
action = action_.lower()
door = door_.lower()

if direction == "left":
    print(" ʕっ•ᴥ•ʔっ")
    if action == "wait":
        print(""""
 W   W  AAAAA  III TTTTT
 W   W A     A  I   TT
 W W W AAAAAAA  I   TT
 W W W A     A  I   TT
  W W  A     A III  TT
""")
        if door == "red":
            print("Burned by fire! GAME OVER")
        elif door == "blue":
            print("Eater by breasts, Game over.")
        elif door == "yellow":
            print("You Win!")
        else:
            print("GAVE OVER.")
    else:
        print("Attacked by trout. Gave Over.")
else:
    print("Fall into a hole. Game Over.")