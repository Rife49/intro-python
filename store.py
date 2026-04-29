from math import prod

from catalog import catalog # import your catalog dictionary

cart = [] # Global variable empty list

# Header/ Helper Functions
def print_header(text):
    print("------------------------")
    print(text)
    print("------------------------")
    
    
def menu():
    print("Menu")
    print(" 1. - View Catalog")
    print(" 2. - Search Product")
    print(" 3. - View Cart")
    # Add more functions 
    print(" 4. - Clear Cart")
    print(" Q. - Quit")

# Catalog and Cart Functions

def print_catalog():
    print_header("-Our catalog -")
    for prod in catalog:          # Ljust (left justify). 15 spaces to the right
        print(f"| {prod["id"]} | {prod["title"].ljust(15)} | ${prod["price"]:.2f}")
        
        # Implemnting adddinf product function
    answer = input("Type ID to add ( N to close): ")
    if answer.lower() == "n":
        return
    else:
        add_product_to_cart(answer)
        print("------------------")
        
        
def add_product_to_cart(prod_id):
    found = False 
    for prod in catalog:
        if str(prod["id"]) == str(prod_id):
            found = True
            cart.append(prod) # add product to the end of the cart
            print(f"{prod["title"]} added to your cart.")
            break # stop after finding the product
        
        
    if not found:
            print("***ERROR: Invalid ID")
            print("--------------------")
            
            
def search_product():
    text = input("Search product title: ").lower()
    found = False
    for prod in catalog:
        if text in prod["title"].lower():
            found = True
            print(f"| {prod["id"]} | {prod["title"].ljust(15)} | ${prod["price"]:.2f}")
            choice = input(" Do you want to add this item to your cart? (y/n)? ")
            if choice.lower() == "y":
                add_product_to_cart(prod["id"])
            break # stop after first match
        
    if not found:
        print("Sorry, this item doesn't exist.")
        print("-------------------------------")


# create a function view_cart()
# print a header call it "your Cart"
# use if and else to print out all items in your cart

def view_cart():
    print_header("Your Cart")
    if not cart:         # checking if cart is empty
        print("Your cart is empty")
    else:
        for prod in cart:  # looping through every item in cart
            print(f"| {prod["id"]} | {prod["title"].ljust(15)} | ${prod["price"]:.2f}")
        cart_total()
        
# function cart_total()
# variable total = 
# for loop to add the price of every product
# print the total

def cart_total():
    total = 0
    for prod in cart:
        total += prod["price"]
    print(f"Total: ${total}")
    
    
# Clear Cart
def clear_cart():
    cart.clear()
    print("Your cart is empty")


# Main program loop
option = ""
while option != "q" and option != "Q":
    print_header("Welcome to the store")
    menu()
    
    option = input("Choose an option: ")
    
    if option == "1":
        print_catalog()
    elif option == "2":
        search_product()
    elif option == "3":
        view_cart()
    elif option == "4":
        clear_cart()
    elif option == "q" or option =="Q":
        print("Quit")
    else:
        print( "** Error: invalid options")
        print("--------------------------")
        
