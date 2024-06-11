#SUBSCRIPTING
print("Hello"[0])
print("Hello"[4])
print(1000000)
print(1_000_000)


exit()
#I'd like to validate and make some error handling already:
print("Welcome to the tip calculator!\n")
total = input("What was the total bill? R")
total = float(total)
tip = input("How much tip [%] would you like to give? 10, 12, or 15? ")
tip = int(tip)
people = input("How many people to split the bill? ")
people = int(people)

person_contribution = str(total*(1 + tip/100)/people)
print("Each person should pay: R" + person_contribution )
