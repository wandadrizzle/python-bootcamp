import os, random, other_deets as w

#Assuming an infinite deck, I chose the "Expect Level" difficulty, my code looks the way it does because I didn't use all of the hints.

cards = {
    "Ace": [1, 11],
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 10,
    "Jack": 10,
    "Queen": 10,
    "King":10,
}

def draw_cards(amount, store):
    count = 0
    card_names = list(cards.keys())
    
    while count < amount:
        card = random.choice(card_names)
        store.append(card)
        count += 1

    return store

def count_score(score, store):
    for v in store:
        if v == "Ace":
            score += cards["Ace"][1]
        else:
            score += cards[v]

    if "Ace" in store and score > 21:
            score -= 10
    return score

def result(player_array, player_score, computer_array, computer_score):

    player_total = count_score(player_score, player_array)
    computer_total = count_score(computer_score, computer_array)

    if player_total > 21:
        return "Bust, you lose!"
    elif player_total > computer_total and player_total <= 21:
        return "You Win! 👑"
    elif player_total < computer_total and computer_total <= 21:
        return "You Lose 😔"
    elif player_total == computer_total:
        return "It's a draw? 🃏"


def blackjack():
    print(w.logo)
    your_cards = []
    your_score = 0
    computers_cards = []
    computers_score = 0
    your_cards = draw_cards(2, your_cards)
    computers_cards = draw_cards(2, computers_cards)

    while count_score(computers_score, computers_cards) < 17:
                computers_cards = draw_cards(1, computers_cards)

    print(f"Your cards: {your_cards}\nComputer's first card: {computers_cards[0]}")
    while True:
        game = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if game == 'y':
            your_cards = draw_cards(1, your_cards)

            print(f"Your cards: {your_cards}\nComputer's first card: {computers_cards[0]}")
            continue
        elif game == 'n':
            print(f"Your final hand: {your_cards}\nComputer's final hand: {computers_cards}")
            print(result(your_cards, your_score, computers_cards, computers_score))
            to_play()
        else:
            print("You killed the game!")
            os.system('cls')
            exit()
    

def to_play():
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if play == 'y':
        os.system('cls')
        blackjack()
    elif play == 'n':
        print("I respect that, wouldn't want you to pick up a gambling habit.")
        exit()
    else:
        print("Don't jest with me. That's an invalid input.")
        print(w.joker)
        exit()

to_play()