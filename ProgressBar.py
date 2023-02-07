from tkinter import *
from tkinter import ttk

import math

import AudioControls as ac

class Bar:
    def __init__(self, frame, sl, fn):
        self.frame = frame
        self.songLength = sl
        self.fileName = fn
        self.var = 0

        self.loop = None

        self.check = True

        self.label = ttk.Label(self.frame, text=0)
        self.label.grid(column=4, row=0, sticky=W)

        self.bar = ttk.Progressbar(self.frame, orient=HORIZONTAL, maximum=self.songLength, mode='determinate', length=200)
        self.bar.grid(column=0, row=0, columnspan=4, sticky=(W,E))

    def start(self):
        if self.check:
            self.label['text'] = self.timer(self.var)
            self.var += 1
            self.bar['value'] = self.var
            if self.bar['value'] >= self.songLength:
                print("done")
                ac.__stop__()
                return
            self.loop = self.frame.after(1000, self.start)

    def stop(self):
        if self.loop is not None:
            self.bar['value'] = self.var
            self.label['text'] = self.timer(self.var)
            self.frame.after_cancel(self.loop)
            self.loop = None
            self.check = False

    def restart(self): 
        self.check = True
        
    def reset(self):
        self.var = 0
        self.bar['value'] = self.var
        self.label['text'] = self.var
        self.check = False

    def timer(self, time):
        minutes = time / 60
        dec = round(minutes, 2) - math.floor(minutes)
        seconds = dec * 60
        if seconds < 10:
            return f"{math.floor(minutes)}:0{round(seconds)}"
        return f"{math.floor(minutes)}:{round(seconds)}"
