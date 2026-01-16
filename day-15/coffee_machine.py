from coffee_data import *


def admin_panel(choice):
    """
    A panel that can only be accessed with username and password.
    Access grants the user to view resources, refill the machine and turn
    the machine off. 
    """
    admin_username = "Ryan"
    admin_password = "1234"
    attempts = 0

    while attempts < 3:
        username = input("Enter your username:\n")
        password = input("Enter your password:\n")
        if username != admin_username and password != admin_password:
            print("Invalid credentials, please try again.")
        
        if username == admin_username and password == admin_password:
            if choice == "off":
                return True
            if choice == "refill":
                # Logic for refilling coffee_data(resources)
                pass

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
        state, resources, refill = admin_panel(choice)

    if choice in MENU:
        pennies = input("How many pennies: ")
        valid = process_payment()
        if valid:
            make_coffee()
    else:
        print(f"{choice.title()} is not an available option. Please try again.")