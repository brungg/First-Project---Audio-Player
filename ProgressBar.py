from tkinter import ttk

class Bar:
    def __init__(self, root, songLength):
        self.songLength = songLength

        self.bar = ttk.Progressbar(root, orient='horizontal', mode='determinate', length=280)
        self.bar.grid(column=3, row=0, columnspan=2)

        self.value_label = ttk.Label(root, text=self.update_progress_label())
        self.value_label.grid(column=0, row=1, columnspan=2)

    def update_progress_label(self):
        return f"Current Progress: {self.bar['value']}%"

    def progress(self):
        if self.bar['value'] < self.songLength:
            self.bar['value'] += 1
            self.value_label['text'] = self.update_progress_label()
            print(self.value_label['text'])

    def stop(self):
        self.bar.stop()
        self.value_label['text'] = self.update_progress_label()
        self.timer.stop()