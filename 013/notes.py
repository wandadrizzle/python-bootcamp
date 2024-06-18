############DEBUGGING#####################

# # Describe Problem
def my_function():
  #for i in range(1, 20): #Range DOESN'T include the upper limit
  for i in range(1, 20 + 1): #Range DOESN'T include the upper limit
    if i == 20:
      print("You got it")
my_function()

print()
# # Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
#dice_num = randint(1, 6) #It's possible to get an IndexError here since ito arrays index 5 = number 6
#print(dice_num) #This is how I'm gonna check what produces the bug
#dice_num = 6 #This is how I'm gonna reproduce the bug
dice_num = randint(0, 5) #This is the FIX
print(dice_imgs[dice_num])

print()
# # Play Computer
year = int(input("What's your year of birth? "))
if year <= 1980:
  print('You could be "The Greatest Generation (GI Generation)", "The Silent Generation", "Baby Boom Generation" or "Generation Z" ')
elif year > 1980 and year <= 1996:
  print("You are a Millenial.")
elif year >= 1997 and year < 2010:
  print("You are a Gen Z.")
else:
  print("Gen Alpha?")

print()
# # Fix the Errors
age = int(input("How old are you? "))
if age >= 18:
    print(f"You can drive at age {age}.")

print()
# #Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

# #Use a Debugger, https://pythontutor.com/python-compiler.html#mode=edit
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])