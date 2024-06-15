# Section 8: Day 8 - Beginner - Function Parameters & Caesar Cipher
import my_formating

print(my_formating.logo)

def play_again():
    again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    again = again.replace(" ","")
    again = again.lower()

    if again == "yes":
        ceasers_cipher()
    else:
        exit()

def encoding(message, shift_number):

    encoded = ""
    print(f"Here's the encoded result: {encoded}")
    play_again()
    pass

def decoding(message, shift_number):
    decoded = ""
    print(f"Here's the decoded result: {decoded}")
    play_again()
    pass

def ceasers_cipher():
    goal = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    goal = goal.replace(" ","")
    goal = goal.lower()
    if goal == "encode" or goal == "decode":
        message = input("Type your message:\n")
        shift_number = int(input("Type the shift number:\n"))
    
        if goal == "encode":
            encoding(message, shift_number)
        elif goal == "decode":
            decoding(shift_number = shift_number, message = message)
    else:
        print("You have selected an invalid input.")

ceasers_cipher()

'''
The argument is the pirce of data, whereas the parameter is the name of it
'''
