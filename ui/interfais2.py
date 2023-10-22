import tkinter 
from tkinter import messagebox
from tkinter import Spinbox
from tkinter.ttk import Progressbar
from tkinter import ttk
from tkinter import filedialog
from tkinter import Menu


def cliked():
    res = messagebox.askyesnocancel("Сдесь заголовок", "Сдесь текст")
    print(res)

def cliked_warning():
    messagebox.showwarning("Заголовок", "Текст")

def cliked_error():
    messagebox.showerror("Заголовок", "Текст")

def cliked_create():
    label.configure(text="Create new file")

window = tkinter.Tk()
window.geometry("700x500")
window.title("first_project")

btn = tkinter.Button(window, text="info", command=cliked).grid(column=0, row=0)
btn2 = tkinter.Button(window, text="warning", 
                      command=cliked_warning).grid(column=1, row=0)
btn3 = tkinter.Button(window, text="error", 
                      command=cliked_error).grid(column=2, row=0)
label = tkinter.Label(window, text="label", font=("arial", 16))
label.grid(column=0, row=5)
text_var = tkinter.IntVar()
text_var.set(20)
spin = Spinbox(window, from_=0, to=50, width=5, 
               textvariable=text_var).grid(column=0, row=1)

stile = ttk.Style()
stile.theme_use("default")
stile.configure("black.Horizontal.TProgressbar", backgraund = "black")
bar = Progressbar(window, length=300, style="black.Horizontal.TProgressbar")
bar["value"] = 80
bar.grid(column=0, row=2)

# file = filedialog.askopenfilename(filetypes=(("Text file", "*.txt"),("All file", "*.*")))
# print(file)
# dir = filedialog.askdirectory()
# print(dir)

menu_app = Menu(window)
new_item = Menu(menu_app, tearoff=0)

new_item.add_command(label="Create new file", command=cliked_create)
new_item.add_separator()
new_item.add_command(label="Changed file")
new_item.add_separator()
new_item.add_command(label="Save file")

menu_app.add_cascade(label="file", menu=new_item)
window.config(menu=menu_app)

# frame_control = ttk.Notebook(window)
# frame_one = ttk.Frame(frame_control)
# frame_control.add(frame_one, text="frame_1")
# frame_control.pack(expand=1, fill="both")

window.mainloop()