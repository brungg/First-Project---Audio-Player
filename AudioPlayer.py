from tkinter import *
from tkinter import ttk
import AudioControls as ac
import OpenFile as f

root = Tk();
root.title("Audio")

frame = ttk.Frame(root, padding="5 5 15 15")
frame.grid(column=0, row=0, sticky=(N,S,E,W))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

songLength = 15

fileName = ""

def __getFile__():
    global fileName
    fileName = f.getFile()

def buttons(txt, cmd, c, r): ttk.Button(frame, text=txt, command=cmd).grid(column=c, row=r, sticky=(W, E))
# bar = ProgressBar.Bar(root, songLength)
def main():
    buttons("start", lambda: ac.__play__(fileName), 1, 1)
    buttons("pause", ac.__pause__, 2, 1)
    buttons("unpause", ac.__unpause__, 3, 1)
    buttons("stop", ac.__stop__, 4, 1)

    buttons("open file", __getFile__, 0, 1)

    root.mainloop()

if __name__ == "__main__":
    main()