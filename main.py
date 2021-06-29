from tkinter import *
import pygame
from PIL import Image, ImageTk
from tkinter import filedialog

THEME_COLOR = 'WHITE'

window = Tk()

window.title('Mp3 music player')
window.config(padx=20, pady=20, bg=THEME_COLOR)
title = Label(text='My music player', bg='white')
title.grid(row=0, column=3, )

pygame.mixer.init()


def add_song():
    song = filedialog.askopenfilename(initialdir='C:/Users/heidi/PycharmProject/MP3/music',
                                      title='Choose A Song',
                                      filetypes=(('mp3 Files', '*.mp3'),))
    song = song.replace('C:/Users/heidi/PycharmProject/MP3/music/', "")
    song = song.replace('.mp3', '')
    music_box.insert(END, song)


def play():
    song = music_box.get(ACTIVE)
    song = f'C:/Users/heidi/PycharmProject/MP3/music/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)


def stop():
    pygame.mixer.music.stop()
    music_box.selection_clear(ACTIVE)


global paused
paused = False


def pause(is_paused):
    global paused
    paused = is_paused
    if paused:
        # unpause
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True


# next button play the next song in the playlist
def next_song():
    # will get the song tuple from the Listbox
    current_song = music_box.curselection()
    #adds 1 to
    current_song = current_song[0] + 1

    song = music_box.get(current_song)
    song = f'C:/Users/heidi/PycharmProject/MP3/music/{song}.mp3'
    #loads song from music files
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    music_box.selection_clear(0, END)
    music_box.activate(current_song)
    music_box.selection_set(current_song, last=None)
    print(song)

def back_song():
    # will get the song tuple from the Listbox
    current_song = music_box.curselection()
    #adds 1 to
    current_song = current_song[0] - 1

    song = music_box.get(current_song)
    song = f'C:/Users/heidi/PycharmProject/MP3/music/{song}.mp3'
    #loads song from music files
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    music_box.selection_clear(0, END)
    music_box.activate(current_song)
    music_box.selection_set(current_song, last=None)
    print(song)

# create menu
my_menu = Menu(window)
window.config(menu=my_menu)

# add song to the Menu
add_music = Menu(my_menu)
my_menu.add_cascade(label='Add Songs', menu=add_music)
add_music.add_command(label='Add song to playlist', command=add_song)

# black screen
music_box = Listbox(window, bg='black', fg='white', width=60, selectbackground='red')
music_box.grid(row=2, column=2, columnspan=3, )

# button Widget
button_widget = Frame(window)
button_widget.grid(column=3)

# Pause button
pause_image = Image.open('pause_button1.png')
resize_pause = pause_image.resize((25, 25))
formatted_pause_image = ImageTk.PhotoImage(resize_pause)
pause_button = Button(button_widget, image=formatted_pause_image, command=lambda: pause(paused))
pause_button.grid(row=3, column=2, padx=10, pady=10)

# play button
play_image = Image.open('play_button.png')
resize_play = play_image.resize((25, 25))
formatted_play_image = ImageTk.PhotoImage(resize_play)
play_button = Button(button_widget, image=formatted_play_image, command=play)
play_button.grid(row=3, column=3, padx=10, pady=10)
# stop button

stop_image = Image.open('stop_png.png')
resize_stop = stop_image.resize((25, 25))
formatted_stop_image = ImageTk.PhotoImage(resize_stop)
play_button = Button(button_widget, image=formatted_stop_image, command=stop)
play_button.grid(row=3, column=4, padx=10, pady=10)

# next button
next_image = Image.open('next_button.png')
resize_next = next_image.resize((25, 25))
formatted_next_image = ImageTk.PhotoImage(resize_next)
next_button = Button(button_widget, image=formatted_next_image, command=next_song)
next_button.grid(row=3, column=5, padx=10, pady=10)

# back button
back_image = Image.open('back_button.png')
resize_back = back_image.resize((25, 25))
formatted_back_image = ImageTk.PhotoImage(resize_back)
back_button = Button(button_widget, image=formatted_back_image, command=back_song)
back_button.grid(row=3, column=1, padx=10, pady=10)

window.mainloop()

# window = Mp3Face()
