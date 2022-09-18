from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = ("Arial", 18, "italic")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizller")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text=f"Score: 0", font=("Arial", 16, "bold"), fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=350, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(175, 125, width=300, text="Question", font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, border=0, command=self.get_true_answer)
        self.true_button.grid(row=2, column=0)
        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, border=0, command=self.get_false_answer)
        self.false_button.grid(row=2, column=1)

        self.timer = self.window.after(1, self.get_next_question)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def get_true_answer(self):
        # self.window.after_cancel()
        self.give_feedback(self.quiz.check_answer("true"))

    def get_false_answer(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_right):
        self.window.after_cancel(self.timer)
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.timer = self.window.after(1000, self.get_next_question)
