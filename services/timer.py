import customtkinter

def switch_event():
    print(f"Switch toggled, current value: {switch_var.get()}")

# Create the main window
root_tk = customtkinter.CTk()

# Define a variable to track the switch state
switch_var = customtkinter.StringVar(value="off")

# Create the switch widget
switch_1 = customtkinter.CTkSwitch(
    master=root_tk,
    command=switch_event,
    variable=switch_var,
    onvalue="on",
    offvalue="off",
    text="Toggle me"
)
switch_1.pack(pady=10) # Place the switch in the window

# Start the application event loop
root_tk.mainloop()
