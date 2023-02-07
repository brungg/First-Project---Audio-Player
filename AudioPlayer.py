from tkinter import *
from tkinter import ttk, messagebox
import AudioControls as ac
import OpenFile as of
import ProgressBar as pb

root = Tk()
root.title("DotiPY")

frame = ttk.Frame(root, padding="5 5 15 15")
frame.grid(column=0, row=0, sticky=(N,S,E,W))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

songLength = 0
fileName = []
bar = None
currentSong = 0
box = None
isPlaying = False

def __getFile__():
    global fileName, box
    try:
        fileName.append(of.getFile())
        i = fileName[-1].split("/")
        box.insert(box.size(), i[-1][:-4])
    except Exception:
        messagebox.showerror("Warning", "Please selected a file")
    
def play_pause():
    global bar, currentSong, isPlaying
    try:
        if not fileName[box.index(box.curselection())] == currentSong and not isPlaying:
            bar = pb.Bar(frame, ac.__length__(fileName[box.index(box.curselection())]), fileName[box.index(box.curselection())])
            currentSong = box.index(box.curselection())
            bar.start()
            ac.__play__(fileName[box.index(box.curselection())])
            isPlaying = True
        elif isPlaying:
            bar.stop()
            ac.__pause__()
            isPlaying = False
        else:
            bar.restart()
            bar.start()
            ac.__unpause__()
            isPlaying = True
    except Exception:
            messagebox.showerror("Warning", "Please selected a file")

def skip_song_fwd():
    global bar, currentSong, isPlaying
    currentSong += 1
    try:
        bar = pb.Bar(frame, ac.__length__(fileName[currentSong]), fileName[currentSong])
        bar.start()
        ac.__play__(fileName[currentSong])
        isPlaying = True
    except Exception:
        currentSong -= 1
        messagebox.showerror("Warning", "Last file in queue")

def skip_song_bwd():
    global bar, currentSong, isPlaying
    currentSong -= 1
    try:
        bar = pb.Bar(frame, ac.__length__(fileName[currentSong]), fileName[currentSong])
        bar.start()
        ac.__play__(fileName[currentSong])
        isPlaying = True
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
        if box.index(box.curselection()) == 0:
            return
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

def buttons(txt, cmd, c, r, x, s): ttk.Button(frame, text=txt, width=x, command=cmd).grid(column=c, columnspan=s, row=r, sticky=(W, E))

box = Listbox(frame)
box.grid(column=5, columnspan=3, row=0)

def main(): 
    buttons("play/pause", play_pause, 1, 3, 10, 1)
    buttons("delete", delete, 7, 3, 6, 1)
    buttons("|<", skip_song_bwd, 0, 3, 2, 1)
    buttons(">|", skip_song_fwd, 2, 3, 2, 1)
    buttons("↑", moveup, 6, 1, 1, 1)
    buttons("↓", movedown, 5, 1, 1, 1)

    buttons("open file", __getFile__, 7, 1, 9, 1)

    root.mainloop()

if __name__ == "__main__":
    main()
