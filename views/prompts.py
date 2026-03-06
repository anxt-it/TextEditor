
import customtkinter as ctk
import os.path
from views.editor import Editor


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
        from views.new_file_menu import NewFileMenu
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
                self.prompt_btn = ctk.CTkButton(
                    self.prompts_list_frame,
                    text=prompt,
                    font=('SF Display', 16),
                    command=lambda p=prompt: self.controller.show_frame(Editor, title=p),
                    anchor='w')
                self.prompt_btn.grid(row=i, column=0, padx=100, pady=5, sticky='nw')

        self.back_button = ctk.CTkButton(self, text='back', font=self.controller.fonts["small_button"], command=lambda: self.controller.show_frame(NewFileMenu), anchor='e')
        self.back_button.grid(row=0, column=0, pady=10, sticky='ne')
