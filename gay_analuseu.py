import tkinter as tk
from tkinter import ttk
import time 


class my_app(tk.Tk):

    def __init__(self):
        super().__init__()
        self.initialyse_app()

    def initialyse_app(self):
        self.geometry("800x600")
        self.title("gay analuseu")
        self.label = tk.Label(self, text="Welcome to your gay analyse app")
        self.label.pack()
        self.analuseuh_button = tk.Button(self, text="start analuseuh",command=self.start_analuseuh)
        self.analuseuh_button.pack()
        
    def start_analuseuh(self):
        progressbar = ttk.Progressbar(self, length=400)
        progressbar.pack()
        for i in range(25):
            progressbar['value'] += 2
            self.update_idletasks()
            time.sleep(0.01)
        for i in range(20):
            progressbar['value'] += 2
            self.update_idletasks()
            time.sleep(0.1)
        for i in range(10):
            progressbar['value'] += 1
            self.update_idletasks()
            time.sleep(0.1)


app = my_app()
app.mainloop()