
import customtkinter as ctk
from views.new_file_menu import NewFileMenu
from services.file_manager import open_file
from views.editor import Editor

class MainMenu(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.menu_label = ctk.CTkLabel(self, text="Text Editor", font=self.controller.fonts['heading_one'])

        self.btns_frame = ctk.CTkFrame(self)

        options = [
            ("Write Something New", lambda: self.controller.show_frame(NewFileMenu)),
            ("Continue Something Old", self.continue_old),
            ("Open Settings", None),
            ("Exit", exit)
        ]

        for i, (text, command) in enumerate(options):
            btn = ctk.CTkButton(
                self.btns_frame,
                text=text,
                font=self.controller.fonts["big_button"],
                command=command,
                anchor='w'
            )

            btn.grid(row=i, column=0, padx=100, sticky='nw')

    def create_layout(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=2)

        self.menu_label.grid(row=0, column=0, padx=100, pady=20, sticky="sw")
        self.btns_frame.grid(row=1, column=0, sticky='nsew')


    def continue_old(self):
        title, file_text = open_file()
        if title and file_text:
            self.controller.show_frame(Editor, title=title, file_text=file_text)
        else:
            return


