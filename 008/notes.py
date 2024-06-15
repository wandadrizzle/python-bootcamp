# Section 8: Day 8 - Beginner - Function Parameters & Caesar Cipher
import my_formating, string

print(my_formating.logo)
#alphabets = string.ascii_lowercase * 2
#alphabets =  list(alphabets)
#print(alphabets)

def play_again():
    again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    again = again.replace(" ","")
    again = again.lower()

    if again == "yes":
        ceasers_cipher()
    else:
        exit()

def encoding(message, shift_number):

    alphabets = string.ascii_lowercase * shift_number
    alphabets =  list(alphabets)

    encoded = []
    for letter in message:
        if letter in alphabets:
            index = alphabets.index(letter)
            letter = alphabets[index + shift_number]

        encoded.append(letter)

    encoded = ''.join(encoded)
    print(f"Here's the encoded result: {encoded}")
    play_again()

def decoding(message, shift_number):
    alphabets = string.ascii_lowercase * shift_number
    alphabets =  list(alphabets)

    decoded = []
    for letter in message:
        if letter in alphabets:
            index = alphabets.index(letter)
            letter = alphabets[index - shift_number]

        decoded.append(letter)
    decoded = ''.join(decoded)
    print(f"Here's the decoded result: {decoded}")
    play_again()

def ceasers_cipher():
    goal = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    goal = goal.replace(" ","")
    goal = goal.lower()
    if goal == "encode" or goal == "decode":
        message = input("Type your message:\n").lower()
        shift_number = int(input("Type the shift number:\n"))
    
        caesar(message, shift_number, goal)
        '''
        if goal == "encode":
            encoding(message, shift_number)
        elif goal == "decode":
            decoding(shift_number = shift_number, message = message)
        '''
    else:
        print("You have selected an invalid input.")

def caesar(message, shift_number, direction):
    alphabets = string.ascii_lowercase * shift_number
    alphabets =  list(alphabets)

    if direction == "encode":
        dc = "encoded"
    elif direction == "decode":
        dc = "decoded"
        shift_number = - shift_number
    else:
        print("UFUNA UKWENZANI?")
        return

    c = []
    for letter in message:
        if letter in alphabets:
            index = alphabets.index(letter)
            letter = alphabets[index + shift_number]

        c.append(letter)
    c = ''.join(c)
    print(f"Here's the {dc} result: {c}")
    play_again()


ceasers_cipher()

'''
The argument is the pirce of data, whereas the parameter is the name of it
'''
