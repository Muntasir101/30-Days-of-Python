"""
Inventory Management System: An inventory management system is a project that
helps businesses manage their inventory.
The system uses Python lists to store the items in the inventory,
their quantities, and prices.
"""
inventory = []

while True:
    print("1. Add item to inventory")
    print("2. Update item in inventory")
    print("3. Remove item from inventory")
    print("4. View inventory")
    print("5. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        inventory.append([item, quantity, price])
        print("Item added to inventory successfully!")
    elif choice == "2":
        item = input("Enter item name: ")
        for i, inv_item in enumerate(inventory):
            if inv_item[0] == item:
                quantity = int(input("Enter new quantity: "))
                price = float(input("Enter new price: "))
                inventory[i] = [item, quantity, price]
                print("Item updated successfully!")
                break
        else:
            print("Item not found!")
    elif choice == "3":
        item = input("Enter item name: ")
        for inv_item in inventory:
            if inv_item[0] == item:
                inventory.remove(inv_item)
                print("Item removed from inventory successfully!")
                break
        else:
            print("Item not found!")
    elif choice == "4":
        print("Inventory:")
        print("{:<20} {:<10} {:<10}".format("Item", "Quantity", "Price"))
        for item, quantity, price in inventory:
            print("{:<20} {:<10} {:<10}".format(item, quantity, price))
    elif choice == "5":
        break
    else:
        print("Invalid choice!")
