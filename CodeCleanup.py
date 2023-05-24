# CodeCleanup.py
from tkinter import filedialog
from pathlib import Path

# Import Black library directly
import black


class CodeCleanup:
    def __init__(self, root):
        self.root = root

    def format_with_black(self, file_path):
        # Format the python file using black
        try:
            # Read file content
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Format content with black
            mode = black.FileMode()
            formatted_content = black.format_file_contents(
                content, fast=False, mode=mode
            )

            # Write formatted content back to the file
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(formatted_content)

        except black.NothingChanged as e:
            print(f"No formatting changes needed for {file_path}.")
            return False

        except black.InvalidInput as e:
            print(f"Invalid Python code in {file_path}: {str(e)}")
            return False

        except Exception as e:
            print(f"An unexpected error occurred while formatting {file_path}: {str(e)}")
            return False

        return True

    def check_and_add_title(self, file_path):
        # Open the file and read its contents
        try:
            with open(file_path, "r+", encoding="utf-8") as f:
                lines = f.readlines()

                # Check if the first line is a title comment
                if not lines or not lines[0].startswith("# "):
                    # If not, insert a title comment
                    lines.insert(0, f"# {Path(file_path).name}\n")
                elif lines[0] != f"# {Path(file_path).name}\n":
                    # If there is a title comment but it's incorrect, replace it
                    lines[0] = f"# {Path(file_path).name}\n"

                # Write the modified contents back to the file
                f.seek(0)
                f.writelines(lines)
        except Exception as e:
            print(f"An error occurred while adding title to {file_path}: {str(e)}")
            return False
        return True

    def cleanup_directory(self):
        # Open a dialog for the user to select a folder
        directory = filedialog.askdirectory(
            title="Select directory to clean up", parent=self.root
        )
        directory = Path(directory)

        if not directory.is_dir():
            print(f"{directory} is not a valid directory.")
            return

        # Go through every python file in the directory and its subdirectories
        for file_path in directory.glob("**/*.py"):
            print(f"Processing {file_path}...")
            if self.check_and_add_title(file_path):
                print(f"Checked/added title to {file_path}.")
            if self.format_with_black(file_path):
                print(f"Formatted {file_path} with black.")
