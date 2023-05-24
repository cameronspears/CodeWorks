# CodeWorks.py
import tkinter as tk
from tkinter import messagebox

from CodeCleanup import CodeCleanup
from CodeClipboard import CodeClipboard


class CodeWorks:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("CodeWorks")

        self.code_cleanup = CodeCleanup(self.root)
        self.code_clipboard = CodeClipboard(self.root)

        self.cleanup_button = tk.Button(
            self.root, text="Code Cleanup", command=self.run_cleanup
        )
        self.clipboard_button = tk.Button(
            self.root, text="Code Clipboard", command=self.run_clipboard
        )

        self.cleanup_button.pack(pady=10)
        self.clipboard_button.pack(pady=10)

    def run_cleanup(self):
        try:
            self.code_cleanup.cleanup_directory()
            messagebox.showinfo("Success", "Code cleanup completed successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def run_clipboard(self):
        try:
            self.code_clipboard.copy_project_to_clipboard()
            messagebox.showinfo("Success", "Project copied to clipboard successfully.")
        # Assistant should continue the previous message
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    CodeWorks().run()
