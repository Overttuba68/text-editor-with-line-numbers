import tkinter as tk
from tkinter import messagebox

class TextEditorWithLineNumbers(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Text Editor with Line Numbers")
        self.geometry("700x400")

        # Create the top frame for the Jump to Line section
        self.top_frame = tk.Frame(self)
        self.top_frame.pack(fill=tk.X, pady=10)  # Add padding to bring it up

        # "Jump to Line" section
        self.jump_label = tk.Label(self.top_frame, text="Jump to Line:")
        self.jump_label.pack(side=tk.LEFT, padx=10)

        self.line_entry = tk.Entry(self.top_frame)
        self.line_entry.pack(side=tk.LEFT, padx=5)

        self.jump_button = tk.Button(self.top_frame, text="Jump", command=self.jump_to_line)
        self.jump_button.pack(side=tk.LEFT, padx=5)

        # Creating a frame to hold the editor and line numbers
        self.frame = tk.Frame(self)
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Line numbers (Listbox for line numbers)
        self.line_numbers = tk.Listbox(self.frame, width=5, bg="#f4f4f4", height=20, font=("Courier", 10))
        self.line_numbers.pack(side=tk.LEFT, fill=tk.Y)

        # Text editor (Text widget for content)
        self.text_editor = tk.Text(self.frame, wrap=tk.WORD, font=("Courier", 10), undo=True)
        self.text_editor.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Adding scrollbar for the text editor
        self.scrollbar = tk.Scrollbar(self.text_editor, command=self.text_editor.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_editor.config(yscrollcommand=self.scrollbar.set)

        # Bind the content change and scrolling events
        self.text_editor.bind('<KeyRelease>', self.update_line_numbers)
        self.text_editor.bind('<Configure>', self.update_line_numbers)
        self.text_editor.bind('<MouseWheel>', self.update_line_numbers)

        # Initially populate the line numbers
        self.update_line_numbers()

        # Define highlight tag
        self.text_editor.tag_configure("highlight", background="yellow")

    def update_line_numbers(self, event=None):
        """Update the line numbers when content changes or scrolling occurs."""
        lines = self.text_editor.get(1.0, tk.END).splitlines()
        self.line_numbers.delete(0, tk.END)

        for i in range(1, len(lines) + 1):
            self.line_numbers.insert(tk.END, str(i))

    def jump_to_line(self):
        """Highlight the specified line when 'Jump' button is pressed."""
        try:
            line_number = int(self.line_entry.get())
            if line_number < 1:
                raise ValueError("Line number should be greater than 0.")
                
            # Get the total number of lines
            lines = self.text_editor.get(1.0, tk.END).splitlines()

            if line_number > len(lines):
                messagebox.showerror("Invalid Line", f"Line {line_number} exceeds total lines.")
            else:
                # Remove any previous highlights
                self.text_editor.tag_remove("highlight", 1.0, tk.END)

                # Move the cursor to the given line and highlight it
                line_start = f"{line_number}.0"
                line_end = f"{line_number}.end"

                # Add the highlight tag to the specific line
                self.text_editor.tag_add("highlight", line_start, line_end)
                self.text_editor.mark_set("insert", line_start)  # Move the cursor
                self.text_editor.see(line_start)  # Scroll to the line
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid line number.")

if __name__ == "__main__":
    app = TextEditorWithLineNumbers()
    app.mainloop()
