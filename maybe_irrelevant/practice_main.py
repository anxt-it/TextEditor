
import customtkinter as ctk
import os.path
from tkinter import filedialog
from pathlib import Path
import datetime


ctk.set_default_color_theme("textEditor_theme.json")
ctk.set_appearance_mode("light")

global opened_file_name
opened_file_name = False

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
        self.open_file_btn = ctk.CTkButton(self.btns_frame, text="Continue Something Old", font=self.controller.fonts["big_button"], command=lambda: self.controller.show_frame(Editor, 'open file'), anchor='w')
        self.settings_btn = ctk.CTkButton(self.btns_frame, text="Open Settings", font=self.controller.fonts["big_button"], anchor='w')

    def create_layout(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=2)

        self.menu_label.grid(row=0, column=0, padx=100, pady=20, sticky="sw")
        self.btns_frame.grid(row=1, column=0, sticky='nsew')

        self.new_file_menu_btn.grid(row=0, column=0, padx=100, sticky='nw')
        self.open_file_btn.grid(row=1, column=0, padx=100, sticky='nw')
        self.settings_btn.grid(row=2, column=0, padx=100, sticky='nw')

class NewFileMenu(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.menu_label = ctk.CTkLabel(self, text="Text Editor", font=self.controller.fonts['heading_one'])

        self.menu_btns_frame = ctk.CTkFrame(self)

        self.timed_btn = ctk.CTkButton(self.menu_btns_frame, text="timed writing", font=self.controller.fonts['big_button'], anchor='w')
        self.daily_btn = ctk.CTkButton(self.menu_btns_frame, text='daily pages', font=self.controller.fonts['big_button'], command=lambda: self.controller.show_frame(frame_class=Editor, mode='daily' ,title=datetime.date.today().isoformat(), file_path='daily pages'), anchor='w')
        self.btn_prompt = ctk.CTkButton(self.menu_btns_frame, text='use prompt', font=self.controller.fonts['big_button'], command=lambda: self.controller.show_frame(Prompts), anchor='w')
        self.other = ctk.CTkButton(self.menu_btns_frame, text='other',
                                        font=self.controller.fonts['big_button'],
                                        command=lambda: self.controller.show_frame(Editor, mode='other'), anchor='w')

    def create_layout(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=2)

        self.menu_label.grid(row=0, column=0, padx=100, pady=20, sticky="sw")
        self.menu_btns_frame.grid(row=1, column=0, sticky="nsew")

        self.timed_btn.grid(row=0, column=0, padx=100, sticky="nw")
        self.daily_btn.grid(row=1, column=0, padx=100,  sticky='nw')
        self.btn_prompt.grid(row=2, column=0, padx=100, sticky='nw')
        self.other.grid(row=3, column=0, padx=100, sticky='nw')

class Editor(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.title_entry = ctk.CTkEntry(self, border_color='white', fg_color='transparent', placeholder_text='New Page', font=self.controller.fonts["heading_one"])
        self.textbox = ctk.CTkTextbox(self, font=('SF Display', 17))
        self.back_button = ctk.CTkButton(self, text='back', font=self.controller.fonts["small_button"], command=lambda: self.controller.show_frame(MainMenu), anchor='e')
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
        self.title_entry.configure(placeholder_text_color='#dbdbd9', placeholder_text="New Page")
        self.file_path = None


    def update_content(self, mode='other', title=None, file_path=None):
        self.reset_editor()
        self.mode = mode
        self.file_path = file_path

        if mode == "daily":
            self.title_entry.configure(placeholder_text=title, placeholder_text_color="gray14")
        elif mode == "prompt":
            self.title_entry.configure(placeholder_text=title, placeholder_text_color="gray14")
        elif mode == "file" and file_path: # not sure what and file_path means
            self.open_file()
        else: # the other
            self.title_entry.configure(placeholder_text="New Page")

        """
        
        self.title_entry.configure(placeholder_text=title or "New Page")
        if title == "default":
            self.title_entry.configure(placeholder_text='New Page', placeholder_text_color="#dbdbd9") # feels like patchwork, but i think it's fine for now
        else:
            self.title_entry.configure(placeholder_text=title, placeholder_text_color="gray14") # makes it look like a label, but is still changeable
        # self.textbox.delete(1.0,  ctk.END)
"""
        """ do something like 
        if mode == "something" and file_path: 
        then use save method or load file or something 
        else: reset_editor() """


    def open_file(self):
        self.textbox.delete("1.0", ctk.END)
        text_file = filedialog.askopenfilename(title="open file",
                                               initialdir="/Users/anatorevi/PycharmProjects/TextEditor/TestFolder",
                                               defaultextension='.txt',
                                               filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
        # check to see if theres a file name
        if text_file:
            # make file name global so we can access later
            global opened_file_name
            opened_file_name = text_file
        # actually open the file
        text_file = open(text_file, 'r')
        inside_file = text_file.read() # read whats in there and assign to variable
        self.textbox.insert(ctk.END, inside_file)
        file_path = Path(opened_file_name)
        # print(file_path.stem)
        self.update_content(file_path.stem)
        text_file.close()


    def save_as_file(self):
        text_file = filedialog.asksaveasfilename(defaultextension='.txt',
                                                 initialdir="/Users/anatorevi/PycharmProjects/TextEditor/TestFolder",
                                                 title="save file",
                                                 filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
        if text_file:
            # save the file
            text_file = open(text_file, 'w')
            text_file.write(self.textbox.get(1.0, ctk.END))
            self.status_bar.configure(text=f"Saved: {opened_file_name}")
            text_file.close()


    def save_file(self):
        if self.mode == "prompt":
            # create


        self.status_bar.configure(text=f"Saved  ")
        self.filepath_status.configure(text=f"  /Users/anatorevi/PycharmProjects/TextEditor/TestFolder/{self.file_path}")


class Prompts(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.prompts = self.load_prompts()
        self.layout()

    def load_prompts(self):
        prompts_file = '../prompts.txt'

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
                self.prompt_btn = ctk.CTkButton(self.prompts_list_frame, text=prompt, font=('SF Display', 16), command=lambda p=prompt: self.controller.show_frame(frame_class=Editor,mode="prompt", title=p, file_path='Prompts'), anchor='w')
                self.prompt_btn.grid(row=i, column=0, padx=100, pady=5, sticky='nw')

        self.back_button = ctk.CTkButton(self, text='back', font=self.controller.fonts["small_button"], command=lambda: self.controller.show_frame(MainMenu), anchor='e')
        self.back_button.grid(row=0, column=0, pady=10, sticky='ne')


class TextEditor(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Text Editor Practice")
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
        self.show_frame(NewFileMenu)
        self.mainloop()

    def show_frame(self, frame_class, **kwargs):
        frame = self.frames[frame_class.__name__]
        frame.tkraise()
        if hasattr(frame, "update_content"):
            frame.update_content(**kwargs)

app = TextEditor()
app.mainloop()