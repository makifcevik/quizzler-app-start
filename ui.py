from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
QUESTION_FONT = ("Arial", 14, "normal")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quız App")
        self.window.config(padx=50, pady=20, background=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, borderwidth=0)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.item_text = self.canvas.create_text(150, 125, text="", width=280, font=QUESTION_FONT)

        self.label_score = Label(text="Score: 0", font=FONT, bg=THEME_COLOR, fg="White")
        self.label_score.grid(row=0, column=1)

        img_true = PhotoImage(file="./images/true.png")
        img_false = PhotoImage(file="./images/false.png")

        self.button_false = Button(image=img_false, command=self.false_pressed)
        self.button_false.config(borderwidth=0)
        self.button_false.grid(row=2, column=0)

        self.button_true = Button(image=img_true, command=self.true_pressed)
        self.button_true.config(borderwidth=0)
        self.button_true.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="White")
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.item_text, text=self.quiz.next_question())
            self.update_score()
        else:
            self.canvas.itemconfig(self.item_text, text="You've reached the end of the quiz!")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="Green")
        else:
            self.canvas.config(bg="Red")
        self.window.after(1000, self.get_next_question)

    def update_score(self):
        score = self.quiz.score
        self.label_score.config(text=f"Score: {score}")
