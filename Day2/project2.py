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


add_contact()
view_contacts()
search_contact()
save_contacts()
load_contacts()