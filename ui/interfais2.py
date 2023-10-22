import tkinter 
from tkinter import messagebox
from tkinter import Spinbox
from tkinter.ttk import Progressbar
from tkinter import ttk
from tkinter import filedialog

def cliked():
    res = messagebox.askyesnocancel("Сдесь заголовок", "Сдесь текст")
    print(res)

def cliked_warning():
    messagebox.showwarning("Заголовок", "Текст")

def cliked_error():
    messagebox.showerror("Заголовок", "Текст")

window = tkinter.Tk()
window.geometry("700x500")
window.title("first_project")

btn = tkinter.Button(window, text="info", command=cliked).grid(column=0, row=0)
btn2 = tkinter.Button(window, text="warning", 
                      command=cliked_warning).grid(column=1, row=0)
btn3 = tkinter.Button(window, text="error", 
                      command=cliked_error).grid(column=2, row=0)

text_var = tkinter.IntVar()
text_var.set(20)
spin = Spinbox(window, from_= 0, to= 50, width= 5, 
               textvariable= text_var).grid(column=0, row=1)

stile = ttk.Style()
stile.theme_use("default")
stile.configure("black.Horizontal.TProgressbar", backgraund = "black")
bar = Progressbar(window, length=300, style="black.Horizontal.TProgressbar")
bar["value"] = 80
bar.grid(column=0, row=2)

file = filedialog.askopenfilename()

window.mainloop()