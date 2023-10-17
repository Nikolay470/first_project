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
        connect.close()
        return [True, user_id]
    else:
        print("Пользователь уже зарегистрирован")
        connect.close()
        return [False]    


def entrains(log, passw):
    connect = sq.connect("src/data_bases/data_bases.db")
    connect.execute("PRAGMA foreign_keys = 1")
    cursor = connect.cursor()
    user_id = cursor.execute("""SELECT id_user FROM accounts WHERE
                                login = ? AND password = ?""", [log, passw]).fetchone()
    if user_id is None:
        print("Данные введены неверно или пользователь не зарегистрирован")
        connect.close()
        return [False]
    else:
        connect.close()
        return [True, user_id]
    

def changed_name_user(user_id, new_name):
    connect = sq.connect("src/data_bases/data_bases.db")
    connect.execute("PRAGMA foreign_keys = 1")
    cursor = connect.cursor()

    cursor.execute("""UPDATE users SET name = ? WHERE id = ?""", 
                   [new_name, user_id])
    connect.commit()
    connect.close()
    return True

def changed_age_user(user_id, new_age):
    connect = sq.connect("src/data_bases/data_bases.db")
    connect.execute("PRAGMA foreign_keys = 1")
    cursor = connect.cursor()

    cursor.execute("""UPDATE users SET age = ? WHERE id = ?""",
                   [new_age, user_id])
    connect.commit()
    connect.close()
    return True

def changed_email_user(user_id, new_email):
    connect = sq.connect("src/data_bases/data_bases.db")
    connect.execute("PRAGMA foreign_keys = 1")
    cursor = connect.cursor()

    cursor.execute("""UPDATE email SET email_address = ? WHERE id = ?""",
                   [new_email, user_id])
    connect.commit()

    cursor.execute("""UPDATE accounts SET login = ? WHERE id_user = ?""",
                   [new_email, user_id])
    connect.commit()
    connect.close()
    return True

    
def changed_password_user(user_id, new_password):
    connect = sq.connect("src/data_bases/data_bases.db")
    connect.execute("PRAGMA foreign_keys = 1")
    cursor = connect.cursor()

    cursor.execute("""UPDATE accounts SET password = ? WHERE id_user = ?""",
                   [new_password, user_id])
    connect.commit()
    connect.close()
    