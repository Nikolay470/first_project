author = 0
executor = 0
year_releaze = 1
short_description = 2
album = 2

def print_list(spisok):
    for i in range(len(spisok)):
        print(f"{i + 1}. \"{spisok[i]}\"\n")

def print_image(img):
    print(img)

def description_book(name_book, data_structure):
    data = data_structure[name_book]
    print(f"Автор: {data[author]}\nГод релиза: {data[year_releaze]}\n" 
          +f"Описание: {data[short_description]}")

def music_decription(music, data_structure):
    data = data_structure[music]
    print(f"Исполнитель: {data[executor]}\n"
          + f"Год релиза: {data[year_releaze]}\n"
          + f"Альбом: {data[album]}")