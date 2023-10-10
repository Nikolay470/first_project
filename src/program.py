import datetime
import json
import methods.functions as func
import data_bases.managment_db as manag_db
########################################
# data
storis = list()
books = list()
description = dict()
images = list()
play_list = list()
favorites_books = list()
favorites_music = list()

with open("src/data_json/storis.json", "r") as st:
    storis = json.loads(st.read())
with open("src/data_json/books.json", "r") as b:
    books = json.loads(b.read())
with open("src/data_json/description.json", "r") as des:
    description = json.loads(des.read())
with open("src/data_json/images.json", "r") as img:
    images = json.loads(img.read())
with open("src/data_json/play_list.json", "r") as p_list:
    play_list = json.loads(p_list.read())
with open("src/data_json/favorites_books.json", "r") as fav_book:
    favorites_books = json.loads(fav_book.read())
with open("src/data_json/favorites_music.json", "r") as fav_music:
    favorites_music = json.loads(fav_music.read())




#######################################
to_hour = datetime.datetime.today().hour
if to_hour >= 6 and to_hour <= 11:
    print("Доброе утро")
elif to_hour > 11 and to_hour <= 18:
    print("Добрый день")
elif to_hour > 18 and to_hour <= 22:
    print("Добрый вечер")
else:
    print("Доброй ночи")

iteration = True    
while iteration:
    select_user = int(print("1. Вход 2. Регистрация\n"))
    result = False
    if select_user == 1:
        login = print("Введите логин:\n")
        password = print("Введите пароль:\n")
        if manag_db.entrains(login, password):
            result = True
            iteration = False
    elif select_user == 2:
        data_user = dict()
        name_user = print("Введите ваше имя:\n")
        data_user["name"] = name_user

        age_user = print("Введите ваш возраст:\n")
        data_user["age"] = age_user

        email_user = print("Придумайте логин:\n")
        data_user["email"] = email_user

        password_user = print("Придумайте пароль:\n")
        data_user["password"] = password_user

        if manag_db.registration(data_user):
            print("Регистрация прошла успешно!")
            result = True
            iteration = False
    else:
        print("Выберите действие\n")
if result:
    iteration = True    

    while iteration:
        command = int(input("\nВыберите действие\n"
                        + "1. Что почитать?\n2. Интересные истории\n"
                        + "3. Послушать музыку\n4. Фото с котиками\n"
                        + "5. Завершить\n"))
        if command == 1:
            func.print_list(books)
            command = int(input("Какую книгу вы выбрали?\n"))
            selection_book = books[command - 1]
            func.description_book_and_film(selection_book, books)
            command = int(input("1. Прочитать\n2. В избранное\n"))
            if command == 1:
                print("Открывается электронный вариант книги\n")
                iteration = False
            elif command == 2:
                favorites_books.append(selection_book)
                print("Книга добавлена в избранное")
            else:
                print("Укажите номер действия\n")
                                
        elif command == 2:
            func.print_list(storis)
            command = int(input("Какую историю вы хотите прочитать?\n"))
            selection_storis = storis[command - 1]
            print("Показываем текст истории")

        elif command == 3:
            func.print_list(play_list)
            command = int(input("Какаю песню вы выбрали?\n"))
            selection_music = play_list[command - 1]
            func.music_decription(selection_music, play_list)
            command = int(input("1. Слушать\n2. Скачать\n3. В избранное\n"))
            if command == 1:
                print("Начинается пролушивание")
            elif command == 2:
                print("Начинается скачивание...")
            elif command == 3:
                favorites_music.append(selection_music)
                print("Песня добавлена в избранное")
            else:
                print("Введите номер действия")
        elif command == 4:
            swap = True
            count = 0
            selection = ""
            
            while swap:
                func.print_image(images[count])
                count += 1
                selection = input("Показать следующею?\nДа\nНет\n").lower()

                if count == len(images) or selection == "нет":
                    swap = False
            
            print("Спасибо за просмотр")
            command = int(input("1. Завершить\n2. Вернутся к меню\n"))
            if command == 1:
                iteration = False
        elif command == 5:
            iteration = False
        else:
            print("Выберите действие")

    with open("src/data_json/favorites_books.json", "w") as fav_book:
        fav_book.write(json.dumps(favorites_books))
    with open("src/data_json/favorites_music.json", "w") as fav_music:
        fav_music.write(json.dumps(favorites_music))
    print("Обязательно заходите еще раз!")
else:
    print("Что пошло не так")