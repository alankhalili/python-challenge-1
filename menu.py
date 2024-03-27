# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

    # Set up a list that will store a list of dictionaries.
    # The dictionaries will be used to:
    #   (a) that associates an item number to a item of food and the price.
    #   (b) that list will also be used to associate the quanity ordered to the 
    #       above. 
order_list = []

    # Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

    # Customers may want to order multiple items, so let's create a continuous
    # loop.  For continuous loops, a "While" True loop is optimal.
    # Prior to the loop, we must establish, outside the loop, that place_order
    # statement is true for the first loop.  Thereafter, the customer imput
    # will drive the extent the loop repeats itself.
place_order = True
while place_order:

    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable to associate an item number to the food.
    i = 1
#1 Create a dictionary to store the numbered menu categories for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in the "menu").

    #Create a for/in statement to run through the list of key items in the
    # "menu".  This will create a numbered list of menu categories and 
    # store that list as a dictionary. 
     
    #   The items in "menu" will be temporarily assinged to the variable "key"
    #   The function 'dictionary'.key() will be menu.key().  This will run through each 
    #   key in the menu dictionary.
    for key in menu.keys():
        # in first loop, print 1 for the variable "i" and the first key item (first menu category on the list) from the dictionary
        # in the nth loop, will print the nth number that reflects the nth key item (menu category), 
        #followed by the nth key item (menu category) from the dictionary "menu"
        print(f"{i}: {key}")
        # Pooulate the menu_item dictionary.  The key will be the variable "i" and 
        # the value will be the cooresponding key from the "menu" dictionary.  From the "menu_items" dictionary's perspective,
        # "i" will be the key and menu category will be the value.
        # for the first loop, this will be "1" : "Snacks"
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1
        # This will loop back up until all keys from the "menu" dictionary has been listed.

    # Get the customer's input regarding what category they want to see the details (sub-categories).
    menu_category = input("Type menu number: ")

    # Before we can print the sub categories from the menue, we need to make sure the number selected
    # can be used.
    
#3   Check if the customer's input is a number, then...
    if menu_category.isdigit():
        # Check if the customer's input is a valid option from the "menu_items" dictionary created to 
        # assign a number to a category.
        # We must make sure the nubmer selected is a key item from the "menu_item" dictionary 
        # that is storing the itemized list of menu categories created around line 97. 
        # we will create a variable called "int(menu_category)" to go down the list of key items in the menu_items disctionary.
            #note that doens't ensure the number is an interger.
        if int(menu_category) in menu_items.keys():
        
        # We must now print the selected category and it's components from the "menu"
            # We will pull the selected category's name from the "menu_item" dictonary that has assoicated the # with the menu category.
            # The key for the menu_items dictionary is the "menu_category" selected and the value is the category that was entered in line 97 
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
           # Create a dictionary to track the menu items name and prices presented.
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            
            # create two variables,"key" and "value" that will be assigned the key and value from
            # the menu items (the sub dictionary in "menu" dictionary via the code on lines 121, 116 103 97 and 76).
            # the ".items()" fuction will be used to pull the key and value from the
            # "menu" sub dictionary and assign those values to the veriables "key" and "value"
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                # Use the type() function on the  "value" varible to direct data handeling.
                # for a dictionary within a dictionary (exmple, varieity of pizza or coffe drings), we need to extract the key and value from the menu sub dictionary called "menu_category_name" see code line 121
                if type(value) is dict:
                    for key2, value2 in value.items():
                        #print formatting
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        #print the item number, the item category, the food item and cost.
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        # Establishes several key/value pairs that will make up the menu_item dictionary
                            # key1 is = "i"
                            # value1 = sub dictionary with 
                                        # [category and ]food item above as one key/value pair   
                                        # price = $ price value as one key/value pair
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                # if the items extracted isn't a dictionary, but a stirng (burrito or sushi), this prints the string directly.
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    # expands the menu_item dictionary for string additions.
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
#2 Ask customer to input menu item number
            menu_selection = input(f"\nType the menu number you wish to order or q to quit:  ")
        # Exit loop if "q" is selected
        if menu_selection.lower() == "q":
            break
       

#3 Check if the customer typed a number
        if menu_selection.isdigit():
            # Convert the menu selection to an integer.   Needed to do the operation below.
            menu_selection = int(menu_selection)
       
#4 Check if the menu selection is in the menu items
            if menu_selection in menu_items.keys():

                # Store the item name as a variable.
                # "Item name" and "Price" was associated with the food item on lines 154 and 165
                menu_selection_name = menu_items[menu_selection]["Item name"]
                menu_selection_price = menu_items[menu_selection]["Price"]
                # Ask the customer for the quantity of the menu item
                quantity = input(f'\nHow many {menu_selection_name} do you want? If you make an invalid selection, the quantity will default to one {menu_selection_name}. ')

                # Check if the quantity is a number, default to 1 if not # Additional check for positive integer
                if not quantity.isdigit() or int(quantity) <= 0:  
                    quantity = 1 

                # Add the item name, price, and quantity to the order list (line 58, created to track orders)
                # this list has a dictionary in it.
                order_list.append({
                    "Item name" : menu_selection_name,
                    "Price" : menu_selection_price,
                    "Quantity" : quantity        
                })

                # Tell the customer that their input isn't valid
            else:
                print("Invalid menu selection.")

            # Tell the customer they didn't select a menu option

        else:
            print("You did not select a proper menu option." )
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    while True:
        # Ask the customer if they would like to order anything else
           
        # Keep ordering
        keep_ordering = input(f"\nWould you like to keep ordering? (Y)es or (N)o ")
#5  Match/case is used to manage the customer's response
        match keep_ordering.lower():
            case 'n':
                place_order = False
                print(f"\nThank you for your order")
                break
            # Complete the order
            case 'y':
                place_order = True
                break
            case _:
                print("Invalid input. Please enter 'Y' or 'N'.")
                
# Print out the customer's order
print(f"\nThis is what we are preparing for you.\n")

print("Item name                  | Price   | Quantity")
print("---------------------------|---------|----------")

#6 Loop through the items in the customer's order
for order_item in order_list:

#7 Save the value of each key as thier own variable
    item_name = order_item["Item name"]
    price = order_item["Price"]
    quantity = order_item["Quantity"]

#8 Print the item name, price, and quantity
    print(f"{item_name:26} | ${price:6.2f} | {quantity:8}")

#9 Formatting string to seperate the detail from the subtotal
print("------------------------------------------------")   

#10 Calculate the cost of the order using list comprehension
    # Multiply the price by quantity for each item in the order list, then sum()
    # and print the prices.

total_cost = sum(float(order_item["Price"]) * int(order_item["Quantity"]) for order_item in order_list)
print(f"\nTotal cost: ${total_cost:,.2f}\n")

