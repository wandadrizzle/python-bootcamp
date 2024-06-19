# Coffee Machine Project
import os
import time

MILK = 0
WATER = 0
COFFEE = 0
MONEY = 0

coins = [
    {"name": "quarter", "value": 0.25, "tag": "q"},
    {"name": "dime", "value": 0.10, "tag": "d"},
    {"name": "nickel", "value": 0.05, "tag": "n"},
    {"name": "penny", "value": 0.01, "tag": "p"},
]

drinks = {
    "espresso": {"price": 0, "water": 0, "milk": 0, "coffee": 0},
    "latte": {"price": 0, "water": 0, "milk": 0, "coffee": 0},
    "cappuccino": {"price": 0, "water": 0, "milk": 0, "coffee": 0},
}


def print_report():
    print("The machine currently has the following:")
    print(f"Water: {WATER} ml\nMilk: {MILK} ml\nCoffee: {COFFEE}g\nMoney: ${MONEY}")


def check_resources():
    pass


def process_coins():
    pass


def transact():
    pass


def make_coffee():
    pass


def get_order():

    order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if order == "espresso":
        pass
    elif order == "latte":
        pass
    elif order == "cappuccino":
        pass
    elif order == "report":
        print_report()
    elif order == "cancel" or order == "off":
        print("Good bye, come back for a cup of Joe next time.")
        exit()
    else:
        print(f"It seems like you have have selected an invalid input or this machine can't make a/an '{order}'"
              f" for you.\nBe sure to double check your spelling before ordering again.\n")
        time.sleep(3)
        os.system('cls')
        get_order()


get_order()
