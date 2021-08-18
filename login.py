from tkinter import *
import os
import sys
from PIL import Image, ImageTk
# Designing window for registration
from tkinter import Toplevel


def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("444x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    register_screen.resizable(0, 0)
    register_screen.load = Image.open("C:\\Users\\Manav\\Downloads\\MP\\MP-1\\pic.jpg")
    register_screen.render = ImageTk.PhotoImage(register_screen.load)
    l = Label(register_screen, image=login_screen.render)
    l.place(x=0, y=0)

    Label(register_screen, text="Please enter details below" , bg="#21c393").pack()
    #Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ", bg="#21c393")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ", bg="#24958b")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    #Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, command=register_user, bg="#245692").pack()


# Designing window for login

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("444x250")
    Label(login_screen, text="Please enter details below to login").pack()
    #Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    login_screen.resizable(0, 0)
    login_screen.load = Image.open("C:\\Users\\Manav\\Downloads\\MP\\MP-1\\pic.jpg")
    login_screen.render = ImageTk.PhotoImage(login_screen.load)
    l = Label(login_screen, image=login_screen.render)
    l.place(x=0, y=0)

    Label(login_screen, text="Username * ", bg="#21c393").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    #Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ", bg="#24958b").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    #Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify, bg="#245692").pack()


# Implementing event on register button

def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()


# Implementing event on login button

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()


# Designing popup for login success

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()


# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()


# Designing popup for user not found

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


# Deleting popups

def delete_login_success():
    login_success_screen.destroy()
    login_screen.destroy()
    main_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()
    sys.exit()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()
    sys.exit()


def exit_system():
    sys.exit()


# Designing Main(first) window

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("444x250")
    main_screen.title("Account Login")

    main_screen.resizable(0, 0)
    main_screen.load = Image.open("C:\\Users\\Manav\\Downloads\\MP\\MP-1\\pic.jpg")
    main_screen.render = ImageTk.PhotoImage(main_screen.load)
    l = Label(main_screen, image=main_screen.render)
    l.place(x=0, y=0)

    Label(text="Select Your Choice", bg="#21c393", width="300", height="2", font=("Calibri", 13)).pack()
    #Label(text="", bg="#21c393").pack()
    Button(text="Login", height="2", width="30", command=login, bg="#21c393").pack()
    #Label(text="", bg="#2c8c8e").pack()
    Button(text="Register", height="2", width="30", command=register, bg="#2d6190").pack()
    #Label(text="", bg="#245692").pack()
    Button(text="Quit", height="1", width="10", command=exit_system, bg="#245692").pack()
    main_screen.mainloop()


main_account_screen()
