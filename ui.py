from tkinter import *
from quiz_brain import QuizBrain
import time
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        # Access the quiz brain
        self.quiz = quiz_brain
        # Create the main window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        # Create a score counter
        self.score_counter = 0
        self.score_label = Label(text=f"Score: {self.score_counter}")
        self.score_label.config(bg=THEME_COLOR, font=("Arial", 12, "bold"), fg="white")
        # Create the canvas
        self.canvas = Canvas()
        self.canvas.config(height=250, width=300, bg="white")
        # Create the question text placement
        self.question_text = self.canvas.create_text(150, 125, text="", font=("Arial", 18, "italic"), width=290)
        # Create the true and false buttons with images
        true_button_img = PhotoImage(file="images/true.png")
        false_button_img = PhotoImage(file="images/false.png")
        self.true_button = Button(
            image=true_button_img,
            command=self.answer_true,
            highlightthickness=0
        )
        self.false_button = Button(
            image=false_button_img,
            command=self.answer_false,
            highlightthickness=0
        )
        self.true_button.config(padx=20, pady=20)
        self.false_button.config(padx=20, pady=20)
        # Align all items in the grid
        self.score_label.grid(column=1, row=0, sticky='n')
        self.canvas.grid(pady=50, column=0, row=1, columnspan=2)
        self.true_button.grid(column=0, row=2, sticky="w")
        self.false_button.grid(column=1, row=2, sticky="e")
        # Call get next question method to print out the first question text on init
        self.get_next_question()
        # Call the window main loop
        self.window.mainloop()
        
    def answer_true(self):
        self.give_feedback(self.quiz.check_answer(user_answer="True"))

    def answer_false(self):
        self.give_feedback(self.quiz.check_answer(user_answer="False"))

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
        else:
            q_text = (f"You have answered all the questions!  "
                      f"Your final score is: {self.score_counter}/{len(self.quiz.question_list)}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
        self.canvas.itemconfig(self.question_text, text=q_text)

    def give_feedback(self, is_right):

        if is_right:
            self.canvas.config(bg="green")
            self.score_counter += 1
            self.score_label.config(text=f"Score: {self.score_counter}")
        else:
            self.canvas.config(bg="red")
        self.canvas.after(1000, func=self.get_next_question)




