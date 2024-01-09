# Importing all the necessary libraries
import numpy.random
from gtts import gTTS
from tkinter import *
import pygame

# Initializing the pygame library
pygame.init()


# This function plays the sound in the file audio.mp3
def play():
    sound = pygame.mixer.Sound('audio.mp3')
    sound.play()
    pygame.time.wait(int(sound.get_length() * 1000))


# This function picks a random line from the insults.txt file
def pick_a_swear():
    try:
        with open('insults.txt', 'r') as file:
            insults = file.read().split(',')
            speaker = gTTS(text=insults[numpy.random.randint(0, len(insults))], lang='en', slow=False)
            speaker.save('audio.mp3')
        play()
    except FileNotFoundError as f:
        with open('insults.txt', 'w') as file:
            file.write("Heya bozo don't forget to write the insults in this file before running the code.")
    pick_a_swear()


root = Tk()  # Initialize the tkinter window
root.geometry('500x500')  # Sets the window's dimensions
frame = Frame(root)  # Sets up a frame for our button to be in
frame.pack(pady=50)
button = Button(frame, text='Press to get swore at', height=50, width=50, bg='red', command=pick_a_swear)  # Creates the button
button.pack(side=BOTTOM, pady=100)

root.mainloop()  # Calls the main loop of the window
