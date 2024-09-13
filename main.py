import os, functions

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
            functions.add_contact()
        elif choice == 2:
            functions.edit_contact()
        elif choice == 3:
            functions.delete_contact()
        elif choice == 4:
            functions.search_contact()
        elif choice == 5:
            functions.display_contacts()
        elif choice == 6:
            functions.export_contacts()
        elif choice == 7:
            print("Thank you for using the Contact Management System!")
            break
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid input. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")