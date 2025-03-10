import tkinter as tk
from tkinter import ttk



class my_app(tk.Tk):

    def __init__(self, root):
        super().__init__(*args, **kwargs)
        self.initialyse_app()

    def initialyse_app(self):
        self.title("gay analuseu")
        self.label = tk.Label(self.root, text="Welcome to your gay analyse app")
        self.label.pack()
        self.geometry("800x600")

    def start_analuseuh(self):
        progressbar = ttk.Progressbar(root, length=400)
        progressbar.start()



