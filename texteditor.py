import tkinter as tk
from tkinter import filedialog

def new_file():
    text.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text.get(1.0, tk.END))

# Create the main window
window = tk.Tk()
window.title("Text Editor")

# Create a text widget
text = tk.Text(window)
text.pack()

# Create a menu bar
menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

# File menu
file_menu = tk.Menu(menu_bar)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)

window.mainloop()
