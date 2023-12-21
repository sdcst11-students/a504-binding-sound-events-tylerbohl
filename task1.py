#Create a sound board. This is a collection of buttons that is each bound to a sound effect. 
# These are great ways to help teach little children the different sounds that animals make, 
# especially if you can add an image of the animal to the button.

import tkinter as tk
import playsound 

win = tk.Tk()

yeah = tk.Button(win, text = "YEAH!!!")
fligigu = tk.Button(win, text = "Fligigu")
bell = tk.Button(win, text = "For Whom the Bell Tolls")
hour = tk.Button(win, text = "One Hour")
twist = tk.Button(win, text = "unrapenduprapebu!!!!!!")
weezer = tk.Button(win, text = "Wonderwall")
chicken = tk.Button(win, text = "chicken")

def Yeah(event):
    playsound.playsound("yeah.mp3",block=False)
def Fligigu(event):
    playsound.playsound("fligugigu.mp3",block=False)
def Bell(event):
    playsound.playsound("bell.mp3",block=False)
def Hour(event):
    playsound.playsound("onehourlater.mp3",block=False)
def Twist(event):
    playsound.playsound("twist.mp3",block=False)
def Weezer(event):
    playsound.playsound("weezer.mp3",block=False)
def Chicken(event):
    playsound.playsound("chicken.mp3",block=False)

yeah.bind("<Button>",Yeah)
fligigu.bind("<Button>",Fligigu)
bell.bind("<Button>",Bell)
hour.bind("<Button>",Hour)
twist.bind("<Button>",Twist)
weezer.bind("<Button>",Weezer)
chicken.bind("<Button>",Chicken)

yeah.pack()
fligigu.pack()
bell.pack()
hour.pack()
twist.pack()
weezer.pack()
chicken.pack()

win.mainloop()