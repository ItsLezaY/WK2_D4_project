# 1) Create a Module in VS Code and Import It into jupyter notebook

# Module should have the following capabilities:

# 1a) Has a function to calculate the square footage of a house
# Reminder of Formula: Length X Width == Area
# 1b) Has a function to calculate the circumference of a circle 2 Pi r

# Program in Jupyter Notebook should take in user input and use imported functions
# to calculate a circle's circumference or a houses square footage


import math

def calculate_square_footage(length, width):
    return length * width

def calculate_circumference(radius):
    return 2 * math.pi * radius

def calculator_module():
    print("\tHello, please select your choice:\n")
    print("\n1 - Calculate square footage of a house.\n")
    print("\n2 - Calculate circumference of a circle.\n")

    choice = int(input("Enter your choice: \n"))

    if choice == 1:
        length = float(input("\nEnter length of house: "))
        width = float(input("\nEnter width of house: "))
        area = calculate_square_footage(length, width)
        print(f"\nThe square footage of the house is: {area:.2f} square units") # .2f for decimal formatting

    elif choice == 2:
        radius = float(input("\nEnter radius of circle: "))
        circumference = calculate_circumference(radius)
        print(f"\nThe circumference of the circle is: {circumference:.2f}")

    else:
        print("\nPlease select choice 1 or 2.")

calculator_module()



# 2) Build a Shopping Cart Function BUT MAKE IT SPICY WITH SAWCE

# You can use either lists or dictionaries. The program should have the following capabilities:

# 1) Takes in input
# 2) Stores user input into a dictionary or list
# 3) The User can add or delete items
# 4) The User can see current shopping list
# 5) The program Loops until user 'quits'
# 6) Upon quiting the program, print out all items in the user's list

# I'm adding a feature to my shopping cart that takes in a promo code:

# FIXED discount of 20% off

def apply_discount(cart, discount):
    discounted_cart = []
    for item in cart:
        discounted_price = round(item['price'] * (1 - discount), 2)
        discounted_cart.append({'name': item['name'], 'price': discounted_price})
    return discounted_cart

def my_func():
    shopping_cart = []
    promo_code = "DISCOUNT20"  # promo code
    discount = 0.20  # 20% discount

    while True:
        print("\nWhat would you like to do: \n1 - Show Cart\n2 - Add Item\n3 - Delete Item\n4 - Apply Promo Code\n5 - Quit and Checkout")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Here is your current shopping cart:\n")
            for item in shopping_cart:
                print(f"{item['name']}: ${item['price']:.2f}") #.2f to format decimal 
        elif choice == "2":
            item_name = input("Enter item name to add to your cart: ")
            item_price = float(input("Enter item price: "))
            shopping_cart.append({'name': item_name, 'price': item_price})
            print(f"{item_name.title()} added to your cart.")
        elif choice == "3":
            item_name = input("Enter item name to remove from your cart: ")
            for item in shopping_cart:
                if item['name'] == item_name:
                    shopping_cart.remove(item)
                    print(f"{item_name.title()} removed from your cart.")
                    break
            else:
                print(f"{item_name.title()} not found in your cart.")
        elif choice == "4":
            entered_code = input("Enter promo code 'DISCOUNT20' for extra savings: ")
            if entered_code == promo_code:
                shopping_cart = apply_discount(shopping_cart, discount)
                print("Promo code applied. 20% discount has been applied to your cart.")
            else:
                print("Invalid promo code.")
        elif choice == "5":
            print("\nProceed to Checkout:")
            total_price = sum(item['price'] for item in shopping_cart)
            for item in shopping_cart:
                print(f"{item['name']}: ${item['price']:.2f}")
            print(f"Your total is: ${total_price:.2f}")
            break
        else:
            print("I'm sorry. Please type: 1, 2, 3, 4, or 5 to continue.")

my_func()


