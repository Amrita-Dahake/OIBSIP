import random
import string
from tkinter import *

# Window
window = Tk()
window.title("OASIS PASSWORD GENERATOR")
window.geometry('1000x500')
window.config(bg="#f3e9dd")

# Heading
label1 = Label(window, text="Enter Password Length:",
               font='Times 18 bold',
               bg="#f3e9dd",
               fg="#6b4f3f")
label1.pack(pady=20)

# Entry box
entry = Entry(window, font='Times 16',
              bg="#fff8ef",
              fg="#5a3d2b",
              relief="flat",
              justify='center')
entry.pack(ipady=5)

# Result label
result_label = Label(window, text="",
                     font='Times 18 bold',
                     bg="#f3e9dd",
                     fg="#4a3b2a")
result_label.pack(pady=30)

# Global variable to store password
generated_password = ""

# Function to generate password
def generate_password():
    global generated_password
    n = int(entry.get())

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*(){}[]?<>/"

    all_chars = lower + upper + digits + symbols
    generated_password = ""

    for i in range(n):
        generated_password += random.choice(all_chars)

    result_label.config(text="Generated Password: " + generated_password)

# Function to copy password
def copy_password():
    window.clipboard_clear()
    window.clipboard_append(generated_password)

    # Temporary message to show "Copied!"
    result_label.config(text="Copied to Clipboard ✔️")

# Generate Button
btn = Button(window, text="Generate Password",
             font='Times 16 bold',
             fg="white",
             bg="#8d6e63",
             activebackground="#a1887f",
             relief="flat",
             padx=20, pady=10,
             command=generate_password)
btn.pack(pady=10)

# Copy Button
copy_btn = Button(window, text="Copy to Clipboard",
                  font='Times 16 bold',
                  fg="white",
                  bg="#6b4f3f",
                  activebackground="#8d6e63",
                  relief="flat",
                  padx=20, pady=10,
                  command=copy_password)
copy_btn.pack(pady=10)

window.mainloop()
