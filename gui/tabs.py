import tkinter as tk
from tkinter import filedialog, messagebox

def create_tabs(notebook):
    upload_tab = tk.Frame(notebook)
    notebook.add(upload_tab, text="Upload Dataset")

    label = tk.Label(upload_tab, text="Upload IoT Dataset", font=("Arial", 14))
    label.pack(pady=20)

    def upload_file():
        filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

    btn = tk.Button(upload_tab, text="Upload CSV", command=upload_file)
    btn.pack()
