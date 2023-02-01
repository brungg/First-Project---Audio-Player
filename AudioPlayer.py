from tkinter import *
from tkinter import ttk
import AudioControls as ac
import OpenFile as of
import ProgressBar as pb

root = Tk()
root.title("Audio")

frame = ttk.Frame(root, padding="5 5 15 15")
frame.grid(column=0, row=0, sticky=(N,S,E,W))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

songLength = 10

fileName = []

bar = None

def __getFile__():
    global fileName
    f = of.getFile()
    fileName.append(f)
    i = f.split("/")
    box.insert(box.size(), i[-1][:-4])
def play():
    global bar
    bar = pb.Bar(frame, ac.__length__(fileName[box.index(box.curselection())]), fileName[box.index(box.curselection())])
    bar.start()
    ac.__play__(fileName[box.index(box.curselection())])
def pause():
    bar.stop()
    ac.__pause__()
def unpause():
    bar.restart()
    bar.start()
    ac.__unpause__()
def stop():
    bar.stop()
    bar.reset()
    ac.__stop__()
def delete():
    box.delete(box.index(box.curselection()))
    fileName.pop(box.index(box.curselection()))
def moveup():
    global fileName
    f = fileName[box.index(box.curselection())]
    fileName.pop(box.index(box.curselection()))
    fileName.insert(box.index(box.curselection()) - 1, f)
    print(fileName)
    box.delete(box.index(box.curselection()))
    i = f.split("/")
    box.insert(fileName.index(f), i[-1][:-4])
def movedown():
    global fileName
    f = fileName[box.index(box.curselection())]
    fileName.pop(box.index(box.curselection()))
    fileName.insert(box.index(box.curselection()) + 1, f)
    print(fileName)
    box.delete(box.index(box.curselection()))
    i = f.split("/")
    box.insert(fileName.index(f), i[-1][:-4])

def buttons(txt, cmd, c, r): ttk.Button(frame, text=txt, command=cmd).grid(column=c, row=r, sticky=(W, E))

box = Listbox(frame)
box.grid(column=4, columnspan=3, row=0)

def main(): 
    buttons("start", play, 1, 1)
    buttons("pause", pause, 2, 1)
    buttons("unpause", unpause, 3, 1)
    buttons("stop/reset", stop, 4, 1)
    buttons("delete", delete, 1, 2)
    buttons("↑", moveup, 2, 2)
    buttons("↓", movedown, 2, 3)

    buttons("open file", __getFile__, 0, 1)

    root.mainloop()

if __name__ == "__main__":
    main()
