from tkinter import *
from tkinter import ttk, messagebox
import AudioControls as ac
import OpenFile as of
import ProgressBar as pb

root = Tk()
root.title("Audio")

frame = ttk.Frame(root, padding="5 5 15 15")
frame.grid(column=0, row=0, sticky=(N,S,E,W))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

songLength = 0
fileName = []
bar = None
currentSong = 0
box = None

def __getFile__():
    global fileName, box
    fileName.append(of.getFile())
    i = fileName[-1].split("/")
    box.insert(box.size(), i[-1][:-4])
def play():
    global bar, currentSong
    try:
        bar = pb.Bar(frame, ac.__length__(fileName[box.index(box.curselection())]), fileName[box.index(box.curselection())])
        currentSong = box.index(box.curselection())
        bar.start()
        ac.__play__(fileName[box.index(box.curselection())])
    except Exception:
        messagebox.showerror("Warning", "Please selected a file")
def pause():
    try:
        bar.stop()
        ac.__pause__()
    except Exception:
        messagebox.showerror("Warning", "Please selected a file")
def unpause():
    try:
        bar.restart()
        bar.start()
        ac.__unpause__()
    except Exception:
        messagebox.showerror("Warning", "Please selected a file")
def stop():
    try:
        bar.stop()
        bar.reset()
        ac.__stop__()
    except Exception:
        messagebox.showerror("Warning", "Please selected a file")
def skip_song_fwd():
    global bar, currentSong
    currentSong += 1
    try:
        bar = pb.Bar(frame, ac.__length__(fileName[currentSong]), fileName[currentSong])
        bar.start()
        ac.__play__(fileName[currentSong])
    except Exception:
        currentSong -= 1
        messagebox.showerror("Warning", "Last file in queue")
def skip_song_bwd():
    global bar, currentSong
    currentSong -= 1
    try:
        bar = pb.Bar(frame, ac.__length__(fileName[currentSong]), fileName[currentSong])
        bar.start()
        ac.__play__(fileName[currentSong])
    except Exception:
        currentSong += 1
        messagebox.showerror("Warning", "First file in queue")
def delete():
    try:
        fileName.pop(box.index(box.curselection()))
        box.delete(box.index(box.curselection()))
    except Exception:
        messagebox.showerror("Warning", "Please selected a file")
def moveup():
    global fileName
    try:
        f = fileName[box.index(box.curselection())]
        fileName.pop(box.index(box.curselection()))
        fileName.insert(box.index(box.curselection()) - 1, f)
        box.delete(box.index(box.curselection()))
        i = f.split("/")
        box.insert(fileName.index(f), i[-1][:-4])
    except Exception:
        messagebox.showerror("Warning", "Please selected a file")
def movedown():
    global fileName
    try:
        f = fileName[box.index(box.curselection())]
        fileName.pop(box.index(box.curselection()))
        fileName.insert(box.index(box.curselection()) + 1, f)
        box.delete(box.index(box.curselection()))
        i = f.split("/")
        box.insert(fileName.index(f), i[-1][:-4])
    except Exception:
        messagebox.showerror("Warning", "Please selected a file")

def buttons(txt, cmd, c, r): ttk.Button(frame, text=txt, command=cmd).grid(column=c, row=r, sticky=(W, E))

box = Listbox(frame)
box.grid(column=4, columnspan=3, row=0)

def main(): 
    buttons("start", play, 1, 1)
    buttons("pause", pause, 2, 1)
    buttons("unpause", unpause, 3, 1)
    buttons("stop/reset", stop, 4, 1)
    buttons("delete", delete, 1, 2)
    buttons(">|", skip_song_fwd, 4, 2)
    buttons("|<", skip_song_bwd, 3, 2)
    buttons("↑", moveup, 2, 2)
    buttons("↓", movedown, 2, 3)

    buttons("open file", __getFile__, 0, 1)

    root.mainloop()

if __name__ == "__main__":
    main()
