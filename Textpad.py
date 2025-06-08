import tkinter as tk
from tkinter import filedialog

def save_file():
    text_content = text_box.get("1.0", tk.END)
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_content)

root = tk.Tk()
root.title("Text Saver")

text_box = tk.Text(root, height=10, width=40)
text_box.pack()

save_button = tk.Button(root, text="Save", command=save_file)
save_button.pack()

root.mainloop()