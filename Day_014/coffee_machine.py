from main import *


def is_resource_sufficient(order_ingredients, ):
    """return True when order can be made, False if ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"sorry, you don't have enough {item}")
            return False
    return True



def process_coin():
    """returns the total calculated from coins entered"""
    print("please insert coin")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many pickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """:return True when the payment is accepted, or False if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"here is the ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("sorry, that's not enough Money. Money refunded")
        return False


def make_coffe(drink_name, order_ingredients):
    """deduct the required ingredients from the resource"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"here is your {drink_name}☕")


profit = 0

is_off = True

while is_off:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_off = False
    elif choice == "report":
        print(f"water: {resources["water"]}ml")
        print(f"milk: {resources["milk"]}ml")
        print(f"coffee: {resources["coffee"]}g ")
        print(f"money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffe(choice, drink["ingredients"])