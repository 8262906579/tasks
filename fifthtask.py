import json

# File to store contacts
CONTACTS_FILE = 'contacts.json'

# Load existing contacts from the file
def load_contacts():
    try:
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save contacts to the file
def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact(contacts):
    name = input("Enter the contact's name: ")
    phone_number = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email: ")
    address = input("Enter the contact's address: ")
    
    contact = {
        'name': name,
        'phone_number': phone_number,
        'email': email,
        'address': address
    }
    
    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added successfully!")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    for idx, contact in enumerate(contacts, 1):
        print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone_number']}")

# Search for a contact by name or phone number
def search_contact(contacts):
    search_term = input("Enter the name or phone number to search: ").lower()
    results = [contact for contact in contacts if search_term in contact['name'].lower() or search_term in contact['phone_number']]
    
    if not results:
        print("No contacts found.")
        return
    
    for contact in results:
        print(f"Name: {contact['name']}, Phone: {contact['phone_number']}, Email: {contact['email']}, Address: {contact['address']}")

# Update an existing contact's details
def update_contact(contacts):
    view_contacts(contacts)
    try:
        contact_number = int(input("Enter the number of the contact you want to update: "))
        if 1 <= contact_number <= len(contacts):
            contact = contacts[contact_number - 1]
            print(f"Updating contact: {contact['name']}")
            contact['name'] = input(f"Enter new name (current: {contact['name']}): ") or contact['name']
            contact['phone_number'] = input(f"Enter new phone number (current: {contact['phone_number']}): ") or contact['phone_number']
            contact['email'] = input(f"Enter new email (current: {contact['email']}): ") or contact['email']
            contact['address'] = input(f"Enter new address (current: {contact['address']}): ") or contact['address']
            save_contacts(contacts)
            print("Contact updated successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")

# Delete a contact
def delete_contact(contacts):
    view_contacts(contacts)
    try:
        contact_number = int(input("Enter the number of the contact you want to delete: "))
        if 1 <= contact_number <= len(contacts):
            contact = contacts.pop(contact_number - 1)
            save_contacts(contacts)
            print(f"Contact {contact['name']} deleted successfully.")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")

# Main menu
def main():
    contacts = load_contacts()
    
    while True:
        print("\nContact Information Manager")
        print("1. View contact list")
        print("2. Add a new contact")
        print("3. Search for a contact")
        print("4. Update a contact")
        print("5. Delete a contact")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ")
        
        if choice == '1':
            view_contacts(contacts)
        elif choice == '2':
            add_contact(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid option, please choose again.")

# Run the program
if __name__ == "__main__":
    main()
