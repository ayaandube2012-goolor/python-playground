from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', "'", '"', '|', '/', '.', ':', ';', '^', '=', '?', '@', '[', ']',
               '{', '}', '_', '-']

    nr_letters = random.randint(10, 15)
    nr_symbols = random.randint(3, 6)
    nr_numbers = random.randint(3, 7)

    password_list = []

    for char in range(nr_letters):
      password_list.append(random.choice(letters))

    for char in range(nr_symbols):
      password_list += random.choice(symbols)

    for char in range(nr_numbers):
      password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char

    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_to_file():


    new_data = {
        website_input.get(): {
            "Email/Username": email_or_username_input.get(),
            "Password": password_input.get()
        }
    }

    if len(website_input.get()) == 0 or len(password_input.get()) == 0 or len(email_or_username_input.get()) == 0:
        messagebox.showerror(title="ERROR", message="Please do not leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_input.get(), message=f"Here are the details: "
                                                                  f"\nEmail/Username: {email_or_username_input.get()} "
                                                                  f"\nPassword: {password_input.get()} "
                                                                  f"\nIs it ok to save?")

        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)

            website_input.delete(0, END)
            password_input.delete(0, END)
            email_or_username_input.delete(0, END)
            email_or_username_input.insert(0, "ayaandube2012@gmail.com")

# ---------------------------- WEBSITE SEARCH ------------------------------- #

def data_search():
    website = website_input.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
        user_website = data[website]
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="You currently have no data inputted, please add an account first")
    except KeyError:
        messagebox.showerror(title="Error", message="Sorry, this website does not seem to have a username or password. "
                                                     "\nPlease check if you have made any typos")
    else:
        pyperclip.copy(user_website["Password"])
        messagebox.showinfo(title=website, message=f"Password: {user_website["Password"]} "
                                                   f"\nEmail/Username: {user_website["Email/Username"]}")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("MyPass")
window.config(pady=50, padx=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", bg="white")
website_label.grid(row=1, column=0)

email_or_username_label = Label(text="Email/Username:", bg="white")
email_or_username_label.grid(row=2, column=0)

password_label = Label(text="Password", bg="white")
password_label.grid(row=3, column=0)

website_input = Entry(width=21, highlightthickness=2, highlightbackground="#000000", borderwidth=0)
website_input.focus()
website_input.grid(row=1, column=1, sticky="NSEW", padx=5, pady=5)

email_or_username_input = Entry(width=35, highlightthickness=2, highlightbackground="#000000", borderwidth=0)
email_or_username_input.insert(0, "ayaandube2012@gmail.com")
email_or_username_input.grid(row=2, column=1, columnspan=2, sticky="NSEW", padx=5, pady=5)

password_input = Entry(width=21, highlightthickness=2, highlightbackground="#000000", borderwidth=0)
password_input.grid(row=3, column=1, sticky="NSEW", padx=5, pady=5)

add_button = Button(text="Add", width=10, bg="red", fg="white", highlightthickness=0, command=save_to_file)
add_button.grid(row=4, column=1, columnspan=2, sticky="NSEW", padx=5, pady=5)

generate_password_button = Button(text="Generate Password", bg="red", fg="white", highlightthickness=0, command=generate_password)
generate_password_button.grid(row=3, column=2, sticky="NSEW", padx=5, pady=5)

search_button = Button(text="Search", bg="red", fg="white", highlightthickness=0, command=data_search)
search_button.grid(row=1, column=2, sticky="NSEW", padx=5, pady=5)

window.mainloop()
