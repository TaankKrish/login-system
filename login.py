import mysql.connector
from tkinter import *
from tkinter import ttk


window = Tk()
window.title("Login-Window")
window.configure(bg='#333333')

frame = Frame(bg='#333333')

# creating widgets
login_label = Label(frame, text = "Login", bg='#333333', fg='#76EE00', font=('cooper black',40))
admno_label = Label(frame, text = "Admisssion Number", bg='#333333', fg='#FFFFFF', font=12)
admno_entry = Entry(frame, font=12)
passwrd_label = Label(frame, text = "Password", bg='#333333', fg='#FFFFFF', font=12)
passwrd_entry = Entry(frame, show = "*", font=12)
login_button = Button(frame, text = "login",  bg='#458B00', fg='#FFFFFF', font=12)
newstd_button = ttk.Button(frame,text="Register new user")


# placing widget on screen
login_label.grid(row=0, column=0, columnspan=2, pady=40)
admno_label.grid(row=1, column=0, padx=10)
admno_entry.grid(row=1, column=1, pady=20)
passwrd_label.grid(row=2, column=0)
passwrd_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=10)
newstd_button.grid(row=4, column=0, columnspan=2, pady=20)

frame.pack(padx=50)

window.mainloop()