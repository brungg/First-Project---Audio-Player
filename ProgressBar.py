from tkinter import *
from tkinter import ttk

class Bar:
    def __init__(self, frame, songLength):
        self.frame = frame
        self.songLength = songLength
        self.var = 0

        self.bar = ttk.Progressbar(self.frame, orient=HORIZONTAL, mode='determinate', length=200)
        self.bar.grid(column=0, row=0, columnspan=2, sticky=(W,E))

    def start(self):
        self.var += 1
        self.bar['value'] = self.var
        if self.bar['value'] >= self.songLength:

            print("done")
            # Here you can do anything when the  progress bar finishes.

            return  # This will end the after() loop
        self.frame.after(1000, self.start)
