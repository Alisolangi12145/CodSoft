import tkinter as tk
import random
import string

# A list to store generated passwords
saved_passwords = []

def generate_password():
    password_length = int(password_length_entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))
    password_display_label.config(text=password)
    message_label.config(text="Your password has been generated.")
    saved_passwords.append(password)

def save_password():
    if saved_passwords:
        saved_password = saved_passwords[-1]  # Get the last saved password
        saved_password_label.config(text="Last Saved Password:\n" + saved_password)
    else:
        saved_password_label.config(text="No saved passwords yet.")

def refresh_screen():
    password_length_entry.delete(0, "end")  # Clear the password length entry
    password_display_label.config(text="")  # Clear the displayed password
    message_label.config(text="")  # Clear the message

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Set the window size
window_width = 400
window_height = 350  # Increased height to accommodate saved password display
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f'{window_width}x{window_height}+{x}+{y}')

# Create a frame to center the elements
frame = tk.Frame(root)
frame.pack(expand=True)

# Create a label for the heading
heading_label = tk.Label(frame, text="Password Generator", font=("Helvetica", 20))
heading_label.pack(pady=10)

# Create and place a label and an entry for password length
password_length_label = tk.Label(frame, text="Password Length:")
password_length_label.pack(pady=5)
password_length_entry = tk.Entry(frame)
password_length_entry.pack(pady=5)

# Create a button to generate the password
generate_button = tk.Button(frame, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Create a button to save the password
save_button = tk.Button(frame, text="Save Password", command=save_password)
save_button.pack(pady=5)

# Create a button to refresh the screen
refresh_button = tk.Button(frame, text="Refresh Screen", command=refresh_screen)
refresh_button.pack(pady=10)

# Create a label to display the generated password
password_display_label = tk.Label(frame, text="", font=("Helvetica", 14))
password_display_label.pack(pady=10)

# Create a label for the message
message_label = tk.Label(frame, text="")
message_label.pack(pady=5)

# Create a label for the saved password display
saved_password_label = tk.Label(frame, text="Last Saved Password:\n")
saved_password_label.pack(pady=10)

# Start the main GUI loop
root.mainloop()
