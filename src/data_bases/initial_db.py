import sqlite3 as sq

con = sq.connect("src/data_bases/data_bases.db")
con.execute("PRAGMA foreign_keys = 1")
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users 
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                name TEXT NOT NULL,
                age INTEGER 
            )
            """)
cur.execute("""CREATE TABLE IF NOT EXISTS accounts (
               id_user INTEGER NOT NULL,
               login TEXT NOT NULL,
               password TEXT NOT NULL,
               FOREIGN KEY (id_user) REFERENCES users(id) ON DELETE CASCADE 
               ON UPDATE CASCADE
)""")
cur.execute("""CREATE TABLE IF NOT EXISTS email (
                id_user INTEGER NOT NULL,
                email_address TEXT NOT NULL,
                FOREIGN KEY (id_user) REFERENCES users(id) ON DELETE CASCADE
                ON UPDATE CASCADE
)""")

con.commit()
con.close()