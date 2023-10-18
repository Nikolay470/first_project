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
favorites_books = dict()
favorites_music = dict()
id_current_user = 0 # переменная для хранения id текущего пользователя
result_call_func = 0
id = 1

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
    select_user = int(input("1.Вход 2.Регистрация 3.Выход\n"))
    result = False
    if select_user == 1:
        login = input("Введите логин:\n")
        password = input("Введите пароль:\n")
        result_entrains = manag_db.entrains(login, password)
        if result_entrains[result_call_func]:
            id_current_user = result_entrains[id]
            result = True
            iteration = False
        else:
            print("Произошла ошибка входа")
    elif select_user == 2:
        data_user = dict()
        name_user = input("Введите ваше имя:\n")
        data_user["name"] = name_user

        age_user = input("Введите ваш возраст:\n")
        data_user["age"] = age_user

        email_user = input("Введите почту. Этот адрес будет вашим логином:\n")
        data_user["email"] = email_user

        password_user = input("Придумайте пароль:\n")
        data_user["password"] = password_user

        result_registration = manag_db.registration(data_user)
        if result_registration[result_call_func]:
            print("Регистрация прошла успешно!")
            id_current_user = result_registration[id]
            favorites_books[id_current_user] = []
            favorites_music[id_current_user] = []

            result = True
            iteration = False
        else:
            print("Произошла ошибка регистрации\n")
    elif select_user == 3:
        iteration = False        
    else:
        print("Выберите действие\n")

if result:
    iteration = True    

    while iteration:
        command = int(input("\nВыберите действие\n"
                        + "1. Что почитать?\n2. Интересные истории\n"
                        + "3. Послушать музыку\n4. Фото с котиками\n"
                        + "5. Изменить учетные данные\n6. Завершить\n"))
        if command == 1:
            command = int(input("Посмотреть в избранном\n1.Да 2.Нет\n"))
            if command == 1:
                func.print_list(favorites_books[id_current_user])
                command = int(input("Выберите книгу\nВернутся к меню (введите 0)"))
                if command == 0:
                    iteration = True
                else:
                    selection_book = favorites_books[id_current_user][command - 1]
                    func.description_book(selection_book, description)
                    command = int(input("1. Прочитать\n"
                                        +"2. Удалить из избранного\n"
                                        +"3. Вернуться к меню\n"))
                    if command == 1:
                        print("Открывается электронный вариант книги\n")
                        iteration = False
                    elif command == 2:
                        try:
                            favorites_books[id_current_user].remove(selection_book)
                            print("Книга удалена из избранного")
                        except:
                            print("Удаление завершилось с ошибкой")
                    elif command == 3:
                        iteration = True
            elif command == 2:    
                func.print_list(books)
                command = int(input("Какую книгу вы выбрали?\n"))
                selection_book = books[command - 1]
                func.description_book(selection_book, description)
                command = int(input("1. Прочитать\n2. В избранное\n"
                                    +"3. Вернуться к меню\n"))
                if command == 1:
                    print("Открывается электронный вариант книги\n")
                    iteration = False
                elif command == 2:
                    favorites_books[id_current_user].append(selection_book)
                    print("Книга добавлена в избранное")
                elif command == 3:
                    iteration = True
        elif command == 2:
            func.print_list(storis)
            command = int(input("Какую историю вы хотите прочитать?\n"))
            selection_storis = storis[command - 1]
            print("Показываем текст истории")

        elif command == 3:
            command = int(input("Хотите посмотреть избранные песни?\n"
                                +"1.Да 2.Нет"))
            if command == 1:
                func.print_list(favorites_music[id_current_user])
                command = int(input("Выберите песню\n"
                                    +"Вернуться к меню (введите 0)\n"))
                if command == 0:
                    iteration = True
                else:
                    selection_music = favorites_music[id_current_user][command - 1]
                    func.music_decription(selection_music, description)
                    command = int(input("1.Скачать 2. Прослушать\n"
                                        +"3.Удалить из избранного" 
                                        +"4.Вернуться к меню (введите 0)"))
                    if command == 0:
                        iteration = True
                    elif command == 1:
                        print("Песня скачивается...")
                    elif command == 2:
                        print("Начинается проигрывание песни...")
                    elif command == 3:
                        try:
                            favorites_music[id_current_user].remove(selection_music)
                            print("Песня удалена")
                        except:
                            print("Удаление завершилось с ошибкой")
            elif command == 2:                    
                func.print_list(play_list)
                command = int(input("Какаю песню вы выбрали?\n"))
                selection_music = play_list[command - 1]
                func.music_decription(selection_music, description)
                command = int(input("1. Слушать\n2. Скачать\n3. В избранное\n"))
                if command == 1:
                    print("Начинается пролушивание")
                elif command == 2:
                    print("Начинается скачивание...")
                elif command == 3:
                    favorites_music[id_current_user].append(selection_music)
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
            command = int(input("Что вы хотите изменить?\n"
                                +"1. Имя\n2. Возраст\n3. Email\n4. Пароль\n"
                                +"5. Вернутся к меню\n"))
            result_changed = False
            error_text = "Изменение завершилось с ошибкой"
            if command ==1:
                new_name_user = input("Введите новое имя: ")
                result_changed = manag_db.changed_name_user(id_current_user, new_name_user)
                if result_changed:
                    print("Имя успешно заменено")
                else:
                    print(error_text)
            elif command == 2:
                new_age_user = int(input("Введите новый возраст: "))
                result_changed = manag_db.changed_age_user(id_current_user, 
                                                           new_age_user)
                if result_changed:
                    print("Возраст изменен успешно")
                else:
                    print(error_text)
            elif command == 3:
                new_email_user = input("Введите новый email: ")
                result_changed = manag_db.changed_email_user(id_current_user,
                                                             new_email_user)
                if result_changed:
                    print("Email успешно изменен")
                else:
                    print(error_text)
            elif command == 4:
                new_password_user = input("Введите новый пароль: ")
                result_changed = manag_db.changed_password_user(id_current_user,
                                                                new_password_user)
                if result_changed:
                    print("Пароль успешно изменен")
                else:
                    print(error_text)
            elif command == 5:
                iteration = True
        elif command == 6:
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