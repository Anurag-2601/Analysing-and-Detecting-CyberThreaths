import tkinter as tk
from tkinter import ttk
from gui.tabs import create_tabs

def run_app():
    root = tk.Tk()
    root.title("Cyber Attack Detection System")
    root.geometry("900x600")

    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True)

    create_tabs(notebook)

    root.mainloop()

if __name__ == "__main__":
    run_app()

