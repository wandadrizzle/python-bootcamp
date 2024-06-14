# Section 7: Day 7 - Beginner - Hangman, I did it by myself

#https://developers.google.com/edu/python/lists#for-and-in, https://developers.google.com/edu/python, https://www.askpython.com/python/python-import-statement

hangman_ascii = r"""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/ 
"""

hangman_stages = [
    r"""
      _______
     |/      |
     |
     |
     |
     |
     |
    _|___
    """,
    r"""
      _______
     |/      |
     |      (_)
     |
     |
     |
     |
    _|___
    """,
    r"""
      _______
     |/      |
     |      (_)
     |       |
     |
     |
     |
    _|___
    """,
    r"""
      _______
     |/      |
     |      (_)
     |      \|
     |
     |
     |
    _|___
    """,
    r"""
      _______
     |/      |
     |      (_)
     |      \|/
     |
     |
     |
    _|___
    """,
    r"""
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |
     |
    _|___
    """,
    r"""
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      /
     |
    _|___
    """,
    r"""
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \
     |
    _|___
    """
]

import my_words, random, os

print(hangman_ascii) #Note that it's printed as a raw string
print(hangman_stages[0])


def play():
    word = "PLACEHOLDER"
    game_list = []
    first_rand = random.randint(0,1)
    if first_rand == 0:
        game_list = my_words.produce_list
    else:
        game_list = my_words.random_list
    
    word = random.choice(game_list)
    #print(f"Pssst, the solution is {word}.) Just checking whether it got randomised or not! :)
    revealed_word = ""

    for char in word:
        revealed_word += "-"
    lives_lost = 0
    print(revealed_word)
    while lives_lost < 7:

        guess = input("Guess a letter: ")
        os.system('cls')
        guess = guess[0].upper()
        if guess in word:
            loop = 0
            revealed_word = list(revealed_word)
            while loop < len(word):
                if guess == word[loop]:
                    revealed_word[loop] = guess
                loop += 1
            revealed_word = ''.join(revealed_word)

            if "-" not in revealed_word:
                print(revealed_word)
                print ("\nYou win! 🏆")
                break
            
        else:
            lives_lost += 1
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            if lives_lost  == 7:
                print(f"Game Over! 💀\nThe word was {word}.")
            print(hangman_stages[lives_lost])

        print(revealed_word)



play()