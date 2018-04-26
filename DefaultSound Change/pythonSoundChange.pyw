import sounddevice as sd
import os
import sys
import tkinter as tk

def headphones():
    os.system("C:/Users/Wayne/Desktop/DeafultSpeakerChange/setToHeadphones.Bat")
    root.iconify()

def speakers():
    os.system("C:/Users/Wayne/Desktop/DeafultSpeakerChange/changeToSpeakers.Bat")
    root.iconify()
    
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

speak = tk.Button(frame, 
                   text="Headhpones", 
                   command=headphones)
speak.pack(side=tk.LEFT)

head = tk.Button(frame,
                   text="Speakers",
                   command=speakers)
head.pack(side=tk.RIGHT)

stop =  tk.Button(frame,
                   text="Stop",
                   command=quit)
stop.pack(side=tk.RIGHT)

#root.iconify()

root.mainloop()
