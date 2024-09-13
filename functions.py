def add_contact(contacts):
    phone = input('Enter phone number: ')
    if phone in contacts.keys():
        print('This contact has already been added.')
        return
    name = input('Enter name: ')
    email = input('Enter email: ')
    address = input('Enter address: ')
    contacts[phone] = {'name': name, 'email': email, 'address': address}

def edit_contact():
    pass

def delete_contact():
    pass

def search_contact():
    pass

def display_contacts():
    pass

def export_contacts():
    pass