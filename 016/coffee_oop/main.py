from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import my_art

m = Menu()
cm = CoffeeMaker()
zar = MoneyMachine()


def price_list():
    print("\nThe prices are as follows:")
    items = m.get_items().replace("/", " ")
    items = items.strip()
    item_list = items.split(" ")

    for item in item_list:
        x = m.find_drink(item)
        print(f"{x.name.title()}:\t${x.cost}")


def get_order():
    print(my_art.art)
    print("Hidden prompts include 'report', 'prices' to see the price-list and 'off' to switch the machine off.")
    my_order = input(f"What would you like? ({m.get_items()}): ").lower()
    order = m.find_drink(my_order)
    # print(order.ingredients)
    if my_order == "off":
        exit()
    elif my_order == 'prices':
        price_list()
        get_order()
    elif my_order == "espresso" or my_order == "latte" or my_order == "cappuccino":
        mi = MenuItem(order.name, order.ingredients['water'], order.ingredients['milk'],
                      order.ingredients['coffee'], order.cost)

        can_make_coffee = cm.is_resource_sufficient(mi)
        pay = zar.make_payment(order.cost)
        if can_make_coffee and pay:
            cm.make_coffee(mi)
        get_order()
    elif my_order == "report":
        cm.report()
        zar.report()
        get_order()


# price_list()
# get_order()


# Need to get used to creating while loops that break after a condition change - PRACTICE DONE BELOW

while True:
    print(my_art.art)
    print("Hidden prompts include 'report', 'prices' to see the price-list and 'off' to switch the machine off.")
    my_order2 = input(f"What would you like? ({m.get_items()}): ").lower()
    order2 = m.find_drink(my_order2)
    # print(order.ingredients)
    if my_order2 == "off":
        break
    elif my_order2 == 'prices':
        price_list()
    elif my_order2 == "espresso" or my_order2 == "latte" or my_order2 == "cappuccino":
        mi2 = MenuItem(order2.name, order2.ingredients['water'], order2.ingredients['milk'],
                       order2.ingredients['coffee'], order2.cost)

        can_make_coffee2 = cm.is_resource_sufficient(mi2)
        pay2 = zar.make_payment(order2.cost)
        if can_make_coffee2 and pay2:
            cm.make_coffee(mi2)
    elif my_order2 == "report":
        cm.report()
        zar.report()

# Okay, so the only thing I don't like now is the fact that there are inputs that break my code
# AND the "Sorry that item is not available." line gets printed even when it shouldn't be
