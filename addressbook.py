# Address Book

import json

contacts = []

def main_menu():
    print("Address Book")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Exit")

def save_contacts():
    with open("contacts.txt", "w") as file:
        json.dump(contacts, file)
    print("Contacts saved successfully!")

def load_contacts():
    try:
        with open("contacts.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    
    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    
    contacts.append(contact)
    save_contacts()
    print(f"Contact {name} added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. {contact['name']} - {contact['phone']} - {contact['email']}")

def update_contact():
    if not contacts:
        print("No contacts found.")
        return
    
    view_contacts()
    try:
        contact_index = int(input("Enter the number of the contact you want to update: ")) - 1
        
        if 0 <= contact_index < len(contacts):
            print("What would you like to update?")
            print("1. Name")
            print("2. Phone")
            print("3. Email")
            choice = input("Choose an option: ")

            if choice == "1":
                new_name = input("Enter new name: ")
                contacts[contact_index]["name"] = new_name
            elif choice == "2":
                new_phone = input("Enter new phone number: ")
                contacts[contact_index]["phone"] = new_phone
            elif choice == "3":
                new_email = input("Enter new email: ")
                contacts[contact_index]["email"] = new_email
            else:
                print("Invalid choice.")
            
            save_contacts()
            print("Contact updated successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_contact():
    if not contacts:
        print("No contacts found.")
        return
    
    view_contacts()
    try:
        contact_index = int(input("Enter the number of the contact you want to delete: ")) - 1
        
        if 0 <= contact_index < len(contacts):
            deleted_contact = contacts.pop(contact_index)
            save_contacts()
            print(f"Contact {deleted_contact['name']} deleted successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    global contacts
    contacts = load_contacts()
    
    while True:
        main_menu()
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

