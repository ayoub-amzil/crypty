import tkinter as tk
from tkinter import filedialog

def select_file():
    file_path = filedialog.askopenfilename()
    # Update the label with the selected file path
    file_label.config(text=file_path)
    # Do something with the file_path, like encrypting it with PyCryptodome

root = tk.Tk()
root.title("File Encryption App")

# Set the window size to 400x400 pixels and disable resizing
root.geometry("400x400")
root.resizable(False, False)

# Create a label to display the selected file path
file_label = tk.Label(root, text="")
file_label.pack()

# Create a button that calls the select_file function when clicked
select_button = tk.Button(root, text="Select File", command=select_file)
select_button.pack()

root.mainloop()
