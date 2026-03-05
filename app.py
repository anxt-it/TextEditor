import customtkinter as ctk
from views.main_menu import MainMenu
from views.editor import Editor
from views.new_file_menu import NewFileMenu
from views.prompts import Prompts


ctk.set_default_color_theme("textEditor_theme.json")
ctk.set_appearance_mode("light")

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

