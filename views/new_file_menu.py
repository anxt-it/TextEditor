
import customtkinter as ctk
from tkinter import filedialog, StringVar, messagebox
import datetime
from views.editor import Editor
from views.prompts import Prompts


class NewFileMenu(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.create_widgets_layout()


    def create_widgets_layout(self):
        from views.main_menu import MainMenu

        self.menu_label = ctk.CTkLabel(self, text="Text Editor", font=self.controller.fonts['heading_one'])
        self.back_button = ctk.CTkButton(self, text='back', font=self.controller.fonts["small_button"], command=lambda: self.controller.show_frame(MainMenu), anchor='e')

        self.menu_btns_frame = ctk.CTkFrame(self)

        options = [
            ("timed writing", self.open_timer),
            ("daily pages", lambda: self.controller.show_frame(Editor, mode="daily", title=datetime.date.today().isoformat())),
            ("use prompt", lambda: self.controller.show_frame(Prompts)),
            ("scene", lambda: self.controller.show_frame(Editor, mode="scene")),
            ("memory", lambda: self.controller.show_frame(Editor, mode="memory")),
            ("something from a book", lambda: self.controller.show_frame(Editor, mode="book")),
            ("something from a movie", lambda: self.controller.show_frame(Editor, mode="movie")),
            ("other", lambda: self.controller.show_frame(Editor, mode="other"))
        ]


        for i, (text, command) in enumerate(options):

            btn = ctk.CTkButton(
                self.menu_btns_frame,
                text= text,
                font=self.controller.fonts['big_button'],
                command=command,
                anchor='w'
            )

            btn.grid(row=i, column=0, padx=100, sticky="nw")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=2)

        self.back_button.grid(row=0, column=0, pady=10, sticky='ne')

        self.menu_label.grid(row=0, column=0, padx=100, pady=20, sticky="sw")
        self.menu_btns_frame.grid(row=1, column=0, sticky="nsew")



# everything down here i hate
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
