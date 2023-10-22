import tkinter as tk
from tkinter.ttk import Combobox
from tkinter.ttk import Checkbutton
from tkinter.ttk import Radiobutton
from tkinter import scrolledtext

def cliked():
    greetings = f"Привет {text_input.get()}"
    label.configure(text=greetings)

def cliked_box():
    label.configure(text=f"Box = {box.get()}")

def cliked_rd_button1():
    label.configure(text=selected_rd.get())

def cliked_rd_button2():
    label.configure(text="Second rd_button")

def cliked_rd_button3():
    label.configure(text="There rd_button")

window = tk.Tk()
window.title("Первое приложение")
window.geometry("700x500")
label = tk.Label(window, text="hello, nikolay", font=("arial bold", 16))
label.grid(column=0, row=0)

button = tk.Button(window, text="Press my", bg="green", fg="black", command=cliked_box)
button.grid(column=0, row=1)

text_input = tk.Entry(window, width=20, font=("arial bold", 16))
text_input.grid(column=0, row=2)
text_input.focus()

box = Combobox(window)
box["values"] = (1, 2, 3, 4, 5, "hello")
box.grid(column=0, row=3)
box.current(3)

check_state = tk.BooleanVar()
check_state.set(False)
check_btn = Checkbutton(window, text="Выбор", variable=check_state)
check_btn.grid(column=0, row=4)

# check = tk.IntVar()
# check.set(1)
selected_rd = tk.IntVar()
rd_button1 = Radiobutton(window, text="Первый", value=1, 
                         command=cliked_rd_button1, variable= selected_rd)
rd_button1.grid(column=1, row=0)
rd_button2 = Radiobutton(window, text="Второй", value=2, 
                         command=cliked_rd_button1, variable= selected_rd)
rd_button2.grid(column=1, row= 1)
rd_button3 = Radiobutton(window, text="Третий", value=3, 
                         command=cliked_rd_button1, variable= selected_rd)
rd_button3.grid(column=1, row=2)

text_scrol = scrolledtext.ScrolledText(window, width = 40, height= 10)
text_scrol.grid(column=0, row=5)

text_scrol.insert(tk.INSERT, "Какой то текст")
# btn_text_scrol = tk.Button(text_scrol, text="button", font=("arial", 16))
# btn_text_scrol.grid(column=0, row=0)
text_scrol.delete(0.0, tk.END)
window.mainloop()
