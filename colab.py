import json
import os
from IPython.display import display, clear_output
import ipywidgets as widgets

# File to store contacts
CONTACTS_FILE = "contacts.json"

# Load contacts from the file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return {}

# Save contacts to the file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Initialize contacts
contacts = load_contacts()

# Function to display contacts
def display_contacts():
    if not contacts:
        output.clear_output()
        with output:
            print("No contacts available.")
    else:
        output.clear_output()
        with output:
            print("Contact List:")
            for name, info in contacts.items():
                print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
    clear_inputs()

# Function to add a contact
def add_contact(button):
    name = name_input.value.strip()
    phone = phone_input.value.strip()
    email = email_input.value.strip()
    if name in contacts:
        with output:
            print(f"Contact with the name '{name}' already exists.")
    else:
        contacts[name] = {"phone": phone, "email": email}
        save_contacts(contacts)
        with output:
            print(f"Contact '{name}' added successfully!")
    display_contacts()

# Function to edit a contact
def edit_contact(button):
    name = name_input.value.strip()
    if name in contacts:
        phone = phone_input.value.strip()
        email = email_input.value.strip()
        contacts[name]["phone"] = phone if phone else contacts[name]["phone"]
        contacts[name]["email"] = email if email else contacts[name]["email"]
        save_contacts(contacts)
        with output:
            print(f"Contact '{name}' updated successfully!")
    else:
        with output:
            print(f"No contact found with the name '{name}'.")
    display_contacts()

# Function to delete a contact
def delete_contact(button):
    name = name_input.value.strip()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        with output:
            print(f"Contact '{name}' deleted successfully!")
    else:
        with output:
            print(f"No contact found with the name '{name}'.")
    display_contacts()

# Clear input fields
def clear_inputs():
    name_input.value = ""
    phone_input.value = ""
    email_input.value = ""

# Widgets
name_input = widgets.Text(description="Name:", placeholder="Enter name")
phone_input = widgets.Text(description="Phone:", placeholder="Enter phone number")
email_input = widgets.Text(description="Email:", placeholder="Enter email address")

add_button = widgets.Button(description="Add Contact")
edit_button = widgets.Button(description="Edit Contact")
delete_button = widgets.Button(description="Delete Contact")
view_button = widgets.Button(description="View Contacts")

output = widgets.Output()

# Assign actions to buttons
add_button.on_click(add_contact)
edit_button.on_click(edit_contact)
delete_button.on_click(delete_contact)
view_button.on_click(lambda x: display_contacts())

# Layout
display(
    widgets.VBox([
        name_input,
        phone_input,
        email_input,
        widgets.HBox([add_button, edit_button, delete_button, view_button]),
        output
    ])
)
