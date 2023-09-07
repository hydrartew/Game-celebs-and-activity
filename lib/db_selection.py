import sqlite3 as sq
from random import randint

# проверка на запись в БД
async def random_names(field_of_activity: str, seq_number: int):
    con = sq.connect('celebs.db')
    cur = con.cursor()

    cur.execute('SELECT name FROM celebrity WHERE field_of_activity = ? ORDER BY RANDOM() LIMIT 10', (field_of_activity,))
    names = cur.fetchall()

    cur.close()
    con.close()

    output_text = ''

    names = [i for tup in names for i in tup]  # список кортежей в список
    for i, name in enumerate(names):
        if '(' in name:
            bold_text = name[:name.index('(')]
            end_text = name[name.index('('):]
            name = f'<b>{bold_text}</b>{end_text}'
        else:
            name = f'<b>{name}</b>'

        output_text += f'{i + 1 + seq_number}. {name}\n\n'

    return output_text


async def full_random(seq_number: int):
    con = sq.connect('celebs.db')
    cur = con.cursor()

    cur.execute('SELECT * FROM celebrity ORDER BY RANDOM() LIMIT 10')
    random_celebs = cur.fetchall()

    cur.close()
    con.close()

    output_text = ''

    for i, celeb in enumerate(random_celebs):
        name = celeb[1]
        field_of_activity = celeb[2]

        if '(' in name:
            bold_text = name[:name.index('(')]
            end_text = name[name.index('('):]
            name = f'<b>{bold_text}</b>{end_text}'
        else:
            name = f'<b>{name}</b>'

        output_text += f'{i + 1 + seq_number}. {name}\n' \
                       f'<i>Категория: {field_of_activity}</i>\n\n'

    return output_text


async def select_random_words():
    con = sq.connect('celebs.db')
    cur = con.cursor()

    cur.execute('SELECT text FROM activity_game WHERE status = "new" ORDER BY RANDOM() LIMIT 3')
    random_words = cur.fetchall()

    output_text = ''

    for i, word in enumerate(random_words):
        cur.execute("UPDATE activity_game SET status = 'used' WHERE text = ?", (word[0],))
        con.commit()

        count_points = randint(2, 5)
        if 2 <= count_points <= 4:
            points = f'{count_points} балла'
        elif count_points == 5:
            points = f'{count_points} баллов'
        else:
            points = f'1 балл'

        output_text += f'{i + 1}. {word[0]}\n' \
                       f'<i>({points})</i>\n\n'

    cur.close()
    con.close()

    return output_text
