import tkinter as tk
from tkinter import filedialog, messagebox

class TextEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Editor")
        self.current_file = None

        # Frame for buttons and file name
        top_frame = tk.Frame(root)
        top_frame.pack(side=tk.TOP, fill=tk.X)

        # File name label
        self.file_label = tk.Label(top_frame, text="No file selected", anchor="w")
        self.file_label.pack(side=tk.TOP, fill=tk.X, padx=5, pady=2)

        # Buttons
        button_frame = tk.Frame(top_frame)
        button_frame.pack(side=tk.TOP, fill=tk.X)

        self.open_button = tk.Button(button_frame, text="Open", command=self.open_file)
        self.open_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.save_button = tk.Button(button_frame, text="Save", command=self.save_file)
        self.save_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Text box
        self.textbox = tk.Text(root, wrap="word")
        self.textbox.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)

    def update_title(self, filepath):
        self.current_file = filepath
        self.file_label.config(text=f"Current file: {filepath}")

    def save_file(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt")]
        )
        if file_path:
            try:
                with open(file_path, "w", encoding="utf-8") as file:
                    content = self.textbox.get("1.0", tk.END)
                    file.write(content)
                self.update_title(file_path)
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file: {e}")

    def open_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt")]
        )
        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()
                    self.textbox.delete("1.0", tk.END)
                    self.textbox.insert(tk.END, content)
                self.update_title(file_path)
            except Exception as e:
                messagebox.showerror("Error", f"Could not open file: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditorApp(root)
    root.geometry("600x400")
    root.mainloop()
