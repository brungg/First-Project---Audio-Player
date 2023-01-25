from tkinter import *
from tkinter import ttk
import time

class Bar:
    def __init__(self, frame, songLength):
        self.songLength = songLength
        self.var = DoubleVar()

        value_label = ttk.Label(frame, text=0)
        value_label.grid(column=2, row=0, sticky=(W,E))

        def progress(var):
            value_label['text'] = int(round(float(var)))
            time.sleep(1)
            print(value_label['text'])
            #self.bar[]

        self.bar = ttk.Scale(frame, orient=HORIZONTAL, length=200, from_=0, to=songLength, variable=self.var, command=progress)
        self.bar.grid(column=0, row=0, columnspan=2, sticky=(W,E))
