while True:
    items = []
    print("------------------Welcome To ICARUS--------------------------")
    print("1. View Items \n2. Add Items for sale \n3. Purchase Items \n4. Search Items \n5. Edit Items \n6. Exit")
    choice = int(input("Enter a number to specify what you would like to do at ICARUS supermarket: "))
    if choice == 1:
        print("-----------View Items-------------")
        print("The number of items available is : {}".format(len(items)))
        if len(items) != 0:
            print("        Here are all the items available at ICARUS     ")
            for item in items:
                for key, value in item.items():
                    print("{}, {}".format(key, value))
    elif choice == 2:
        print("-----------Add Items for sale------------")
        print("Give me the details of your item")
        item = {}
        item["name"] = input("Item name : ")
        while True:
            try:
                item["quantity"] = int(input("Quantity of Item: "))
                break
            except ValueError :
                print("Quantity should be a number ")
        while True:
            try:
                item["price"] = int(input("Price of item in £: "))
                break
            except ValueError:
                print("Price should be a number")
        print("Your Item has been succesfully added")
        items.append(item)
    elif choice == 3:
        print("--------------Purchase Items---------------")
        print(items)
        purchase_item_name = input("Enter the name of the item you want to purchase: ")
        purchase_item_quantity = int(input("How much of this item do you want?: "))
        for item in items:
            if purchase_item_name.lower() == item["name"].lower():
                if item["quantity"] != 0:
                    if purchase_item_quantity <= item["quantity"]:
                        print("pay {} at checkout counter".format(item["price"] * purchase_item_quantity))
                        item["quantity"] -= purchase_item_quantity
                    else: 
                        print("The quantity you have asked for is not available")
                else: 
                    print("Item out of stock")
    elif choice == 4:
        print("--------------Search Items---------------")
        search = input("Give me the name of the item you want to search for: ")
        for item in items:
            if search.lower() == item["name"].lower():
                print("The details of the item named {} is displayed below".format(search))
                print(item)
            else:
                print("item named {} not found".format(search))
    elif choice == 5:
        print("--------------Update Items---------------")
        target_item = input("Enter the name of the item you wish to edit: ")
        for item in items:
            if target_item.lower() == item["name"].lower():
                print("here are the current details of {} :".format(target_item))
                print(item)
                print("Enter your new details")
                item["name"] = input("Enter the new name of the item: ")
                while True:
                    try:
                        item["quantity"] = int(input("Enter the new quantity of the Item: "))
                        break
                    except ValueError :
                        print("Quantity should be a number ")
                while True:
                    try:
                        item["price"] = int(input("Enter the new price of the item in £: "))
                        break
                    except ValueError:
                        print("Price should be a number")
                    print("Your Item has been succesfully updated")
                    print(item) 
                else: 
                    print("Item not found")
    elif choice == 6:
            print("--------------App Closed---------------")
            break
    else:
        print("You entered an invalid option")
        print("Try entering one of the options listed below")







    
