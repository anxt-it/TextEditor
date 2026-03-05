from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title('text editor tutorial')
root.geometry('1200x700')

global open_status_name
open_status_name = False

my_frame = Frame(root)
my_frame.pack(pady=5)

# functions
def new_file():
    # delete everything in the text box
    my_text.delete("1.0", END)
    root.title("New file")
    status_bar.configure(text="New file")

    global open_status_name
    open_status_name=False


def open_file():
    my_text.delete("1.0", END)
    # Grab file name
    text_file = filedialog.askopenfilename(title="open file", initialdir="/Users/anatorevi/PycharmProjects/TextEditor/TestFolder", defaultextension='.txt', filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))

    # check to see if there is file name
    if text_file:
        # make file name global so we can access later
        global open_status_name
        open_status_name = text_file

    # update status bars and such
    name = text_file
    status_bar.configure(text=name)
    name = name.replace("/Users/anatorevi/PycharmProjects/TextEditor/TestFolder", "")
    root.title(f"{name}")

    # actually open the file
    text_file = open(text_file, 'r') #open the file
    stuff = text_file.read() # read whats in there and assign it to variable
    my_text.insert(END, stuff) # put it into the textbox
    text_file.close()

def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension='.txt', initialdir="/Users/anatorevi/PycharmProjects/TextEditor/TestFolder", title="save file", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    if text_file:
        # update status bars
        name = text_file
        status_bar.configure(text=name)
        name = name.replace("/Users/anatorevi/PycharmProjects/TextEditor/TestFolder", "")
        root.title(f"{name}")

        # save the file
        text_file = open(text_file, 'w')
        text_file.write(my_text.get(1.0, END))
        text_file.close()

def save_file():
    global open_status_name
    if open_status_name: # if theres something inside this variable we just save it like in the save_as
        text_file = open(open_status_name, 'w')
        text_file.write(my_text.get(1.0, END))
        text_file.close()
        status_bar.configure(text=f"Saved: {open_status_name}")
    else: # if the files doesnt already exist
        save_as_file()

# crete scroll bar for the text box
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

my_text = Text(my_frame, font=('SF Display', 16), undo=True, yscrollcommand=text_scroll.set)
my_text.pack()
text_scroll.configure(command=my_text.yview)


# create menu
my_menu = Menu(root)

# add file menu
file_menu = Menu(my_menu)
my_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New', command=new_file)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save As', command=save_as_file)
file_menu.add_command(label='Save', command=save_file)

file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.quit)

root.configure(menu=my_menu)


# add staus bar
status_bar = Label(root, text='Ready', anchor='e')
status_bar.pack(fill=X, side="bottom")



root.mainloop()