"""
Contact Management System: A contact management system is a project that
helps users manage their contacts.
The system uses Python lists to store the contacts and
their details such as name, phone number, and email address.
"""
contacts = []

while True:
    print("1. Add contact")
    print("2. Update contact")
    print("3. Remove contact")
    print("4. View all contacts")
    print("5. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        email = input("Enter email: ")
        contacts.append({'name': name, 'phone_number': phone_number, 'email': email})
        print("Contact added successfully!")
    elif choice == "2":
        name = input("Enter name of contact to update: ")
        for contact in contacts:
            if contact['name'] == name:
                contact['phone_number'] = input("Enter new phone number: ")
                contact['email'] = input("Enter new email: ")
                print("Contact updated successfully!")
                break
        else:
            print("Contact not found!")
    elif choice == "3":
        name = input("Enter name of contact to remove: ")
        for contact in contacts:
            if contact['name'] == name:
                contacts.remove(contact)
                print("Contact removed successfully!")
                break
        else:
            print("Contact not found!")
    elif choice == "4":
        print("All contacts:")
        for contact in contacts:
            print("Name:", contact['name'])
            print("Phone number:", contact['phone_number'])
            print("Email:", contact['email'])
            print()
    elif choice == "5":
        break
    else:
        print("Invalid choice!")

