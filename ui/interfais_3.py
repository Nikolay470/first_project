import tkinter 
from tkinter import ttk

main_win = tkinter.Tk()
main_win.geometry("700x500")
main_win.title("first project")

frame_control = ttk.Notebook(main_win)
frame_one = ttk.Frame(frame_control)
frame_control.add(frame_one, text="frame one")
frame_two = ttk.Frame(frame_control)
frame_control.add(frame_two, text="frame two")
frame_three = ttk.Frame(frame_control)
frame_control.add(frame_three, text="frame three")

label_one = tkinter.Label(
    frame_one, 
    text="test_pad", 
    font=("arial", 16),
    padx=20, pady=20)
label_one.grid(column=0, row=0)

frame_control.pack(expand=1, fill="both")

main_win.mainloop()