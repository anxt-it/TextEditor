
import customtkinter as ctk
import os.path
from tkinter import filedialog, StringVar, messagebox
from pathlib import Path
import datetime
import time


ctk.set_default_color_theme("textEditor_theme.json")
ctk.set_appearance_mode("light")

# moved to main_menu.py
class MainMenu(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.menu_label = ctk.CTkLabel(self, text="Text Editor", font=self.controller.fonts['heading_one'])

        self.btns_frame = ctk.CTkFrame(self)

        self.new_file_menu_btn = ctk.CTkButton(self.btns_frame, text="Write Something New", font=self.controller.fonts["big_button"], command=lambda: self.controller.show_frame(NewFileMenu),anchor='w')
        self.open_file_btn = ctk.CTkButton(self.btns_frame, text="Continue Something Old", font=self.controller.fonts["big_button"], anchor='w' """command=lambda: self.controller.show_frame(Editor, 'open file'),""")
        self.settings_btn = ctk.CTkButton(self.btns_frame, text="Open Settings", font=self.controller.fonts["big_button"], anchor='w')

        self.exit_btn = ctk.CTkButton(self, text='exit', font=self.controller.fonts["small_button"], command=exit , anchor='e')


    def create_layout(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=2)

        self.menu_label.grid(row=0, column=0, padx=100, pady=20, sticky="sw")
        self.btns_frame.grid(row=1, column=0, sticky='nsew')

        self.new_file_menu_btn.grid(row=0, column=0, padx=100, sticky='nw')
        self.open_file_btn.grid(row=1, column=0, padx=100, sticky='nw')
        self.settings_btn.grid(row=2, column=0, padx=100, sticky='nw')

        self.exit_btn.grid(row=0, column=0, pady=10, sticky='ne')

# moved
class NewFileMenu(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.menu_label = ctk.CTkLabel(self, text="Text Editor", font=self.controller.fonts['heading_one'])
        self.back_button = ctk.CTkButton(self, text='back', font=self.controller.fonts["small_button"], command=lambda: self.controller.show_frame(MainMenu), anchor='e')

        self.menu_btns_frame = ctk.CTkFrame(self)

        self.timed_btn = ctk.CTkButton(self.menu_btns_frame, text="timed writing", font=self.controller.fonts['big_button'], command=self.open_timer, anchor='w')
        self.daily_btn = ctk.CTkButton(self.menu_btns_frame, text='daily pages', font=self.controller.fonts['big_button'], command=lambda: self.controller.show_frame(Editor, mode='daily', title=datetime.date.today().isoformat()), anchor='w')
        self.btn_prompt = ctk.CTkButton(self.menu_btns_frame, text='use prompt', font=self.controller.fonts['big_button'], command=lambda: self.controller.show_frame(Prompts), anchor='w')
        self.scene_btn = ctk.CTkButton(self.menu_btns_frame, text='scene', font=self.controller.fonts['big_button'], command=lambda: self.controller.show_frame(Editor, mode="scene"), anchor='w')
        self.memory_btn = ctk.CTkButton(self.menu_btns_frame, text='memory', font=self.controller.fonts['big_button'], command=lambda: self.controller.show_frame(Editor, mode="memory"), anchor='w')
        self.book_btn = ctk.CTkButton(self.menu_btns_frame, text='something from a book', font=self.controller.fonts['big_button'], command=lambda: self.controller.show_frame(Editor, mode="book"), anchor='w')
        self.movie_btn = ctk.CTkButton(self.menu_btns_frame, text='something from a movie', font=self.controller.fonts['big_button'], command=lambda: self.controller.show_frame(Editor, mode="movie"), anchor='w')
        self.other_btn = ctk.CTkButton(self.menu_btns_frame, text='other', font=self.controller.fonts['big_button'], command=lambda: self.controller.show_frame(Editor, mode="other"), anchor='w')

    def create_layout(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=2)

        self.back_button.grid(row=0, column=0, pady=10, sticky='ne')

        self.menu_label.grid(row=0, column=0, padx=100, pady=20, sticky="sw")
        self.menu_btns_frame.grid(row=1, column=0, sticky="nsew")

        self.timed_btn.grid(row=0, column=0, padx=100, sticky="nw")
        self.daily_btn.grid(row=1, column=0, padx=100,  sticky='nw')
        self.btn_prompt.grid(row=2, column=0, padx=100, sticky='nw')
        self.scene_btn.grid(row=3, column=0, padx=100, sticky='nw')
        self.memory_btn.grid(row=4, column=0, padx=100,  sticky='nw')
        self.book_btn.grid(row=5, column=0, padx=100, sticky='nw')
        self.movie_btn.grid(row=6, column=0, padx=100,  sticky='nw')
        self.other_btn.grid(row=7,column=0, padx=100,sticky='nw')

    def open_timer(self):
        top = ctk.CTkToplevel(self)
        top.title("timer")
        top.geometry("300x200")

        hour = StringVar()
        minute = StringVar()
        second = StringVar()
        # setting the default value as 0
        hour.set("00")
        minute.set("00")
        second.set("00")

        top.rowconfigure((0,1,2), weight=1)
        top.columnconfigure((0,1,2,3,4), weight=1)

        hour_entry = ctk.CTkEntry(top, textvariable=hour)
        hour_entry.grid(row=1, column=1, sticky='s')
        minute_entry = ctk.CTkEntry(top,  textvariable=minute)
        minute_entry.grid(row=1, column=2, sticky='s')
        second_entry = ctk.CTkEntry(top, textvariable=second)
        second_entry.grid(row=1, column=3, sticky='s')

        def on_submit():
            top.destroy()
            duration = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
            self.controller.show_frame(Editor, mode="timed", duration=duration)

        submit_btn = ctk.CTkButton(top, text="Submit time", command=on_submit)
        submit_btn.grid(row=2, column=1, columnspan=3)


# moved
class Editor(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.title_entry = ctk.CTkEntry(self, border_color='white', fg_color='transparent', placeholder_text='New Page', font=self.controller.fonts["heading_one"])
        self.textbox = ctk.CTkTextbox(self, font=('SF Display', 17))
        self.back_button = ctk.CTkButton(self, text='back', font=self.controller.fonts["small_button"], command=lambda: self.controller.show_frame(NewFileMenu), anchor='e')
        self.save_button = ctk.CTkButton(self, text='save', font=self.controller.fonts["small_button"], command=self.save_file, anchor='e')
        self.status_bar = ctk.CTkLabel(self, text='Ready   ', font=('SF Display', 12), anchor='w')
        self.filepath_status = ctk.CTkLabel(self, text="   no file path yet",font=('SF Display', 12), anchor='e')

    def create_layout(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=2)

        self.title_entry.grid(row=0, column=0, padx=100, sticky='swe')
        self.textbox.grid(pady=10, padx=100, sticky='nsew')
        self.back_button.grid(row=0, column=0, pady=10, sticky='ne')
        self.save_button.grid(row=0, column=0, pady=40, sticky='ne')

        self.status_bar.grid(row=1, column=0, sticky='se')
        self.filepath_status.grid(row=1, column=0, sticky='sw')


    def reset_editor(self):
        self.textbox.delete("1.0", ctk.END)
        self.title_entry.delete(0, ctk.END)
        self.title_entry.configure(placeholder_text_color='#dbdbd9', placeholder_text="New Page")
        self.file_path = None


    def update_content(self, mode='other', title=None, folder=None, duration=None):
            self.reset_editor()
            self.mode = mode
            self.folder = folder # not sure i ever use that
            self.title = title

            if mode == "daily":
                self.title_entry.configure(placeholder_text=title, placeholder_text_color="gray14")
            elif mode == "prompt":
                self.title_entry.configure(placeholder_text=title, placeholder_text_color="gray14")
            elif mode == "file" and file_path:  # not sure what and file_path means
                # self.open_file()
                pass
            elif mode == "timed":
                # create timer frame
                timer_frame = ctk.CTkFrame(self, fg_color='orange', width=200, height=70)
                timer_frame.grid(row=0, column=0, padx=100, pady=50, sticky='nw')


                label = ctk.CTkLabel(timer_frame, text=" ")
                label.pack()

                hour = duration // 3600
                minute = (duration - hour*3600) // 60
                second = (duration - hour*3600 - minute*60)
                while duration > -1:
                    label.configure(text=f"{hour}:{minute}:{second}")
                    time.sleep(1)

                    if duration == 0:
                        messagebox.showinfo("Time Countdown", "Times Up")
                    duration -= 1





            else: # the other
                self.title_entry.configure(placeholder_text="New Page")


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

# moved
class Prompts(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.prompts = self.load_prompts()
        self.layout()

    def load_prompts(self):
        prompts_file = 'prompts.txt'

        if os.path.exists(prompts_file):
            with open(prompts_file, "r") as f:
                prompts = [line.strip() for line in f if line.strip()]
                return prompts
        return []

    def layout(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=2)

        self.choose_prompt_label = ctk.CTkLabel(self, text="Choose a Prompt", font=self.controller.fonts["heading_one"])
        self.choose_prompt_label.grid(row=0, column=0, padx=100, sticky='sw')

        self.prompts_list_frame = ctk.CTkFrame(self)
        self.prompts_list_frame.grid(row=1,column=0,sticky='nsew')

        if not self.prompts:
            self.label = ctk.CTkLabel(self.prompts_list_frame, text = 'No Prompts Yet', font=('SF Display', 17))
            self.label.grid(row=1, column=0, pady=50, sticky="nw")

        else:
            for i, prompt in enumerate(self.prompts):
                self.prompt_btn = ctk.CTkButton(self.prompts_list_frame, text=prompt, font=('SF Display', 16), command=lambda p=prompt: self.controller.show_frame(Editor, mode="prompt", title=p), anchor='w')
                self.prompt_btn.grid(row=i, column=0, padx=100, pady=5, sticky='nw')

        self.back_button = ctk.CTkButton(self, text='back', font=self.controller.fonts["small_button"], command=lambda: self.controller.show_frame(NewFileMenu), anchor='e')
        self.back_button.grid(row=0, column=0, pady=10, sticky='ne')



# moved to app.py
class TextEditor(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Text Editor")
        self.geometry("1250x1000")


        self.fonts = {
            "heading_one": ctk.CTkFont(family="SF Display", size=58, weight="bold"),
            "big_button": ctk.CTkFont(family="SF Display", size=20, weight="bold"),
            "small_button": ctk.CTkFont(family="SF Display", size=14)
        }

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # create a dictionary of frames
        self.frames = {}
        for F in (MainMenu, NewFileMenu, Editor, Prompts):
            frame = F(self, self)  # parent = self, controller = self
            # the TextEditor class acts as the root window for the frames
            self.frames[F.__name__] = frame  # turns the class name into a string
            frame.grid(row=0, column=0, sticky='nsew')


        # run
        self.show_frame(MainMenu)
        self.mainloop()

    def show_frame(self, frame_class, **kwargs):
        frame = self.frames[frame_class.__name__]
        frame.tkraise()
        if hasattr(frame, "update_content"):
            frame.update_content(**kwargs)



app = TextEditor()
app.mainloop()