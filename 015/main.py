# Coffee Machine Project
import os
import time

# The milk and water quantities are in milliliters and the coffee is in grams
# These aren't constant per se. They are GLOBAL - might need to rethink this
MILK = 400
WATER = 750
COFFEE = 120
MONEY = 5

coins = {
    "q": {"name": "quarter", "value": 0.25, "plural": "quarters"},
    "d": {"name": "dime", "value": 0.10, "plural": "dimes"},
    "n": {"name": "nickel", "value": 0.05, "plural": "nickels"},
    "p": {"name": "penny", "value": 0.01, "plural": "pennies"},
}

drinks = {
    "espresso": {"price": 1.5, "water": 30, "milk": 0, "coffee": 9},
    "latte": {"price": 3.75, "water": 45, "milk": 135, "coffee": 9},
    "cappuccino": {"price": 4.25, "water": 50, "milk": 100, "coffee": 9},
    # A cappuccino has roughly 50 ml steamed milk and 50 ml milk foam
}

art = r'''
          )))
         (((
       +-----+
       |     |]
       `-----'    
     ___________
     `---------'
WANDA'S COFFEE MACHINE
'''

off = r'''
                                                 ad88                                    88                        
                          ,d                    d8"                                      88                        
                          88                    88                                       88                        
 ,adPPYba,  88       88 MM88MMM     ,adPPYba, MM88MMM     ,adPPYba,  8b,dPPYba,  ,adPPYb,88  ,adPPYba, 8b,dPPYba,  
a8"     "8a 88       88   88       a8"     "8a  88       a8"     "8a 88P'   "Y8 a8"    `Y88 a8P_____88 88P'   "Y8  
8b       d8 88       88   88       8b       d8  88       8b       d8 88         8b       88 8PP""""""" 88          
"8a,   ,a8" "8a,   ,a88   88,      "8a,   ,a8"  88       "8a,   ,a8" 88         "8a,   ,d88 "8b,   ,aa 88          
 `"YbbdP"'   `"YbbdP'Y8   "Y888     `"YbbdP"'   88        `"YbbdP"'  88          `"8bbdP"Y8  `"Ybbd8"' 88   
'''


def print_report():
    print("The machine currently has the following:")
    print(f"Water: {WATER} ml\nMilk: {MILK} ml\nCoffee: {COFFEE}g\nMoney: ${MONEY}")
    time.sleep(3)
    get_order()


def check_resources(drink):
    water_required = drinks[drink]["water"]
    milk_required = drinks[drink]["milk"]
    coffee_required = drinks[drink]["coffee"]

    if water_required > WATER:
        print("Sorry there is not enough water.")
    if milk_required > MILK:
        print("Sorry there is not enough milk.")
    if coffee_required > COFFEE:
        print("Sorry there is not enough coffee.")

    if water_required <= WATER and milk_required <= MILK and coffee_required <= COFFEE:
        process_coins(drink)


def process_coins(drink):
    """Processes the coins the user has added and thereafter makes an order transaction."""
    money_required = drinks[drink]["price"]
    coin_combo = {}
    print("Take a moment to separate by type. Then 'insert' them as such.")
    time.sleep(2)

    for coin in coins:
        # print(coins[coin])
        coin_quantity = int(input(f"How many {coins[coin]['plural']} do you have? "))
        coin_combo.update({coin: coin_quantity})
        # print(coin_combo)

    total_money = 0
    for money in coin_combo:
        total_money += (coins[money]['value'] * coin_combo[money])

    total_money = round(total_money, 2)
    print(f"\nYou have added ${total_money}.")

    if money_required > total_money:
        print("Sorry that's not enough money. Money refunded.")
        get_order()
    else:
        change = total_money - money_required
        if money_required < total_money:
            print(f"Here is ${round(change, 2)} dollars in change.\n")
        make_coffee(drink, money_required)


def price_list():
    print("\nThe prices are as follows:")
    for coffee in drinks:
        print(f"{coffee.title()}:\t${drinks[coffee]['price']}")
    time.sleep(3)
    get_order()


def make_coffee(drink, drink_price):
    global MILK
    global WATER
    global COFFEE
    global MONEY

    MILK -= drinks[drink]["milk"]
    WATER -= drinks[drink]["water"]
    COFFEE -= drinks[drink]["coffee"]
    MONEY += drink_price
    print(f"Here enjoy your {drink}. ☕\n")
    print_report()


def get_order():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(art)
    print("Hidden prompts include 'report', 'prices' to see the price-list and 'off' to switch the machine off.")
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if order == "espresso" or order == "latte" or order == "cappuccino":
        check_resources(order)
    elif order == "report":
        print_report()
    elif order == 'prices':
        price_list()
    elif order == "cancel" or order == "off":
        print("Good bye, come back for a cup of Joe next time.")
        print(off)
        exit()
    else:
        print(f"It seems like you have have selected an invalid input or this machine can't make a/an '{order}'"
              f" for you.\nBe sure to double check your spelling before ordering again.\n")
        time.sleep(3)
        get_order()


get_order()
