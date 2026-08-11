# Shabnam Khan
import tkinter as tk
from tkinter import messagebox

# Main window
# Light pink background
root = tk.Tk()
root.title("Login Page")
root.geometry("800x600")
root.configure(bg="#FFD9E6")

# Functions
def submit_login():
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if username == "":
        messagebox.showerror("Error", "Please enter your username.")
    elif password == "":
        messagebox.showerror("Error", "Please enter your password.")
    else:
        messagebox.showinfo("Login Successful", f"Welcome, {username}!")

def go_back():
    messagebox.showinfo("Back", "Going back to the previous page.")

def exit_program():
    root.destroy()

# Pressing Enter will submit
root.bind("<Return>", lambda event: submit_login())

# Heading
heading = tk.Label(
    root,
    text="Welcome Screen",
    font=("Liberation Serif", 35),
    bg="#FFD9E6",
    fg="black"
)
heading.place(x=255, y=40)

# Username label
username_label = tk.Label(
    root,
    text="Username:",
    font=("Liberation Serif", 29),
    bg="#FFD9E6",
    fg="black"
)
username_label.place(x=120, y=170)

# Username entry
username_entry = tk.Entry(
    root,
    font=("Liberation Serif", 23),
    width=22,
    bd=3
)
username_entry.place(x=320, y=175)

# Password label
password_label = tk.Label(
    root,
    text="Password:",
    font=("Liberation Serif", 29),
    bg="#FFD9E6",
    fg="black"
)
password_label.place(x=120, y=280)

# Password entry
password_entry = tk.Entry(
    root,
    font=("Liberation Serif", 23),
    width=22,
    bd=3,
    show="*"
)
password_entry.place(x=320, y=285)

# Buttons
back_button = tk.Button(
    root,
    text="Back",
    font=("Liberation Serif", 23),
    bg="white",
    fg="black",
    width=10,
    command=go_back
)
back_button.place(x=90, y=470)

submit_button = tk.Button(
    root,
    text="Submit",
    font=("Liberation Serif", 23),
    bg="white",
    fg="black",
    width=10,
    command=submit_login
)
submit_button.place(x=325, y=470)

exit_button = tk.Button(
    root,
    text="Exit",
    font=("Liberation Serif", 23),
    bg="white",
    fg="black",
    width=10,
    command=exit_program
)
exit_button.place(x=570, y=470)

root.mainloop()
