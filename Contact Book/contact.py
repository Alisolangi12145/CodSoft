import tkinter as tk
from tkinter import messagebox

# Create a dictionary to store contacts
contacts = {}

# Function to add a new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        contacts[name] = {
            "Phone": phone,
            "Email": email,
            "Address": address
        }
        update_contact_list()
        display_contact_details(name)
        clear_entries()
    else:
        messagebox.showerror("Error", "Name and Phone are required fields.")

# Function to update the contact list
def update_contact_list():
    contact_list.delete(0, tk.END)
    for name, details in contacts.items():
        contact_list.insert(tk.END, f"{name}: {details['Phone']}")

# Function to display contact details
def display_contact_details(name):
    details = contacts.get(name)
    if details:
        details_text.delete(1.0, tk.END)
        details_text.insert(tk.END, f"Name: {name}\n")
        details_text.insert(tk.END, f"Phone: {details['Phone']}\n")
        details_text.insert(tk.END, f"Email: {details['Email']}\n")
        details_text.insert(tk.END, f"Address: {details['Address']}")

# Function to search for a contact
def search_contact():
    search_term = search_entry.get()
    contact_list.delete(0, tk.END)
    for name, details in contacts.items():
        if search_term in name or search_term in details["Phone"]:
            contact_list.insert(tk.END, f"{name}: {details['Phone']}")

# Function to update a contact
def update_selected_contact():
    selected_contact = contact_list.get(contact_list.curselection())
    name = selected_contact.split(":")[0]
    new_phone = new_phone_entry.get()

    if name in contacts and new_phone:
        contacts[name]["Phone"] = new_phone
        update_contact_list()
        display_contact_details(name)
        new_phone_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Please select a contact and provide a new phone number.")

# Function to delete a contact
def delete_selected_contact():
    selected_contact = contact_list.get(contact_list.curselection())
    name = selected_contact.split(":")[0]

    if name in contacts:
        del contacts[name]
        update_contact_list()
        details_text.delete(1.0, tk.END)  # Clear the details text when a contact is deleted

# Function to clear the input fields
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Function to handle contact selection in the listbox
def select_contact(event):
    selected_contact = contact_list.get(contact_list.curselection())
    name = selected_contact.split(":")[0]
    display_contact_details(name)

# Create the main window
root = tk.Tk()
root.title("Contact Book")

# Create input fields
name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

phone_label = tk.Label(root, text="Phone:")
phone_label.pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

email_label = tk.Label(root, text="Email:")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

address_label = tk.Label(root, text="Address:")
address_label.pack()
address_entry = tk.Entry(root)
address_entry.pack()

# Create buttons
add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.pack()

search_label = tk.Label(root, text="Search:")
search_label.pack()
search_entry = tk.Entry(root)
search_entry.pack()
search_button = tk.Button(root, text="Search", command=search_contact)
search_button.pack()

update_label = tk.Label(root, text="New Phone:")
update_label.pack()
new_phone_entry = tk.Entry(root)
new_phone_entry.pack()
update_button = tk.Button(root, text="Update Contact", command=update_selected_contact)
update_button.pack()

delete_button = tk.Button(root, text="Delete Contact", command=delete_selected_contact)
delete_button.pack()

# Create the contact list
contact_list = tk.Listbox(root)
contact_list.pack()
# Bind the listbox selection event to the select_contact function
contact_list.bind('<<ListboxSelect>>', select_contact)

# Create a text widget to display contact details
details_text = tk.Text(root, height=6, width=30)
details_text.pack()

# Start the main loop
update_contact_list()
root.mainloop()
