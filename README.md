# CodeWorks

CodeWorks is a Python project that provides two main functionalities: code cleanup and code clipboard. It includes three modules: `CodeCleanup.py`, `CodeClipboard.py`, and `CodeWorks.py`. This README file provides an overview of the project and instructions for running and using the different features.

## Features

1. Code Cleanup: The `CodeCleanup.py` module allows you to format Python files using the Black library and add or update a title comment at the beginning of each file.
2. Code Clipboard: The `CodeClipboard.py` module enables you to copy a project's file structure and selected file contents to the clipboard.

## Project Structure

The project structure is as follows:

```
└─ CodeWorks/
   ├─ CodeCleanup.py
   ├─ CodeClipboard.py
   └─ CodeWorks.py
```

- `CodeWorks/` is the root directory of the project.
- `CodeCleanup.py` contains the code for the code cleanup functionality.
- `CodeClipboard.py` contains the code for the code clipboard functionality.
- `CodeWorks.py` is the main file that integrates the functionality and provides a graphical user interface (GUI) for running the features.

## Prerequisites

- Python 3.x installed on your system.
- The following Python libraries are required:
  - tkinter
  - black
  - pyperclip

## Installation

1. Clone the repository or download the project files to your local machine.

```
git clone https://github.com/your-username/CodeWorks.git
```

1. Install the required Python libraries by running the following command:

```
pip install tkinter black pyperclip
```

## Usage

To use the CodeWorks project, follow these steps:

1. Open a terminal or command prompt and navigate to the project directory.

```
cd CodeWorks
```

1. Run the `CodeWorks.py` file to start the GUI.

```
python CodeWorks.py
```

1. The CodeWorks GUI will appear with two buttons: "Code Cleanup" and "Code Clipboard".

### Code Cleanup

The "Code Cleanup" feature allows you to format Python files and add or update a title comment at the beginning of each file.

1. Click the "Code Cleanup" button.
2. A file dialog will open. Select the directory you want to clean up.
3. CodeWorks will process each Python file in the selected directory and its subdirectories.
   - The file will be formatted using the Black library.
   - If a title comment is missing or incorrect, CodeWorks will add or update it.
4. The progress will be displayed in the terminal or command prompt.
5. Once the cleanup is completed, a success message will be shown.

### Code Clipboard

The "Code Clipboard" feature allows you to copy a project's file structure and selected file contents to the clipboard.

1. Click the "Code Clipboard" button.
2. A file dialog will open. Select the project directory you want to copy.
3. CodeWorks will generate an ASCII tree structure of the project's files and directories.
4. The tree structure will be printed in the terminal or command prompt.
5. You will be prompted to enter the numbers of the files you want to select, separated by commas.
6. After selecting the files, CodeWorks will copy the ASCII tree structure and the contents of the selected files to the clipboard.
7. You can paste the copied content wherever you want.