import sqlite3 as sq

con = sq.connect("data_bases.db")
con.execute("PRAGMA foreign_keys = 1")
cur = con.cursor()

def registration(data):
    try:    
        cur.execute("""INSERT INTO users (name, age) VALUES (?, ?)""", 
                    data["name"], data["age"])
        con.commit()
        user_id = cur.execute("""SELECT id FROM users WHERE name = ?""", 
                            data["name"]).fetchone()
        cur.execute("""INSERT INTO accounts (id_user, login, password) 
                    VALUES (?, ?, ?)""", user_id[0], data["email"], data["password"])
        cur.execute("""INSERT INTO email (id_user, email_address)
                    VALUES (?, ?)""", user_id[0], data["email"])
        con.commit()
        return True
    except:
        return False

def is_user_registered(log, passw):
    user_password = cur.execute("""SELECT password FROM acconts 
                          WHERE login = ?""", log).fetchone()
    if user_password[0] is None:
        print("Логин указан неверно или такого пользователя не существует :(")
        return False
    else:
        result = passw.equals(user_password[0])
        if result:
            return True
        else:
            return False

def changed_name_user(user_id, new_name):
    try:
        cur.execute("""UPDATE users SET name = ? WHERE id = ?""",
                    new_name, user_id)
        con.commit()
        return True
    except:
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
        return False
    
def changed_password_user(user_id, new_password):
    try:
        cur.execute("""UPDATE accounts SET password = ? WHERE id_user = ?""",
                    new_password, user_id)
        con.commit()
        return True
    except:
        return False
# con.commit()
con.close()
    