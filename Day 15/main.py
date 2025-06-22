MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if resources[item] < order_ingredients[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        else:
            return True

def coffee_maker(coffee_type, q, d, n, p):
    if resources["water"] >= MENU[coffee_type]["ingredients"]['water']:
        if resources["milk"] >= MENU[coffee_type]["ingredients"]['milk']:
            if resources["coffee"] >= MENU[coffee_type]["ingredients"]['coffee']:
                print(f"Here is your {coffee_type}.")
            else:
                print("No enough coffee")
        else:
            print("No enough milk")
    else:
        print("No enough water")

    total_money = (q * 0.25) + (d * 0.10) + (n * 0.05) + (p * 0.01)
    if total_money >= MENU[coffee_type]['cost']:
        print(f"Here is your change : {total_money - MENU[coffee_type]['cost']} and here's your coffee. ☕")
    else:
        print("Not enough money. Money refunded")




choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
print("Please insert coins.")
quarters = int(input("how many quarters?: "))
dimes = int(input("how many dimes?: "))
nickles = int(input("how many nickles?: "))
pennies = int(input("how many pennies?: "))

coffee_maker(choice,quarters,dimes, nickles, pennies)