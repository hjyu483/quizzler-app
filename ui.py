THEME_COLOR = "#375362"

from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface():
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx = 20, pady = 20, bg = THEME_COLOR)
        self.true = PhotoImage(file = "images/true.png")
        self.false = PhotoImage(file = "images/false.png")
        self.canvas = Canvas(height = 300, width = 300, bg = 'white' )
        self.scoreboard = Label(text="Score: ", fg="white", bg=THEME_COLOR, font=("Arial", 16, "italic"))
        self.scoreboard.grid(row=0, column=1)
        self.question_text = self.canvas.create_text(150, 150, width = 280, text="dddd", font = ("Arial", 20, "italic"), fill = THEME_COLOR)
        self.canvas.grid(column = 0, row = 1, columnspan = 2, pady = 50)
        self.true_button = Button(image = self.true, command=self.check_answer)
        self.true_button.grid(column = 0, row = 2, pady = 20)
        self.false_button = Button(image = self.false, command=self.wrong_answer)
        self.false_button.grid(column=1, row=2, pady = 20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.scoreboard.config(text = f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = q_text) # This is used to configure properties of items within the canvas (like rectangles, ovals, texts, etc) rather than canvas widget itself
        else:
            self.canvas.itemconfig(self.question_text, text = "You've reached out the end of the game.")
            self.true_button.config(state = "disabled")
            self.false_button.config(state = "disabled")

    def check_answer(self):
        if self.quiz.check_answer('True'):
            self.canvas.config(bg = 'green') # Set properties of the Canvas widget itself, such as the background color, size, and other widget-level settings.
        else:
            self.canvas.config(bg = 'red')
        self.window.after(1000, self.get_next_question)

    def wrong_answer(self):
        if self.quiz.check_answer('False'):
            self.canvas.config(bg='green')  # Set properties of the Canvas widget itself, such as the background color, size, and other widget-level settings.
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
