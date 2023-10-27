import tkinter
from tkinter import ttk
from tkinter import messagebox

def create_frame(frame_text, name_notebook):
    new_frame = ttk.Frame(name_notebook)
    name_notebook.add(new_frame, text=frame_text)
    return new_frame
    

def clicked_exit():
    select_user = messagebox.askokcancel(
        "До свидания!",
        "Возвращайся снова, я тебя очень жду :)"
        )
    if select_user:
        main_win.destroy()

main_win = tkinter.Tk()
main_win.title("first project")
main_win.geometry("1200x920")
main_win.resizable(width=False, height=False)

frame_control = ttk.Notebook(main_win)

frame_books = create_frame("Книги", frame_control)
frame_storis = create_frame("Интересные истории", frame_control)
frame_music = create_frame("Музыка", frame_control)
frame_foto_cat = create_frame("Фото с котиками", frame_control)
frame_changed_data_user = create_frame("Изменение учетных данных", frame_control)

frame_control.pack(expand=1, fill="both")

menu_app = tkinter.Menu(main_win)
new_item = tkinter.Menu(menu_app, tearoff=0)
new_item.add_command(label="Сменить пользователя")
new_item.add_command(label="Выйти", command=clicked_exit)

menu_app.add_cascade(label="Меню", menu=new_item)
main_win.config(menu=menu_app)

canva = tkinter.Canvas(frame_books, bg="white", )
canva.pack(expand=True, fill="both")

window_out_content = tkinter.Canvas(
    canva, 
    width=500, 
    height=600, 
    bg="green",
    relief="raised",
    borderwidth="10")
window_out_content.place(x=330, y=50)

main_win.mainloop()