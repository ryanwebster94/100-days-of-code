from coffee_data import *


def admin_panel():
    """
    This needs to be streamlined, please give it another try.
    """
    admin = "admin"
    password = "1234"

    attempts = 0
    while attempts < 3:
        username = input("Enter your user name:\n")
        if username != admin:
            print("Please try again.")
        if username == admin:
            enter_password = input("Enter your password:\n")
            if enter_password != password:
                attempts += 1
                print(f"Password invalid: {3 - attempts} remaining")
            


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