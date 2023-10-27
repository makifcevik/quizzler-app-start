from tkinter import *

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quız App")
        self.window.config(padx=50, pady=20, background=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.label_score = Label(text="Score: 0", font=FONT, bg=THEME_COLOR, fg="White")
        self.label_score.grid(row=0, column=1, sticky="EW")

        img_true = PhotoImage(file="./images/true.png")
        img_false = PhotoImage(file="./images/false.png")

        self.button_false = Button(image=img_false)
        self.button_false.config(borderwidth=0)
        self.button_false.grid(row=2, column=0)

        self.button_true = Button(image=img_true)
        self.button_true.config(borderwidth=0)
        self.button_true.grid(row=2, column=1)

        self.window.mainloop()


test = QuizInterface()
