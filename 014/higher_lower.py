from random import randint
import art_and_data as w, os, time


DATA_QUANTITY = len(w.accounts)
SCORE = 0

#print(f"There are {DATA_QUANTITY} accounts in my Instagram follower log.")

def get_comparisons(num1,num2, score):
    '''Compares two instagram accounts and changes the player's score accordingly'''
    print(f"Compare A: {w.accounts[num1]["name"]}, a/an {w.accounts[num1]["description"].lower()}, from {w.accounts[num1]["country"].title()}")
    print(w.vs)
    print(f"Compare B: {w.accounts[num2]["name"]}, a/an {w.accounts[num2]["description"].lower()}, from {w.accounts[num2]["country"].title()}")

    A = w.accounts[num1]["follower_count"]
    B = w.accounts[num2]["follower_count"]

    #print(A, B)

    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    if (guess == "A" and ( A > B)) or (guess == "B" and ( B > A)):
        score += 1
        print(f"{w.GREEN}You're right! Current score: {score}.{w.RESET}")
        time.sleep(3)
        game(score)
    else:
        print(f"{w.RED}Sorry, that's wrong. Final score: {score}{w.RESET}")
        exit()

def game(initial_score):
    '''Clears the UI and creates a new Instagram account guessing case.'''
    os.system('cls')
    #os.system('cls' if os.name == 'nt' else 'clear')
    print(w.logo)
    score = initial_score
    a = randint(0, DATA_QUANTITY - 1)
    b = randint(0, DATA_QUANTITY - 1)
    while  a == b:
        b = randint(0, DATA_QUANTITY - 1)
      
    get_comparisons(a, b, score)


game(SCORE)