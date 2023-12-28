from tkinter import *
from quiz_brain import QuizBrain

clr = "#375362"


class Interface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=clr)

        self.score = Label(text="Score: 0", fg="white", bg=clr)
        self.score.grid(row=0, column=1, sticky='e')

        self.canvas = Canvas(width=300, height=300, bg=clr)
        self.q = self.canvas.create_text(
            150,
            150,
            width=250,
            text="Questino",
            fill="white",
            font=("Times New Roman", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        img_cross = PhotoImage(file="images/false.png").subsample(2)
        img_tick = PhotoImage(file="images/true.png").subsample(2)
        self.cross = Button(width=50, height=50, image=img_cross, highlightthickness=0, bg=clr, command=self.Tick)
        self.tick = Button(width=50, height=50, image=img_tick, highlightthickness=0, bg=clr, command=self.Cross)
        self.cross.grid(row=2, column=0)
        self.tick.grid(row=2, column=1)

        self.getNext()
        self.window.mainloop()

    def getNext(self):
        txt = self.quiz.nextQ()
        self.canvas.itemconfig(self.q, text=txt)

    def Tick(self):
        self.effect(self.quiz.check("False"))

    def Cross(self):
        self.effect(self.quiz.check("False"))

    def effect(self, rg):
        self.score.config(text=f"Score: {self.quiz.score}/{self.quiz.qNo}")
        self.canvas.config(bg=rg)
        self.window.after(100, self.reset)

    def reset(self):
        self.canvas.config(bg=clr)

        if self.quiz.stillQ():
            self.getNext()
        else:
            self.canvas.itemconfig(self.q, text=f"Quiz Over!\n{self.score.cget('text')}")
            self.tick.config(state="disabled")
            self.cross.config(state="disabled")
