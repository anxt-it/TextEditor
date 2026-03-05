import customtkinter as ctk


class Menu(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.welcome_label = ctk.CTkLabel(self, text='Text Editor', font=self.controller.fonts["heading_one"])

        self.menu_btns_frame = ctk.CTkFrame(self)

        self.timed_btn = ctk.CTkButton(self.menu_btns_frame, text="timed writing", font=self.controller.fonts["big_button"], anchor='w')
        self.daily_btn = ctk.CTkButton(self.menu_btns_frame, text='daily pages', font=self.controller.fonts["big_button"], anchor='w')
        self.prompts_btn = ctk.CTkButton(self.menu_btns_frame, text='use prompt', font=self.controller.fonts["big_button"], command=lambda: self.controller.show_frame(Prompts), anchor='w')
        self.scene_btn = ctk.CTkButton(self.menu_btns_frame, text='scene', font=self.controller.fonts["big_button"], anchor='w')
        self.memory_btn = ctk.CTkButton(self.menu_btns_frame, text='memory', font=self.controller.fonts["big_button"], anchor='w')
        self.book_btn = ctk.CTkButton(self.menu_btns_frame, text='something from a book', font=self.controller.fonts["big_button"], anchor='w')
        self.movie_btn = ctk.CTkButton(self.menu_btns_frame, text='something from a movie', font=self.controller.fonts["big_button"], anchor='w')
        self.other_btn = ctk.CTkButton(self.menu_btns_frame, text='other', font=self.controller.fonts["big_button"], anchor='w')


    def create_layout(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=2)

        self.welcome_label.grid(row=0, column=0, padx=100, pady=20, sticky="sw")

        self.menu_btns_frame.grid(row=1,column=0,sticky='nsew')

        self.timed_btn.grid(row=0, column=0, padx=100, sticky="nw")
        self.daily_btn.grid(row=1, column=0, padx=100,  sticky='nw')
        self.prompts_btn.grid(row=2, column=0, padx=100, sticky='nw')
        self.scene_btn.grid(row=3, column=0, padx=100, sticky='nw')
        self.memory_btn.grid(row=4, column=0, padx=100,  sticky='nw')
        self.book_btn.grid(row=5, column=0, padx=100, sticky='nw')
        self.movie_btn.grid(row=6, column=0, padx=100,  sticky='nw')
        self.other_btn.grid(row=7,column=0, padx=100,sticky='nw')


class Editor(ctk.CTkFrame):
    pass

class Prompts(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = ctk.CTkLabel(self, text="this is prompts", font=self.controller.fonts["heading_one"])
        label.pack()


class TextEditor(ctk.CTk):
    def __init__(self):

        # main setup
        super().__init__()
        self.title("Text Editor")
        self.geometry("1250x1000")
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("textEditor_theme.json")

        # grid
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # define fonts
        self.fonts = {
            "heading_one": ctk.CTkFont(family="SF Display", size=58, weight="bold"),
            "big_button": ctk.CTkFont(family="SF Display", size=20, weight="bold"),
            "small_button": ctk.CTkFont(family="SF Display", size=14)
        }

        # create a dictionary of frames
        self.frames = {}
        for F in (Menu, Editor, Prompts):
            frame = F(self, self) # parent = self, controller = self
            # the TextEditor class acts as the root window for the frames
            self.frames[F.__name__] = frame # turns the class name into a string
            frame.grid(row=0, column=0, sticky='nsew')

        # run
        self.show_frame(Menu)
        # self.mainloop()


    def show_frame(self, frame_class):
        frame = self.frames[frame_class.__name__]
        frame.tkraise()

if __name__ == "__main__":
    app = TextEditor()
    app.mainloop()



