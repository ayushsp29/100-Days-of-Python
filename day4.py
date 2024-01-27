"""
DAY 4- Randomisation and Python List
"""
# import random
# random_int = random.randint(0,10)
# print(random_int)

# random_float = random.random()
# random_float * 5
# print(random_float)

# love_score = random.randint(0,100)
# print(f"Your love score is {love_score}")
#------------------------------------------------------------------------------------------------------------

#Heads and Tails Generator

# import random
# number_generator = random.randint(0,1)
# if number_generator == 1:
#   print("Heads")
# else:
#   print("Tails")

#-------------------------------------------------------------------------------------------------------------
#Lists- Data Structure
#Syntax- List = [item1, itme2, ......, item n ]
#List maintains the order of the data tooo... and can be accessed as - print(list_name[0...index])
# List = ["Ayush", "Sachin", "Patil"]
# print(List[0])
# print(List[-1])
# List[1] = "Ayuuu"
# print(List[1])
# print(List)
#-----------------------------------------------------------------------------------------------------------
# Question-You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

# Important: You are not allowed to use the choice() function.

# Line 1 splits the string names_string into individual names and puts them inside a List called names. For this to work, you must enter all the names as names followed by comma then space. e.g. name, name, name

# NOTE: Don't worry about getting hold of the input(), we've done the work behind the scenes to import everything.

# HINT: Assume that names looks like this: input: x, y, z, names = ["x", "y", "z"]
#---------------------- Answer ---------------------------------------------
# names = names_string.split(", ")

# import random
# length = len(names)
# random_choice = random.randint(0, length -1)
# bill = names[random_choice]
# print(f'{bill} is going to buy the meal today!')
#-----------------------------------------------------------------------------------------

#Nested Lists:
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
# dirty_dozen = [fruits, vegetables]
 
# # print(dirty_dozen[0])
# # print(dirty_dozen[1])
# print(dirty_dozen[1][1])
#------------------------------------------------------------------------------------------------------
#Rock paper sessior game
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to Rock-Paper-Scissors Game")
print("Rules for the Game-\n 1.Rock wins against scissors.\n 2.Scissors win against paper.\n 3.Paper wins against rock.")
user_raw= input("Press:\n R for Rock\n P for Paper\n S for Scirrors\n")
user = user_raw.upper()
user = str(user)
pc = random.randint(0,2)
# #Conditions:
if user == "R":
    if pc == 0:
        print("Your choice is Rock")
        print(rock)
        print("Computer choice is Rock")
        print(rock)
        print("Game is Tie.")
    elif pc == 1:
        print("Your choice is Rock")
        print(rock)
        print("Computer choice is Paper")
        print(paper)
        print("You Loose!")
    else:
        print("Your choice is Rock")
        print(rock)
        print("Computer choice is Scissors")
        print(scissors)
        print("You Win!")
elif user == "P":
    if pc == 0:
        print("Your choice is Paper")
        print(paper)
        print("Computer choice is Rock")
        print(rock)
        print("You win")
    elif pc == 1:
        print("Your choice is Paper")
        print(paper)
        print("Computer choice is Paper")
        print(paper)
        print("Game is Tie.")
    else:
        print("Your choice is Paper")
        print(paper)
        print("Computer choice is Scissors")
        print(scissors)
        print("You Loose!")
elif user == "S":
    if pc == 0:
        print("Your choice is Scissors")
        print(scissors)
        print("Computer choice is Rock")
        print(rock)
        print("You Loose!")
    elif pc == 1:
        print("Your choice is Scissors")
        print(scissors)
        print("Computer choice is Paper")
        print(paper)
        print("You win")
    else:
        print("Your choice is Scissors")
        print(scissors)
        print("Computer choice is Scissors")
        print(scissors)
        print("Game is Tie.")
else:
    print("Please choose correct option and try again, Thanks!")