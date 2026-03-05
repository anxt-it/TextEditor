import customtkinter as ctk
import os.path

prompts_file = '../prompts.txt'

def load_prompts():
    if os.path.exists(prompts_file):
        with open(prompts_file, "r") as f:
            prompts = [line.strip() for line in f if line.strip()]
            return prompts
    return []


class TextEditor():
    def __init__(self):

        self.prompts = load_prompts()
        print(self.prompts)

        self.root=ctk.CTk()
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("textEditor_theme.json")
        self.root.geometry("1250x1000")
        self.root.title("Text Editor")


        # -- Design --
        ## define fonts
        heading_one = ctk.CTkFont(family='SF Display', size=58, weight='bold')
        big_buttons_font = ctk.CTkFont(family='SF Display', size=20, weight='bold')
        small_big_buttons_font = ctk.CTkFont(family='SF Display', size=14)
        ## root grid
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        #self.root.columnconfigure(0, weight=1)
        #self.root.columnconfigure(1, weight=4)
        #self.root.columnconfigure(2, weight=1)
        #self.root.rowconfigure(0, weight=1)


        # -- Create frames --
        self.menu_frame = ctk.CTkFrame(self.root, fg_color='white')
        self.editor_frame = ctk.CTkFrame(self.root, fg_color='white')
        self.prompts_frame = ctk.CTkFrame(self.root, fg_color='white')

        for frame in (self.menu_frame, self.editor_frame, self.prompts_frame):
            frame.grid(row=0,column=0, sticky='nsew')



        # -- Menu frame
        ## grid
        self.menu_frame.columnconfigure(0, weight=1)
        self.menu_frame.rowconfigure(0, weight=1)
        self.menu_frame.rowconfigure(1, weight=2)

        welcome_label = ctk.CTkLabel(self.menu_frame, text='Text Editor', font=heading_one)
        welcome_label.grid(row=0, column=0, padx=100, pady=20, sticky="sw")

        self.menu_btns_frame = ctk.CTkFrame(self.menu_frame) # creates sub_frame, esthetics
        self.menu_btns_frame.grid(row=1,column=0,sticky='nsew')

        # main menu buttons
        self.timed_btn = ctk.CTkButton(self.menu_btns_frame, text="timed writing", font=big_buttons_font, anchor='w')
        self.timed_btn.grid(row=0, column=0, padx=100, sticky="nw")

        self.daily_btn = ctk.CTkButton(self.menu_btns_frame, text='daily pages', font=big_buttons_font, anchor='w')
        self.daily_btn.grid(row=1, column=0, padx=100,  sticky='nw')

        self.prompts_btn = ctk.CTkButton(self.menu_btns_frame, text='use prompt', font=big_buttons_font, command=lambda: self.show_frame(self.prompts_frame), anchor='w')
        self.prompts_btn.grid(row=2, column=0, padx=100, sticky='nw')

        self.scene_btn = ctk.CTkButton(self.menu_btns_frame, text='scene', font=big_buttons_font, command=lambda: self.show_frame(self.editor_frame), anchor='w')
        self.scene_btn.grid(row=3, column=0, padx=100, sticky='nw')

        self.memory_btn = ctk.CTkButton(self.menu_btns_frame, text='memory', font=big_buttons_font, command=lambda: self.show_frame(self.editor_frame), anchor='w')
        self.memory_btn.grid(row=4, column=0, padx=100,  sticky='nw')

        self.book_btn = ctk.CTkButton(self.menu_btns_frame, text='something from a book', font=big_buttons_font, command=lambda: self.show_frame(self.editor_frame), anchor='w')
        self.book_btn.grid(row=5, column=0, padx=100, sticky='nw')

        self.movie_btn = ctk.CTkButton(self.menu_btns_frame, text='something from a movie', font=big_buttons_font, command=lambda: self.show_frame(self.editor_frame), anchor='w')
        self.movie_btn.grid(row=6, column=0, padx=100,  sticky='nw')

        self.other_btn = ctk.CTkButton(self.menu_btns_frame, text='other', font=big_buttons_font, command=lambda: self.show_frame(self.editor_frame), anchor='w')
        self.other_btn.grid(row=7,column=0, padx=100,sticky='nw')



        # -- Editor page
        ## grid
        self.editor_frame.columnconfigure(0, weight=1)
        self.editor_frame.rowconfigure(0, weight=1)
        self.editor_frame.rowconfigure(1, weight=2)

        title_entry = ctk.CTkEntry(self.editor_frame, border_color='white', fg_color='transparent', placeholder_text='New Page', font=heading_one)
        title_entry.grid(row=0, column=0, padx=100, sticky='swe')

        self.textbox = ctk.CTkTextbox(self.editor_frame, font=('SF Display', 17))
        self.textbox.grid(pady=10, padx=100, sticky='nsew')

        self.back_button = ctk.CTkButton(self.editor_frame, text='back', font=small_big_buttons_font, command=lambda: self.show_frame(self.menu_frame), anchor='e')
        self.back_button.grid(row=0, column=0, pady=10, sticky='ne')


        # -- Editor prompt page page
        ## grid
        self.editor_frame.columnconfigure(0, weight=1)
        self.editor_frame.rowconfigure(0, weight=1)
        self.editor_frame.rowconfigure(1, weight=2)

        title_entry = ctk.CTkEntry(self.editor_frame, border_color='white', fg_color='transparent', placeholder_text='New Page', font=heading_one)
        title_entry.grid(row=0, column=0, padx=100, sticky='swe')

        self.textbox = ctk.CTkTextbox(self.editor_frame, font=('SF Display', 17))
        self.textbox.grid(pady=10, padx=100, sticky='nsew')

        self.back_button = ctk.CTkButton(self.editor_frame, text='back', font=small_big_buttons_font, command=lambda: self.show_frame(self.menu_frame), anchor='e')
        self.back_button.grid(row=0, column=0, pady=10, sticky='ne')


        # -- Editor with prompts page

        self.prompts_frame.columnconfigure(0, weight=1)
        self.prompts_frame.rowconfigure(0, weight=1)
        self.prompts_frame.rowconfigure(1, weight=2)

        choose_prompt_label = ctk.CTkLabel(self.prompts_frame, text='Choose a Prompt', font=heading_one)
        choose_prompt_label.grid(row=0, column=0, padx=100, sticky='sw')

        self.prompts_list_frame = ctk.CTkFrame(self.prompts_frame) # creates sub_frame, esthetics
        self.prompts_list_frame.grid(row=1,column=0,sticky='nsew')


        if not self.prompts:
            self.label = ctk.CTkLabel(self.prompts_list_frame, text = 'No Prompts Yet', font=('SF Display', 17))
            self.label.grid(row=1, column=0, pady=50, sticky='nw')

        else:
            for i, prompt in enumerate(self.prompts, 1):
                self.prompt_btn = ctk.CTkButton(self.prompts_list_frame, text=prompt, font=('SF Display', 16), command=lambda: self.show_frame(self.editor_frame), anchor='w')
                self.prompt_btn.grid(row=i, column=0, padx=100, pady=5, sticky='nw')

        self.back_button = ctk.CTkButton(self.prompts_frame, text='back', font=small_big_buttons_font, command=lambda: self.show_frame(self.menu_frame), anchor='e')
        self.back_button.grid(row=0, column=0, pady=10, sticky='ne')


        self.show_frame(self.menu_frame)
        self.root.mainloop()

    # the actual functions
    def show_frame(self, frame):
        frame.tkraise()


TextEditor()
