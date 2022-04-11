from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
CANV_FONT = ('Arial', 18, 'italic')


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

    # CREATE WINDOW
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

    # CREATE SCORE LABEL
        self.game_score = 0
        self.label = Label(self.window, text=f"Score: {self.game_score}", fg="white", bg=THEME_COLOR)
        self.label.grid(column=1, row=0)

    # CREATE CANVAS
        self.canvas = Canvas(self.window, bg="white", width=300, height=250)
        self.canv_text = self.canvas.create_text(
                                                 150, 125,
                                                 text="Here is where question will appear",
                                                 font=CANV_FONT,
                                                 width=260,
                                                 fill=THEME_COLOR
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

    # CREATE TRUE/FALSE BUTTONS
        # Get Images
        false_img = PhotoImage(file="images/false.png")
        true_img = PhotoImage(file="images/true.png")
        # Create buttons, setting image, and placing them on grid
        self.false_btn = Button(self.window, image=false_img, borderwidth=0, command=self.pressed_false)
        self.false_btn.grid(column=1, row=2)
        self.true_btn = Button(self.window, image=true_img, borderwidth=0, command=self.pressed_true)
        self.true_btn.grid(column=0, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canv_text, text=q_text)
        else:
            self.canvas.itemconfig(self.canv_text, text="You've reached the end of the quiz.")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def pressed_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def pressed_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
