from tkinter import *
from tkinter import messagebox
import string
import random
import os
import pyperclip
password_result = str

# ------------------------FUNCTION-----------------------------


def get_website_name():
    web_name = website_text_input.get()
    print(web_name)


def get_website_username():
    web_username = username_text_input.get()
    print(web_username)


def generate_user_password():
    alphabets = list(string.ascii_letters)
    digits = list(string.digits)
    special_characters = list("!@#$%^&*()")

    letters = []
    numbers = []
    spec = []
    chosen_alphabets_len = random.randint(5, 8)
    chosen_number_len = random.randint(2, 4)
    chosen_spec_char_len = random.randint(2, 4)

    for i in range(chosen_alphabets_len):
        letters.append(random.choice(alphabets))

    for i in range(chosen_number_len):
        numbers.append(random.choice(digits))

    for i in range(chosen_spec_char_len):
        spec.append(random.choice(special_characters))

    password = letters+numbers+spec
    random.shuffle(password)
    global password_result
    password_result = "".join(password)

    pyperclip.copy(password_result)
    return password_result


def get_password():
    password_text_input.delete(0, END)
    password = generate_user_password()
    password_text_input.insert(0, f"{password}")


def save_data_to_txt():

    if website_text_input.get() == "" or password_text_input.get() == "":
        messagebox.showwarning(title="Warning", message="Ups, make sure there is no blank data")
    else:
        ask_user = messagebox.askokcancel(message=f"Do you want to add ?\n" f"Web : {website_text_input.get()}\n"
                                                  f"Username : {username_text_input.get()}\n"
                                                  f"Password : {password_text_input.get()}\n",
                                          title=website_text_input.get())

        if ask_user:
            with open("my_password.txt", mode="a") as file:
                file.write(f"Web Name : {website_text_input.get()}, "
                           f"Username : {username_text_input.get()},"
                           f"Password : {password_text_input.get()}\n")

    website_text_input.delete(0, END)
    password_text_input.delete(0, END)


def open_txt_file():
    save_data_to_txt()
    os.open("my_password.txt", os.O_RDWR)


# -------------------------SETUP UI----------------------------

# window
window = Tk()
window.title("Password Manager")
window.configure(bg="white")
window.config(padx=100, pady=100)

# image canvas
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=0, columnspan=4)

# website label and website textinput
website_label = Label(text="Website     : ", bg="white", highlightthickness=0)
website_label.grid(row=1, column=0)

website_text_input = Entry(width=35, bg="yellow")
website_text_input.grid(row=1, column=1, columnspan=3)

# username label and username textinput
username_label = Label(text="Username  : ", bg="white", highlightthickness=0)
username_label.grid(row=2, column=0)

username_text_input = Entry(width=35, bg="yellow")
username_text_input.insert(END, "adiftawisnu818@gmail.com")
username_text_input.grid(row=2, column=1, columnspan=3, pady=5)

# password label, password textinput, generate password button
password_label = Label(text="Password   : ", bg="white")
password_label.grid(row=3, column=0)

password_text_input = Entry(bg="yellow", width=25)
password_text_input.grid(row=3, column=2, columnspan=1)

generate_password_button = Button(text="Generate", width=7, height=1, command=get_password)
generate_password_button.grid(row=3, column=3, pady=5)

# add button
add_button = Button(text="add", width=29, pady=5, command=open_txt_file)
add_button.grid(row=4, column=1, columnspan=3)

window.mainloop()
