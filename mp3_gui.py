from tkinter import *
from pygame import mixer
from tkinter import filedialog
from PIL import Image, ImageTk

THEME_COLOR = 'WHITE'


class Mp3Face:

    def __init__(self):
        self.window = Tk()
        self.window.title('Mp3 music player')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.title = Label(text='My music player', bg='white')
        self.title.grid(row=0, column=3, )

        # create menu
        self.my_menu = Menu(self.window)
        self.window.config(menu=self.my_menu)

        #add song to the Menu
        self.add_music = Menu(self.my_menu)
        self.my_menu.add_cascade(label='Add Songs', menu=self.add_music)
        self.add_music.add_command(label='Add song to playist')


        # black screen
        self.music_box = Listbox(self.window, bg='black', fg='white', width=60)
        self.music_box.grid(row=2, column=2, columnspan=3, )

        # button Widget
        self.button_widget = Frame(self.window)
        self.button_widget.grid(column=3)

        # Pause button
        self.pause_image = Image.open('pause_button1.png')
        self.resize_pause = self.pause_image.resize((25, 25))
        self.formatted_pause_image = ImageTk.PhotoImage(self.resize_pause)
        self.pause_button = Button(self.button_widget, image=self.formatted_pause_image)
        self.pause_button.grid(row=3, column=2, padx=10, pady=10)

        # play button
        self.play_image = Image.open('play_button.png')
        self.resize_play = self.play_image.resize((25, 25))
        self.formatted_play_image = ImageTk.PhotoImage(self.resize_play)
        self.play_button = Button(self.button_widget, image=self.formatted_play_image)
        self.play_button.grid(row=3, column=3, padx=10, pady=10)

        # next button
        self.next_image = Image.open('next_button.png')
        self.resize_next = self.next_image.resize((25, 25))
        self.formatted_next_image = ImageTk.PhotoImage(self.resize_next)
        self.next_button = Button(self.button_widget, image=self.formatted_next_image)
        self.next_button.grid(row=3, column=4, padx=10, pady=10)

        # back button
        self.back_image = Image.open('back_button.png')
        self.resize_back = self.back_image.resize((25, 25))
        self.formatted_back_image = ImageTk.PhotoImage(self.resize_back)
        self.back_button = Button(self.button_widget, image=self.formatted_back_image)
        self.back_button.grid(row=3, column=1, padx=10, pady=10)

        self.window.mainloop()

    def add_song(self):
    # music = self.add_music.add_command(label="add a song to the playlist", command=add)
     pass
