from tkinter import *
import requests


def get_quote():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(qT,text=quote)


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
canvas.grid(padx=50, pady=50, row=0, column=0)

img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=img)
qT = canvas.create_text(150,207,text="Kanye Quote Goes Here",width=250,font = ("Ariel",30,"bold"))

kanye = PhotoImage(file="kanye.png")
kB = Button(image=kanye, highlightthickness=0,command=get_quote)
kB.grid(column=0, row=1)

window.mainloop()
