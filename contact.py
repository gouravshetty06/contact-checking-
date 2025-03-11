import json
CONTACTS_FILE = "contacts.json"
def load_contacts():
    
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
def save_contacts(contacts):
  
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)
def add_contact(contacts, name, phone, email):
    
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
def view_contacts(contacts):
   
    if not contacts:
        print("No contacts found.")
        return
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
def search_contact(contacts, search_term):
    found_contacts = [contact for contact in contacts if search_term.lower() in contact['name'].lower()]
    if not found_contacts:
        print("No contacts found.")
    else:
        for i, contact in enumerate(found_contacts, start=1):
            print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
def delete_contact(contacts, search_term):
    
    for contact in contacts:
        if search_term.lower() in contact['name'].lower():
            contacts.remove(contact)
            save_contacts(contacts)
            print(f"Deleted contact: {contact['name']}")
            return

    print("No contacts found.")


def main():
    contacts = load_contacts()

    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. View Contacts")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            add_contact(contacts, name, phone, email)
        elif choice == '2':
            search_term = input("Enter name to search: ")
            search_contact(contacts, search_term)
        elif choice == '3':
            view_contacts(contacts)
        elif choice == '4':
            search_term = input("Enter name to delete: ")
            delete_contact(contacts, search_term)
        elif choice == '5':
            break
        else:
            print("error")


if __name__ == "__main__":
    main()
