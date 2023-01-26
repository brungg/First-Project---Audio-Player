from tkinter import *
from tkinter import ttk

import AudioControls as ac

class Bar:
    def __init__(self, frame, songLength):
        self.frame = frame
        self.songLength = songLength
        self.var = 0

        self.label = ttk.Label(self.frame, text=0)
        self.label.grid(column=3, row=0, sticky=W)

        self.bar = ttk.Progressbar(self.frame, orient=HORIZONTAL, maximum=self.songLength, mode='determinate', length=200)
        self.bar.grid(column=0, row=0, columnspan=3, sticky=(W,E))

    def start(self):
        self.var += 1
        self.bar['value'] = self.var
        self.label['text'] = self.var
        if self.bar['value'] >= self.songLength:
            print("done")
            ac.__stop__()
            return
        self.frame.after(1000, self.start)
