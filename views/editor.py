
import customtkinter as ctk
from services.file_manager import save_as_file, save_file

class Editor(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.create_widgets()
        self.create_layout()

        self.current_file_path = None


    def create_widgets(self):
        from views.main_menu import MainMenu

        self.title_entry = ctk.CTkEntry(self, border_color='white',
                                        fg_color='transparent',
                                        placeholder_text='New Page',
                                        font=self.controller.fonts["heading_one"])

        self.textbox = ctk.CTkTextbox(self, font=('SF Display', 17))

        self.home_button = ctk.CTkButton(self, text='home',
                                         font=self.controller.fonts["small_button"],
                                         command=lambda: self.controller.show_frame(MainMenu),
                                         anchor='e')
        self.save_button = ctk.CTkButton(self, text='save',
                                         font=self.controller.fonts["small_button"],
                                         command=self.handle_save,
                                         anchor='e')

        self.save_as_button = ctk.CTkButton(self, text='save as',
                                         font=self.controller.fonts["small_button"],
                                         command=self.handle_save_as,
                                         anchor='e')


        self.status_bar = ctk.CTkLabel(self, text='Ready   ',
                                       font=('SF Display', 12),
                                       anchor='w')
        self.filepath_status = ctk.CTkLabel(self, text="   no file path yet",
                                            font=('SF Display', 12),
                                            anchor='e')



        self.switch_var = ctk.StringVar(value='off')
        self.direction_toggle = ctk.CTkSwitch(self, onvalue='on', offvalue='off',
                                              command=self.RTL_switch,
                                              variable=self.switch_var,
                                              text='RTL')
        self.textbox.bind("<KeyRelease>", self.RTL_switch)



    def create_layout(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=2)

        self.title_entry.grid(row=0, column=0, padx=100, sticky='swe')
        self.textbox.grid(pady=10, padx=100, sticky='nsew')

        self.home_button.grid(row=0, column=0, pady=10, sticky='ne')
        self.save_button.grid(row=0, column=0, pady=40, sticky='ne')
        self.save_as_button.grid(row=0, column=0, pady=70, sticky='ne')


        self.status_bar.grid(row=1, column=0, sticky='se')
        self.filepath_status.grid(row=1, column=0, sticky='sw')

        self.direction_toggle.grid(row=0, column=0, pady=100, sticky='ne')



    def handle_save(self):
        text_to_save = self.textbox.get("1.0", "end-1c")

        if self.current_file_path:
            save_file(text_to_save, self.current_file_path)
            self.status_bar.configure(text="Saved   ")

        else:
            self.handle_save_as()



    def handle_save_as(self):
        text_to_save = self.textbox.get("1.0", "end-1c")
        saved_path = save_as_file(text_to_save)

        if saved_path:
            self.current_file_path = saved_path
            self.status_bar.configure(text='Saved   ')
            self.filepath_status.configure(text=saved_path)




    def reset_editor(self):
        self.textbox.delete("1.0", ctk.END)
        self.title_entry.delete(0, ctk.END)
        self.title_entry.configure(placeholder_text_color='#dbdbd9', placeholder_text="New Page")
        self.direction_toggle.deselect()



    def update_content(self, title=None, file_text=None, file_path=None):
        self.reset_editor()

        self.current_file_path = file_path
        self.filepath_status.configure(text=file_path)

        if title:
            self.title_entry.configure(placeholder_text_color='gray14', placeholder_text=title)

        if file_text:
            self.textbox.insert("1.0", file_text)



    def RTL_switch(self, event=None):
        self.textbox.tag_config("right", justify='right')

        if self.switch_var.get() == "on":

            if self.textbox.get("1.0", "end-1c") == "":
                self.textbox.insert("1.0", "\u200F") # RTL mark

            self.textbox.tag_add("right", "1.0", "end")

        else:
            self.textbox.tag_remove("right", "1.0", "end")

