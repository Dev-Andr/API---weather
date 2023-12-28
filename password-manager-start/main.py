import pyperclip, random, json
from tkinter import *
from tkinter import messagebox

path = "data.json"


def gen():
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
             'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '!', '@', '#', '$', '%', '^', '&', '*',
             '(', ')', ',', '.', '"', "'", '/', '?', ';', ':', '[', ']', '{', '}', '|', '>', '<', '+', '_', '-',
             '=', '~', '`', ' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    p = ''.join(random.choice(chars) for _ in range(1, 12))
    pyperclip.copy(p)
    e_pwd.insert(0, p)


def save():
    if e_website.get() == "" or e_pwd.get() == "" or e_mail.get() == "":
        messagebox.showwarning(title="Oops!", message="You left out some fields!")
        return
    if not messagebox.askokcancel(title="IMP", message="Do you want to proceed?"):
        return
    val = {e_website.get():
        {
            "mail": e_mail.get(),
            "pwd": e_pwd.get()
        }
    }

    try:
        with open(path, 'r') as f:
            d = json.load(f)
            d.update(val)
    except FileNotFoundError:
        print("Creating new file")
        d = val

    with open(path, 'w') as f:
        json.dump(d, f, indent=4)

    e_website.delete(0, END)
    e_mail.delete(0, END)
    e_pwd.delete(0, END)


def sea():
    if e_website.get() == "":
        messagebox.showwarning(title="Oops!", message="Enter the website address!")
        return
    try:
        with open(path, 'r') as f:
            try:
                d = json.load(f)[e_website.get()]
                messagebox.showinfo(title="Search Result",message=f"Email: {d['mail']}\nPassword: {d['pwd']}")
            except KeyError:
                messagebox.showwarning(title="Error", message="Website not in our database")
    except FileNotFoundError:
        messagebox.showwarning(title="Error",message="No entry yet!")


window = Tk()
window.title("PwdMgr")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

l_website = Label(text="Website:")
l_website.grid(column=0, row=1, sticky="w")
l_mail = Label(text="Email/Username:")
l_mail.grid(column=0, row=2, sticky="w")
l_pwd = Label(text="Password:")
l_pwd.grid(column=0, row=3, sticky="w")

e_website = Entry(width=35)
e_website.grid(column=1, row=1, sticky="e")
e_website.focus()
e_mail = Entry(width=60)
e_mail.grid(column=1, row=2, columnspan=2, sticky="e")
e_mail.insert(0, "abcd@gmail.com")
e_pwd = Entry(width=35)
e_pwd.grid(column=1, row=3, sticky="e")

b_sea = Button(text="Search", width=20, command=sea)
b_sea.grid(column=2, row=1, sticky="w")
b_gen = Button(text="Generate Password", width=20, command=gen)
b_gen.grid(column=2, row=3, sticky="w")
b_add = Button(text="Add", width=51, command=save)
b_add.grid(column=1, row=4, columnspan=2, sticky="w")

window.mainloop()
