#Section 5: Day 5 - Beginner - Python Loops

'''
https://haveibeenpwned.com/'''
import random, string

letter_bank = list(string.ascii_letters)
number_bank = list(string.digits)
symbol_bank = list(string.punctuation)

def gen_password(letters, numbers, symbols):
    while True:
        letter_count = 0
        number_count = 0
        symbol_count = 0

        password = []
        while letter_count < letters:
            password.append(random.choice(letter_bank))
            letter_count += 1
        while number_count < numbers:
            password.append(random.choice(number_bank))
            number_count += 1
        while symbol_count < symbols:
            password.append(random.choice(symbol_bank))
            symbol_count += 1 

        #print(f"The created password has {len(password)} characters.")
        #print(password)
        random.shuffle(password)
        password = ''.join(password)

        print(f"Here is your password:  {password}")
        dif_password = input("\nWould you like to generate a new one? [yes/no] ")
        if dif_password.lower() == "yes":
            gen_password(letters, numbers, symbols)
        else:
            break

print("Welcome to the PyPassword Generator!")
    
letters = input("How many letters would you like in your password?\n")
letters = int(letters)
symbols = input("How many symbols would you like?\n")
symbols = int(symbols)
numbers = input("How many numbers would you like?\n")
numbers = int(numbers)

total_char = letters + numbers + symbols
#print(f"You want a password that has {total_char} characters.\n")

gen_password(letters, numbers, symbols)
exit()
    