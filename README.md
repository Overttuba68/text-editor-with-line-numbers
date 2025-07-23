# Text Editor with Line Numbers and "Jump to Line" Feature

A simple text editor built using Python's Tkinter library, which provides basic text editing functionality along with dynamic line numbering and a "Jump to Line" feature. This allows users to quickly navigate to a specific line in the text editor by entering the line number.

## Features:
- **Dynamic Line Numbers**: Automatically updated line numbers on the left-hand side as you type in the editor.
- **Jump to Line**: Enter a line number and click "Jump" to move to that specific line and highlight it.
- **Highlighting**: When you jump to a line, it is highlighted for easy identification.
- **Text Editing**: Standard text editing capabilities like typing, copy-pasting, and scrolling.
- **Error Handling**: Displays error messages if the user enters an invalid line number.

## Requirements:
- Python 3.x
- Tkinter (comes pre-installed with Python)

## Installation:
To run this project, clone the repository and navigate to the project folder. Then run the Python script.

1. **Clone the repository**:
    ```bash
    git clone https://github.com/overttuba68/text-editor-with-line-numbers.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd text-editor-with-line-numbers
    ```

3. **Run the Python script**:
    ```bash
    python text_editor_with_line_numbers.py
    ```

## Usage:
- **Line Numbers**: The line numbers are shown on the left side of the editor. They update dynamically as you type.
- **Jump to Line**: Enter a line number in the "Jump to Line" input field and click the "Jump" button. The editor will scroll to the specified line and highlight it.
- **Highlighting**: The line that you jump to will be highlighted with a yellow background.

## Screenshot:
![Text Editor with Line Numbers](screenshot.png)

## Future Enhancements:
- Implement **file saving** and **loading** functionality.
- Add **syntax highlighting** for code editing.
- Allow **multiple themes** (dark/light mode).
- Add a **search** feature for text content.

## License:
This project is open source and available under the [MIT License](LICENSE).
