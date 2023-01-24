from tkinter import *
from tkinter import filedialog
    
def getFile():
    print("test")
    try:
        with filedialog.askopenfile('r') as f:
            filename = f.name
            if filename[-4:] == ".mp3" or ".wav" or ".m4a":
                print("works")
                return filename
    except Exception:
        print("No file selected")
