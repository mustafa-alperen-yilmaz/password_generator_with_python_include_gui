import tkinter as tk
from password_generator import generate_password_with_option

def generate_button_clicked():
    option = option_var.get()
    length = int(length_entry.get())

    password = generate_password_with_option(option, length)
    password_label.configure(text="Your password is: " + password)

window = tk.Tk()
window.title("Password Generator")

option_var = tk.IntVar()
length_entry = tk.Entry(window, width=5)
generate_button = tk.Button(window, text="Generate Password", command=generate_button_clicked)
password_label = tk.Label(window, text="Please choose an option and enter a password length.")

option_frame = tk.Frame(window)
tk.Label(option_frame, text="Password Option:").pack(side=tk.LEFT)
tk.Radiobutton(option_frame, text="Small characters only", variable=option_var, value=1).pack(side=tk.LEFT)
tk.Radiobutton(option_frame, text="Big characters only", variable=option_var, value=2).pack(side=tk.LEFT)
tk.Radiobutton(option_frame, text="Small, big, and special characters", variable=option_var, value=3).pack(side=tk.LEFT)
tk.Radiobutton(option_frame, text="Small characters and numbers", variable=option_var, value=4).pack(side=tk.LEFT)
tk.Radiobutton(option_frame, text="Big characters and numbers", variable=option_var, value=5).pack(side=tk.LEFT)
tk.Radiobutton(option_frame, text="Small, big characters, and numbers", variable=option_var, value=6).pack(side=tk.LEFT)
tk.Radiobutton(option_frame, text="Small characters, numbers, and special characters", variable=option_var, value=7).pack(side=tk.LEFT)
tk.Radiobutton(option_frame, text="Big characters, numbers, and special characters", variable=option_var, value=8).pack(side=tk.LEFT)
tk.Radiobutton(option_frame, text="Small, big characters, numbers, and special characters", variable=option_var, value=9).pack(side=tk.LEFT)
option_frame.pack()

length_frame = tk.Frame(window)
tk.Label(length_frame, text="Password Length:").pack(side=tk.LEFT)
length_entry.pack(side=tk.LEFT)
length_frame.pack()

generate_button.pack(pady=10)
password_label.pack