
import customtkinter as ctk
from tkinter import filedialog, StringVar, messagebox
import datetime
from views.editor import Editor
from views.prompts import Prompts


class NewFileMenu(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        from views.main_menu import MainMenu

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
