MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0

# TODO: 1. Ask user about coffee

def coffee_machine(money_amount):
    change = 0
    coffee_option_resources = ""
    coffee_option = ""
    option = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()

    # TODO: 2. Check if they are turning it off

    if option == "off":
        quit()

    # TODO: 3. check for report

    if option == "report":
        print(f"water: {resources["water"]}ml")
        print(f"milk: {resources["milk"]}ml")
        print(f"coffee: {resources["coffee"]}g")
        print(f"money: £{money_amount}")
        coffee_machine(money_amount)

    # TODO: 4. check refill

    if option == "refill":
        if resources["water"] < 300 or resources["milk"] < 200 or resources["coffee"] < 100:
            resources["water"] = 300
            resources["milk"] = 200
            resources["coffee"] = 100
            coffee_machine(money_amount)
        else:
            print("Sorry, but you seem fully stocked")
            coffee_machine(money_amount)

    # TODO: 5. check if enough resources

    if option == "espresso":
        coffee_option = MENU["espresso"]
        coffee_option_resources = coffee_option["ingredients"]
    elif option == "latte":
        coffee_option = MENU["latte"]
        coffee_option_resources = coffee_option["ingredients"]
    elif option == "cappuccino":
        coffee_option = MENU["cappuccino"]
        coffee_option_resources = coffee_option["ingredients"]
    if (
        coffee_option_resources["water"] > resources["water"]
        or coffee_option_resources["milk"] > resources["milk"]
        or coffee_option_resources["coffee"] > resources["coffee"]
    ):
        print("Sorry, but there doesn't seem to be enough resources, please refill.")
        coffee_machine(money_amount)

    # TODO: 6. process coins

    two_pounds = int(input("How many £2 coins: "))
    one_pounds = int(input("How many £1 coins: "))
    fifty_pence = int(input("How many 50p coins: "))
    twenty_pence = int(input("How many 20p coins: "))
    ten_pence = int(input("How many 10p coins: "))

    money_paid = (two_pounds * 2) + one_pounds + (fifty_pence * 0.50) + (twenty_pence * 0.20) + (ten_pence * 0.10)

    # TODO: 7. chck transaction

    if money_paid < coffee_option["cost"]:
        print("HOW DARE YOU TRY TO SCAM US WITH INSUFFICIENT MONEY !!!")
        print("Your money has been refunded")
        coffee_machine(money_amount)

    # TODO: 8. make coffee

    resources["water"] -= coffee_option_resources["water"]
    resources["milk"] -= coffee_option_resources["milk"]
    resources["coffee"] -= coffee_option_resources["coffee"]
    money_amount += coffee_option["cost"]
    money_amount = round(money_amount, 2)
    change = money_paid - coffee_option["cost"]
    change = round(change, 2)

    print(f"Your change is £{change}")
    print(f"Here is your {option}. Enjoy!")
    coffee_machine(money_amount)

coffee_machine(money)