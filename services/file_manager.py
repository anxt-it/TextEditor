
from tkinter import filedialog
from pathlib import Path


def open_file():

    file_path = filedialog.askopenfilename(title="open file",
                                      defaultextension='.txt',
                                      filetypes=(("Text Files", "*.txt"), ("All Files", "*.*"))
                                      )

    if not file_path:
        return None, None, None

    try:
        file_name = Path(file_path).stem

        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()

        return file_name, file_content, file_path

    except Exception:
        return None, None, None


def write_to_file(content, path):
    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)



def save_as_file(content):
    file_path = filedialog.asksaveasfilename(defaultextension='.txt',
                                             title="save file",
                                             filetypes=(("Text Files", "*.txt"), ("All Files", "*.*"))
                                             )

    if file_path:
        write_to_file(content, file_path)
        return file_path

    else:
        return None



def save_file(content, curr_path):
    write_to_file(content, curr_path)
