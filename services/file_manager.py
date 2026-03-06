import os.path


def save_file(self):
    # if it's an opened file, just overwrite
    if hasattr(self, "file_path") and self.file_path:
        with open(self.file_path, "w") as f:
            f.write(self.textbox.get(1.0, "end-1c"))
        self.status_bar.configure(text="Saved")
        self.filepath_status.configure(text=f"   {self.file_path}")
        return

    def smart_save_with_name(folder_name):
        base_folder = "/Users/anatorevi/PycharmProjects/TextEditor/TestFolder"
        # base_folder = os.path.home()

        os.makedirs(base_folder, exist_ok=True)

        folder = os.path.join(base_folder, folder_name)
        os.makedirs(folder, exist_ok=True)
        base_name = f"{self.title}.txt"
        file_path = os.path.join(folder, base_name)

        counter = 1
        while os.path.exists(file_path):
            base_name = f"{self.title}_{counter}.txt"
            file_path = os.path.join(folder, base_name)
            counter += 1

        self.file_path = file_path
        with open(file_path, "w") as f:
            f.write(self.textbox.get(1.0, "end-1c"))

        self.status_bar.configure(text=f"Saved  ")
        self.filepath_status.configure(text=f"  {folder}")

    def save_without_name(folder_name):
        base_folder = "/Users/anatorevi/PycharmProjects/TextEditor/TestFolder"
        os.makedirs(base_folder, exist_ok=True)

        folder = os.path.join(base_folder, folder_name)
        os.makedirs(folder, exist_ok=True)
        base_name = f"{self.title_entry.get()}.txt"
        file_path = os.path.join(folder, base_name)

        counter = 1
        while os.path.exists(file_path):
            base_name = f"{self.title}_{counter}.txt"
            file_path = os.path.join(folder, base_name)
            counter += 1

        self.file_path = file_path
        with open(file_path, "w") as f:
            f.write(self.textbox.get(1.0, "end-1c"))

        self.status_bar.configure(text=f"Saved  ")
        self.filepath_status.configure(text=f"  {folder}")

    if self.mode == "prompt":
        smart_save_with_name("Prompts")
    elif self.mode == "daily":
        smart_save_with_name("Daily Pages")
    elif self.mode == "scene":
        save_without_name("Scene")
    elif self.mode == "memory":
        save_without_name("Memory")
    elif self.mode == "book":
        save_without_name("Something From a Book")
    elif self.mode == "movie":
        save_without_name("Something From a Movie")
    elif self.mode == "other":
        save_without_name("Other")



def open_file():
    print("this should open a file")