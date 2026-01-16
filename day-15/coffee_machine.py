from coffee_data import *


def admin_panel():
    """
    This needs to be streamlined, please give it another try.
    """
    admin_username = "Ryan"
    admin_password = "1234"
    attempts = 0

    while attempts < 3:
        

def process_payment():
    pass


def make_coffee():
    pass


machine_state = True

while machine_state:
    choice = input(
        "Please enter your choice of drink (espresso | latte | cappuccino):\n"
        ).lower()

    if choice == "admin":
        admin_panel()

    if choice in MENU:
        valid = process_payment()
        if valid:
            make_coffee()
    else:
        print(f"{choice.title()} is not an available option. Please try again.")