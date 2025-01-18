from idlelib.configdialog import changes

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

def sufficient_ingredients(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>resources[item]:
            print(f"sorry there is not enough{item}")
            return False
        return True

def process_coins():
    print("please insert coin")
    total = int(input("how many quarters"))*0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def transaction_successful(money_received,drink_cost):
    if money_received>=drink_cost:
        change=round(money_received-drink_cost,2)
        print(f"Here is your change {change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("sorry not enough money")
        return False

def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"Here is your drink{drink_name} ☕️.Enjoy!")




profit=0
resources={
    'water':300,
    'milk':500,
    'coffee':400,
}

status=True
while status:
    choice=input("What would you like? (espresso/latte/cappuccino):")
    if choice=='off':
        status=False
    elif choice=='report':
        water=resources['water']
        milk=resources['milk']
        coffee=resources['coffee']
        print(f"milk:{milk}ml\nwater:{water}ml\ncoffee:{coffee}gm\n")
        print(f"profit:${profit}\n")

    else:
        drink=MENU[choice]
        if sufficient_ingredients(drink['ingredients']):
            payment=process_coins()
            if transaction_successful(payment,drink['cost']):
                make_coffee(choice,drink['ingredients'])












