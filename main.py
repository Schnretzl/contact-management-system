import os, functions

contacts = {'123-456-7890': {'name': 'Alice', 'email': 'alice@example.com', 'address': '123 Main Street'},
            '234-567-8901': {'name': 'Bob', 'email': 'bob@example.com', 'address': '234 Elm Street'}}
while True:
    try:
        print("Welcome to the Contact Management System!")
        print("Menu:")
        print("1. Add a new contact")
        print("2. Edit an existing contact")
        print("3. Delete a contact")
        print("4. Search for a contact")
        print("5. Display all contacts")
        print("6. Export all contacts to a text file")
        print("7. Quit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            functions.add_contact(contacts)
        elif choice == 2:
            functions.edit_contact(contacts)
        elif choice == 3:
            functions.delete_contact(contacts)
        elif choice == 4:
            functions.search_contact(contacts)
        elif choice == 5:
            functions.display_contacts(contacts)
        elif choice == 6:
            functions.export_contacts(contacts)
        elif choice == 7:
            print("Thank you for using the Contact Management System!")
            break
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid input. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")