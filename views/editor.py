
import customtkinter as ctk
import os.path
from services.file_manager import save_file

class Editor(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        from views.new_file_menu import NewFileMenu

        self.title_entry = ctk.CTkEntry(self, border_color='white', fg_color='transparent', placeholder_text='New Page', font=self.controller.fonts["heading_one"])

        self.textbox = ctk.CTkTextbox(self, font=('SF Display', 17))

        self.back_button = ctk.CTkButton(self, text='back', font=self.controller.fonts["small_button"], command=lambda: self.controller.show_frame(NewFileMenu), anchor='e')
        self.save_button = ctk.CTkButton(self, text='save', font=self.controller.fonts["small_button"], command=save_file, anchor='e')

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


            else: # the other
                self.title_entry.configure(placeholder_text="New Page")


