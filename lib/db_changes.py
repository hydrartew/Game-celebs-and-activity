import datetime
import sqlite3 as sq


# создание нового пользователя
async def add_celeb(name: str, field_of_activity: str):
    con = sq.connect('celebs.db')
    cur = con.cursor()

    dt = datetime.datetime.now()
    date_now = dt.strftime('%d.%m.%Y %H:%M:%S')

    try:
        first_name_last_name = name.split()
        first_name_last_name = first_name_last_name[0] + ' ' + first_name_last_name[1] + '%'

        cur.execute("SELECT * FROM celebrity WHERE name LIKE ?", (first_name_last_name,))
        celeb = cur.fetchone()

        if celeb is None:
            cur.execute('INSERT INTO celebrity VALUES (NULL, ?, ?, ?)', (name, field_of_activity, date_now))
            con.commit()

    except:
        cur.execute('INSERT INTO celebrity VALUES (NULL, ?, ?, ?)', (name, field_of_activity, date_now))
        con.commit()

    cur.close()
    con.close()


async def add_text(text: str):
    con = sq.connect('celebs.db')
    cur = con.cursor()

    dt = datetime.datetime.now()
    date_now = dt.strftime('%d.%m.%Y %H:%M:%S')

    cur.execute("SELECT text FROM activity_game WHERE text = ?", (text,))
    sel_text = cur.fetchone()

    if sel_text is None:
        cur.execute('INSERT INTO activity_game VALUES (NULL, ?, ?, ?)', (text, 'new', date_now))
        con.commit()

    cur.close()
    con.close()
