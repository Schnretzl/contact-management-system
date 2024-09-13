import re

def add_contact(contacts):
    phone = get_valid_phone()
    if phone in contacts.keys():
        print('This contact has already been added.')
        return
    name = get_valid_name()
    email = get_valid_email()
    address = get_valid_address()
    contacts[phone] = {'name': name, 'email': email, 'address': address}

def edit_contact(contacts):
    phone = get_valid_phone('Please enter the phone number of the contact you want to edit: ')
    if phone not in contacts.keys():
        print('This contact does not exist.')
        return
    print('What info would you like edit?')
    print('1. Name')
    print('2. Email')
    print('3. Address')
    try:
        choice = int(input())
        if choice == 1:
            contacts[phone]['name'] = get_valid_name('Enter new name: ')
        elif choice == 2:
            contacts[phone]['email'] = get_valid_email('Enter new email: ')
        elif choice == 3:
            contacts[phone]['address'] = get_valid_address('Enter new address: ')
        else:
            print('Invalid choice.')
    except ValueError:
        print('Invalid input.')
    except Exception as e:
        print(f'An error occurred: {e}')

def delete_contact(contacts):
    phone = get_valid_phone('Please enter the phone number of the contact you want to delete: ')
    if phone not in contacts.keys():
        print('This contact does not exist.')
        return
    del contacts[phone]

def search_contact(contacts):
    found = False
    name = get_valid_name('Please enter the name of the contact you want to search for: ')
    for phone, info in contacts.items():
        if info['name'] == name:
            found = True
            break
    if not found:
        print('Name not found in contacts.')
        return
    print(f'Phone: {phone}')
    print(f'Name: {name}')
    print(f'Email: {contacts[phone]["email"]}')
    print(f'Address: {contacts[phone]["address"]}')
    print()
    
def display_contacts(contacts):
    print()
    for phone, info in contacts.items():
        print(f'Name: {info["name"]}')
        print(f'Phone: {phone}')
        print(f'Email: {info["email"]}')
        print(f'Address: {info["address"]}')
        print()

def export_contacts(contacts):
    for phone, info in contacts.items():
        with open('contacts.txt', 'a') as file:
            file.write(f'Phone: {phone}\n')
            file.write(f'Name: {info["name"]}\n')
            file.write(f'Email: {info["email"]}\n')
            file.write(f'Address: {info["address"]}\n\n')
    print('Contacts exported to contacts.txt.')
    
def import_contacts(contacts):
    try:
        with open('contacts.txt', 'r') as file:
            lines = file.readlines()
            for i in range(0, len(lines), 5):
                phone = lines[i].strip().split(': ')[1]
                if phone in contacts.keys():
                    continue
                name = lines[i + 1].strip().split(': ')[1]
                email = lines[i + 2].strip().split(': ')[1]
                address = lines[i + 3].strip().split(': ')[1]
                contacts[phone] = {'name': name, 'email': email, 'address': address}
        print('Contacts imported from contacts.txt.')
    except FileNotFoundError:
        print('contacts.txt not found.')
    except Exception as e:
        print(f'An error occurred: {e}')
            
################################################################

# Validation functions
            
def get_valid_phone(prompt = 'Enter phone number: '):
    while True:
        try:
            phone = input(prompt)
            if len(phone) != 10:
                raise ValueError('Phone number must be 10 digits long.')
            if not phone.isdigit():
                raise ValueError('Phone number must contain only digits.')
            if phone[0] == '0':
                raise ValueError('Phone number cannot start with 0.')
        except ValueError as e:
            print(f'Error: {e}')
        else:
            return phone[:3] + '-' + phone[3:6] + '-' + phone[6:]
    
def get_valid_name(prompt = 'Enter name: '):
    while True:
        name = input(prompt)
        if name.isalpha():
            return name
        print('Name must contain only letters.')
        
def get_valid_email(prompt = 'Enter email: '):
    valid_pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    while True:
        email = input(prompt)
        if re.search(valid_pattern, email):
            return email
        print('Invalid email address.')
        
def get_valid_address(prompt = 'Enter address: '):
    valid_pattern = r"(^\d+(\s[a-zA-Z]+)+$)"
    while True:
        address = input(prompt)
        if re.search(valid_pattern, address):
            return address
        print('Invalid address.')