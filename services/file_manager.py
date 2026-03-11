
from tkinter import filedialog
from pathlib import Path

def open_file():

    file_path = filedialog.askopenfilename(title="open file",
                                      defaultextension='.txt',
                                      filetypes=(("Text Files", "*.txt"), ("All Files", "*.*"))
                                      )

    try:
        file_name = Path(file_path).stem

        with open(file_path, 'r') as file:
            file_content = file.read()
        return file_name, file_content

    except:
        return None, None


# save file
