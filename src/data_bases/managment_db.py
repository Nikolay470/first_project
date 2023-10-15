import sqlite3 as sq


# con = sq.connect("src/data_bases/data_bases.db")
# con.execute("PRAGMA foreign_keys = 1")
# cur = con.cursor()

def registration(data):
    connect = sq.connect("src/data_bases/data_bases.db")
    connect.execute("PRAGMA foreign_keys = 1")
    cursor = connect.cursor()
    user_is_registered = cursor.execute("""SELECT login FROM accounts WHERE
                                        password = ?""", [data["password"]]).fetchone()
    print(user_is_registered)
    if user_is_registered is None:
        cursor.execute("""INSERT INTO accounts(login, password)
                       VALUES (?, ?)""", [data["email"], data["password"]])
        connect.commit()
    
        user_id = cursor.execute("""SELECT id_user FROM accounts WHERE
                                 password = ?""", [data["password"]]).fetchone()
        
        cursor.execute("""INSERT INTO users (id, name, age)
                    VALUES (?, ?, ?)""", [user_id[0], data["name"], data["age"]])
        connect.commit()

        cursor.execute("""INSERT INTO email (id, email_address)
                       VALUES (?, ?)""", [user_id[0], data["email"]])
        connect.commit()
        return True
    else:
        print("Пользователь уже зарегистрирован")
        return False    


def entrains(log, passw):
    connect = sq.connect("src/data_bases/data_bases.db")
    connect.execute("PRAGMA foreign_keys = 1")
    cursor = connect.cursor()
    is_registered = cursor.execute("""SELECT id_user FROM accounts WHERE
                                login = ? AND password = ?""", [log, passw]).fetchone()
    if is_registered is None:
        print("Данные введены неверно или пользователь не зарегистрирован")
        return False
    else:
        return True
    

def changed_name_user(user_id, new_name):
    try:
        cur.execute("""UPDATE users SET name = ? WHERE id = ?""",
                    new_name, user_id)
        con.commit()
        return True
    except:
        print("Ошибка изменения имени")
        return False

def changed_age_user(user_id, new_age):
    try:
        age = cur.execute("""SELECT age FROM users WHERE id = ?""", 
                        user_id).fetchone()
        if age[0] is None:
            cur.execute("""UPDATE users SET age = ? WHERE id = ?""",
                        new_age, user_id)
            con.commit()
            return True
        else:
            return False
    except:
        print("Ошибка изменения возраста")
        return False

def changed_email_user(user_id, new_email):
    try:
        cur.execute("""UPDATE email SET email_address = ? WHERE id_user = ?""",
                    new_email, user_id)
        cur.execute("""UPDATE accounts SET login = ? WHERE id_user = ?""",
                    new_email, user_id)
        con.commit()
        return True
    except:
        print("Ошибка изменения email")
        return False
    
def changed_password_user(user_id, new_password):
    try:
        cur.execute("""UPDATE accounts SET password = ? WHERE id_user = ?""",
                    new_password, user_id)
        con.commit()
        return True
    except:
        print("Ошибка изменения пароля")
        return False
# con.commit()
# con.close()
    