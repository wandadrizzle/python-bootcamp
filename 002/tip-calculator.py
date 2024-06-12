print("Welcome to the tip calculator!\n")
total = input("What was the total bill? R")
total = float(total)
tip = input("How much tip [%] would you like to give? 10, 12, or 15? ")
tip = int(tip)
people = input("How many people to split the bill? ")
people = int(people)

person_contribution = str(round(total*(1 + tip/100)/people, 2))
#You can round like so: "{:.2f}".format(bill_per_person)
print("Each person should pay: R" + person_contribution )

exit()
#The len() function doesn't like integers

#SUBSCRIPTING
print("Hello"[0])
print("Hello"[4],"\n")
print(1000000)
print(1_000_000)
print()
a = 7
b = "Seven"
c = 7.0

print(type(a), type(b), type(c))

d = str(a)
e = True
f = int(e)

print(type(d), type(e), type(f))
age = 27
print(f"she is {age} years old.") #f-string
#PEMDAS [LR]
print()
print(3**2)
print(3*3+3/3-3)
print(3*(3+3)/3-3)
print(3-3+3/3*3) #Not what she meant by modify to get 3

print()
print(round(8/3, 2))
print(8//3)
print(6 + 4 / 2 - (1 * 2))
print()
print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

score_1 = 0
score_2 = 0
both_names = (name1 + name2).upper()

print(both_names.count("E")) #alternatively you can do that!

for char in both_names:
  if char == "T" or char == "R" or char == "U" or char == "E":
    score_1 += 1
  if char == "L" or char == "O" or char == "V" or char == "E":
    score_2 += 1

score = int(str(score_1)+str(score_2))
if score > 90 or score < 10:
  print("Your score is " + str(score) + ", you go together like coke and mentos."
)
elif score > 40 and score < 50:
   print("Your score is " + str(score) + ", you are alright together.")
else:
  print("Your score is " + str(score) + ".")

exit()
#I'd like to validate and make some error handling already:
