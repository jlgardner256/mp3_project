from tkinter import *

THEME_COLOR = 'BLACK'


class Mp3_Ui:

    def __init__(self):
        self.window = Tk()
        self.window.title('Mp3_player')

        self.window = Tk()
        self.window.title('Quizzle')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text="Score: 0", fg='white', bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text='some stuff',
            fill='black',
            font=('arial', 20, 'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.true_image = PhotoImage(file='images/true.png')
        self.true_button = Button(image=self.true_image, highlightthickness=0, command=self.agree)
        self.true_button.grid(row=2, column=0)

        self.false_image = PhotoImage(file='images/false.png')
        self.false_button = Button(image=self.false_image, highlightthickness=0, command=self.disagree_button)
        self.false_button.grid(row=2, column=1)

        self.window.mainloop()
