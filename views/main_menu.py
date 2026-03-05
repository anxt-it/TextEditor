
import customtkinter as ctk
from views.new_file_menu import NewFileMenu


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
