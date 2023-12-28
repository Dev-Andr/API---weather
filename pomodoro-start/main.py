from tkinter import *

pink = "#e2979c"
red = "#e7305b"
green = "#9bdeac"
yellow = "#f7f5dd"
font = "Courier"
trophy = "🏆"
rep = 0
timer = None


def adjust(t):
    mint = t // 60
    sec = t % 60
    if mint < 10:
        mint = f"0{mint}"
    if sec < 10:
        sec = f"0{sec}"

    return f'{mint}:{sec}'


def setup():
    def startT():
        global rep
        l1.config(text="Work", fg=green)

        if rep != 4:
            logic(1500)
            rep += 1
        else:
            l1.config(text="Goal done")

    def breakT():
        global rep
        l1.config(text="Break", fg=pink)
        l2.config(text=trophy * rep)

        if rep != 4:
            logic(300)
        else:
            logic(1200)

    def reset():
        global rep, timer
        rep = 0
        window.after_cancel(timer)
        window.destroy()
        setup()

    def logic(count):
        global timer
        if count != -1:
            canvas.itemconfig(timerT, text=adjust(count))
            timer = window.after(1, logic, count - 1)
        else:
            if l1["text"] == "Break":
                startT()
            else:
                breakT()

    window = Tk()
    window.title("Tamatar")
    window.config(padx=25, pady=25, bg=yellow)

    canvas = Canvas(width=200, height=224, bg=yellow)

    img = PhotoImage(file='tomato.png')
    canvas.create_image(102, 112, image=img)
    timerT = canvas.create_text(100, 130, text="00:00", font=(font, 30, "bold"), fill="white")

    canvas.grid(column=1, row=1)

    l1 = Label(text="Timer", font=(font, 30, "bold"), fg=green, bg=yellow)
    l1.grid(column=1, row=0)
    l2 = Label(text="⏰", font=(font, 30, "bold"), fg="orange", bg=yellow)
    l2.grid(column=1, row=3)

    b1 = Button(text="Start", font=(font, 20, "bold"), bg=yellow, command=startT)
    b2 = Button(text="Reset", font=(font, 20, "bold"), bg=yellow, command=reset)
    b1.grid(column=0, row=2)
    b2.grid(column=2, row=2)

    window.mainloop()

setup()