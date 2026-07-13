import json


def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


contacts = load_contacts()


def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    print("Contact added successfully!")


def view_contacts():
    if len(contacts) == 0:
        print("No contacts found.")
    else:
        for contact in contacts:
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print("--------------------")


def search_contact():
    search_name = input("Enter name to search: ")

    for contact in contacts:
        if contact["name"].lower() == search_name.lower():
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            return

    print("Contact not found.")


def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)

    print("Contacts saved successfully!")


while True:
    print("\nContact Book Menu")
    print("1. Add contact")
    print("2. View contacts")
    print("3. Search contact")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        save_contacts()
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose 1, 2, 3, or 4.")