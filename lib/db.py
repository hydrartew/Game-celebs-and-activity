import sqlite3 as sq


# таблица с информацией о селебах
async def create_table_celebs():
    con = sq.connect('celebs.db')
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS celebrity(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(40) NOT NULL,  
                field_of_activity VARCHAR(20) NOT NULL, 
                creation_date VARCHAR(20))""")

    cur.close()
    con.close()


async def create_table_activity():
    con = sq.connect('celebs.db')
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS activity_game(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                text VARCHAR(40) NOT NULL,
                status VARCHAR(10) NOT NULL,
                creation_date VARCHAR(20))""")

    cur.close()
    con.close()
