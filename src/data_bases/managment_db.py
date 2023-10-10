import sqlite3 as sq


con = sq.connect("src/data_bases/data_bases.db")
con.execute("PRAGMA foreign_keys = 1")
cur = con.cursor()

def registration(data):
    try:
        con = sq.connect("src/data_bases/data_bases.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        res = (cur.execute("""SELECT login FROM accounts WHERE password = ?""", 
                    (data["password"])).fetchone())
        if res is None:
            try:    
                cur.execute("""INSERT INTO users (name, age) VALUES (?, ?)""", 
                            data["name"], data["age"])
                con.commit()
                user_id = cur.execute("""SELECT id FROM users WHERE name = ?""", 
                                    data["name"]).fetchone()
                cur.execute("""INSERT INTO accounts (id_user, login, password) 
                            VALUES (?, ?, ?)""", user_id[0], data["email"], 
                            data["password"])
                cur.execute("""INSERT INTO email (id_user, email_address)
                            VALUES (?, ?)""", user_id[0], data["email"])
                con.commit()
                con.close()
                return True
            except:
                print("Произошла ошибка при регистрации")
                con.close()
                return False
        else:
            print("Пользователь с такими данными уже зарегистрирован")
            con.close()
            return False
    except:
        print("Произошла ошибка при проверке данных в базе")

def entrains(log, passw):
    try:
        is_registered = cur.execute("""SELECT id_user FROM accounts WHERE
                                    login = ?, password = ?""", log, passw).fetchone()
        if is_registered is None:
            print("Данные введены неверно или пользователь не зарегистрирован")
            return False
        else:
            return True
    except:
        print("Произошла ошибка при входе в аккаунт")
        return False

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
con.close()
    