# import tkinter
# from tkinter import ttk

# main_win = tkinter.Tk()
# main_win.title("first project")
# main_win.geometry("700x500")

# # canva = tkinter.Canvas(bg="white", width=400, height=400)
# # canva.pack(anchor="center", expand=1)
# style_btn = ttk.Style()
# style_btn.configure(
#     "My.TButton", 
#     bg=[("active", "green"),("pressed", "red")],
#     fg=[("active", "red"), ("pressed", "black")],
#     borderwidth="3", 
#     borderradius="10"
#     )

# button = ttk.Button(main_win, text="test_button", style="My.TButton")

# button.pack(anchor="center", expand=1)
# main_win.mainloop()

import tkinter as tk
from tkinter import ttk
 
root = tk.Tk()
 
style = ttk.Style()
style.configure('my.TButton', font=('Helvetica', 12, 'bold'), borderwidth='5', borderradius='50')
 
my_button = ttk.Button(root, style='my.TButton', text="Click Me!")
style.map('my.TButton', foreground=[('pressed', 'red'), ('active', 'green')], background=[('pressed', '!disabled', 'black'), ('active', 'white')])
 
my_button.pack(pady=20, padx=20)
 
root.mainloop()