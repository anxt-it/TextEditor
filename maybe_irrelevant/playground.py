import customtkinter as ctk

import time
from tkinter import messagebox, StringVar

# creating Tk window
root = ctk.CTk()
root.geometry("400x350")
root.title("Time Counter")

label1 = ctk.CTkLabel(root, text="This is a Timer", font=('SF Display', 52))
label1.pack()
label2 = ctk.CTkLabel(root, text=" ", font=('SF Display', 30))
label2.pack(pady=10)

def start_countdown(duration):
    def tick():
        nonlocal duration
        if duration < 0:
            messagebox.showinfo("countdown", "time's up")
            return
        h, rem = divmod(duration, 3600)
        m , s = divmod(rem, 60)
        label2.configure(text=f"{h:02}:{m:02}:{s:02}")
        duration -= 1
        root.after(1000, tick)
    tick()

def set_time():
    top = ctk.CTkToplevel(root)
    top.title("choose time")
    top.geometry("300x250")

    hour = StringVar()
    minute = StringVar()
    second = StringVar()
    # setting the default value as 0
    hour.set("00")
    minute.set("00")
    second.set("00")

    top.rowconfigure((0, 1, 2), weight=1)
    top.columnconfigure((0, 1, 2, 3, 4), weight=1)

    hour_entry = ctk.CTkEntry(top, textvariable=hour)
    hour_entry.grid(row=1, column=1, sticky='s')
    minute_entry = ctk.CTkEntry(top, textvariable=minute)
    minute_entry.grid(row=1, column=2, sticky='s')
    second_entry = ctk.CTkEntry(top, textvariable=second)
    second_entry.grid(row=1, column=3, sticky='s')

    def on_submit():
        top.destroy()
        duration = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
        start_countdown(duration)


    submit_btn = ctk.CTkButton(top, text="Submit time", command=on_submit)
    submit_btn.grid(row=2, column=1, columnspan=3)


btn1 = ctk.CTkButton(root, text="Set Time", font=('SF Display', 14), command=set_time)
btn1.pack(pady=100)

root.mainloop()
