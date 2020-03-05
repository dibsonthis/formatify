from replace_functions import modify, copy_text, paste_text, copy_to_clipboard, get_clipboard_data, clear_clipboard, undo
import time

import tkinter as tk
import tkinter.font as font

def get_font(family, size, weight='normal'):
    return font.Font(family=family, size=size, weight=weight)

def on_enter(event=None, function='upper'):
    data_preview = modify(function, paste=False)
    preview_label.config(text=data_preview['modified_data'])

def on_exit(event):
    pass

def tk_modify(function):
    root.withdraw()
    time.sleep(0.1)
    modify(function)
    root.deiconify()
    time.sleep(0.01)
    clear_clipboard()

root = tk.Tk()

windowWidth = root.winfo_screenwidth()
windowHeight = root.winfo_screenheight()

custom_margin = 70
root_height = int(windowHeight * 0.1)
y_pos = windowHeight - root_height - custom_margin

root.title("Formatify")
root.wm_attributes("-topmost", 1)
root.config(bg="skyblue")

left_frame = tk.Frame(root, width=200, height=400)
left_frame.grid(row=0, column=0, padx=10, pady=5)

right_frame = tk.Frame(root, width=300, height=200)
right_frame.grid(row=0, column=1, padx=10, pady=5)

function_buttons = tk.Frame(left_frame)
function_buttons.grid(row=0, column=0, padx=10, pady=5)

button_font = get_font('Arial', 11)
preview_label_font = get_font('Arial', 8)

preview_label = tk.Label(right_frame, text="Preview Window", font=preview_label_font)
preview_label.grid(row=0,column=0, sticky='nesw')

upper = tk.Button(function_buttons, text="UPPERCASE", command= lambda: tk_modify('upper'), font=button_font)
upper.grid(row=0, column=0, ipadx=5, pady=5)
upper.bind("<Enter>", lambda event: on_enter(event, function='upper'))
upper.bind("<Leave>", on_exit)

lower = tk.Button(function_buttons, text="lowercase", command= lambda: tk_modify('lower'), font=button_font)
lower.grid(row=0, column=1, ipadx=5, pady=5)
lower.bind("<Enter>", lambda event: on_enter(event, function='lower'))
lower.bind("<Leave>", on_exit)

cap_all = tk.Button(function_buttons, text="Cap All", command= lambda: tk_modify('cap_all'), font=button_font)
cap_all.grid(row=0, column=2, ipadx=7, pady=5)
cap_all.bind("<Enter>", lambda event: on_enter(event, function='cap_all'))
cap_all.bind("<Leave>", on_exit)

snake_case = tk.Button(function_buttons, text="snake_case", command= lambda: tk_modify('snake_case'), font=button_font)
snake_case.grid(row=1, column=0, ipadx=5, pady=5)
snake_case.bind("<Enter>", lambda event: on_enter(event, function='snake_case'))
snake_case.bind("<Leave>", on_exit)

camel_case = tk.Button(function_buttons, text="CamelCase", command= lambda: tk_modify('camel_case'), font=button_font)
camel_case.grid(row=2, column=0, ipadx=5, pady=5)
camel_case.bind("<Enter>", lambda event: on_enter(event, function='camel_case'))
camel_case.bind("<Leave>", on_exit)

root.mainloop()