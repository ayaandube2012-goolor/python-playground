from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

def coffee_machine():
    coffees = menu.get_items()
    user_choice = input(f"What would you like ({coffees}): ")
    if user_choice == "off":
        quit()
    if user_choice == "report":
        coffee_maker.report()
        money_machine.report()
        coffee_machine()

    coffee_option = menu.find_drink(user_choice)
    if coffee_option is None:
        coffee_machine()
    else:
        sufficient_resources = coffee_maker.is_resource_sufficient(coffee_option)
        if sufficient_resources:
            sufficient_money = money_machine.make_payment(coffee_option.cost)
            if sufficient_money:
                coffee_maker.make_coffee(coffee_option)
            else:
                coffee_machine()
        else:
            coffee_machine()


coffee_machine()
