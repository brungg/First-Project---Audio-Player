from tkinter import *
from tkinter import ttk
import AudioControls as ac
import OpenFile as of
import ProgressBar as pb

root = Tk();
root.title("Audio")

frame = ttk.Frame(root, padding="5 5 15 15")
frame.grid(column=0, row=0, sticky=(N,S,E,W))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

songLength = 10

fileName = ""

bar = None

def __getFile__():
    global fileName, bar
    fileName = of.getFile()

def buttons(txt, cmd, c, r): ttk.Button(frame, text=txt, command=cmd).grid(column=c, row=r, sticky=(W, E))

def play():
    global fileName, bar
    bar = pb.Bar(frame, ac.__length__(fileName), fileName)
    bar.start()
    ac.__play__(fileName)
    
def pause():
    global fileName, bar
    bar.stop()
    ac.__pause__()
    
def unpause():
    global fileName, bar
    bar.restart()
    bar.start()
    ac.__unpause__()
    
def stop():
    global fileName, bar
    bar.stop()
    bar.reset()
    ac.__stop__()

def main(): 
    buttons("start", play, 1, 1)
    buttons("pause", pause, 2, 1)
    buttons("unpause", unpause, 3, 1)
    buttons("stop/reset", stop, 4, 1)

    buttons("open file", __getFile__, 0, 1)

    root.mainloop()

if __name__ == "__main__":
    main()
