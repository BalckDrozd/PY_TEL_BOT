import sqlite3
from create_bot import bot
from random import randint


# Пользовательская функция изменения регистра
def myfunc(s):
    return s.lower()


def sql_start():
    global db, cur
    db = sqlite3.connect('BD_Film_lordfilm.db')
    db.create_function("mylower", 1, myfunc)
    cur = db.cursor()
    if db:
        print(f'База данных BD_Film_lordfilm.db подключена')


async def find_Film_name(message):
    name_list = []
    year_list = []
    kp_rate_list = []
    imdb_rate_list = []
    link_film_list = []
    link_img_list = []
    opisanie_list = []

    # Поиск названия фильма
    for name1 in cur.execute('SELECT NAME FROM BD_Film_lordfilm WHERE mylower(NAME) LIKE ?',
                             ('%' + message.text.lower() + '%',)):
        print(name1)
        name_list.append(name1[0])
    print(len(name_list))
    for year1 in cur.execute('SELECT YEAR FROM BD_Film_lordfilm WHERE mylower(NAME) LIKE ?',
                             ('%' + message.text.lower() + '%',)):
        print(year1)
        year_list.append(year1[0])
    print(len(year_list))
    for kp_rate1 in cur.execute('SELECT KP_RATE FROM BD_Film_lordfilm WHERE mylower(NAME) LIKE ?',
                                ('%' + message.text.lower() + '%',)):
        print(kp_rate1)
        kp_rate_list.append(kp_rate1[0])
    print(len(kp_rate_list))
    for imdb_rate1 in cur.execute('SELECT IMDB_RATE FROM BD_Film_lordfilm WHERE mylower(NAME) LIKE ?',
                                  ('%' + message.text.lower() + '%',)):
        print(imdb_rate1)
        imdb_rate_list.append(imdb_rate1[0])
    print(len(imdb_rate_list))
    for link_film1 in cur.execute('SELECT LINK_FILM FROM BD_Film_lordfilm WHERE mylower(NAME) LIKE ?',
                                  ('%' + message.text.lower() + '%',)):
        print(link_film1)
        link_film_list.append(link_film1[0])
    print(len(link_film_list))
    for link_img1 in cur.execute('SELECT LINK_IMG FROM BD_Film_lordfilm WHERE mylower(NAME) LIKE ?',
                                 ('%' + message.text.lower() + '%',)):
        print(link_img1)
        link_img_list.append(link_img1[0])
    print(len(link_img_list))
    for opisanie1 in cur.execute('SELECT OPISANIE FROM BD_Film_lordfilm WHERE mylower(NAME) LIKE ?',
                                 ('%' + message.text.lower() + '%',)):
        print(opisanie1)
        print(len(opisanie1[0]))
        opisanie_list.append(opisanie1[0])
    print(len(opisanie_list))

    print('Поиск закончен')

    for i in range(len(name_list)):
        captions = f'Название фильма: {name_list[i]}\nГод: {year_list[i]}\nРейтинг КП: {kp_rate_list[i]}\nРейтинг IMDB: {imdb_rate_list[i]}\nОписание: {opisanie_list[i]}\nСсылка на фильм: {link_film_list[i]}'
        print(len(captions))
        if len(captions) > 1023:
            captions = f'Название фильма: {name_list[i]}\nГод: {year_list[i]}\nРейтинг КП: {kp_rate_list[i]}\nРейтинг IMDB: {imdb_rate_list[i]}\nОписание: {opisanie_list[i][:-(len(captions) - 1024)]}\nСсылка на фильм: {link_film_list[i]}'

        await bot.send_photo(message.from_user.id, photo=link_img_list[i], caption=captions)

    await bot.send_message(message.from_user.id, f'Нашлось {len(name_list)} совпадений')


async def find_Film_random(message):
    r = randint(1, 37521)
    rnd_film = cur.execute(
        'SELECT NAME, YEAR, KP_RATE, IMDB_RATE, LINK_FILM, LINK_IMG, OPISANIE FROM BD_Film_lordfilm WHERE ID == ?',
        (r,))
    sfilm = rnd_film.fetchall()[0]
    capt = f'Название фильма: {sfilm[0]}\nГод: {sfilm[1]}\nРейтинг КП: {sfilm[2]}\nРейтинг IMDB: {sfilm[3]}\nОписание: {sfilm[6]}\nСсылка на фильм: {sfilm[4]}'
    if len(capt) > 1023:
        capt = f'Название фильма: {sfilm[0]}\nГод: {sfilm[1]}\nРейтинг КП: {sfilm[2]}\nРейтинг IMDB: {sfilm[3]}\nОписание: {sfilm[6][:-(len(capt) - 1024)]}\nСсылка на фильм: {sfilm[4]}'
    await bot.send_photo(message.from_user.id, photo=sfilm[5],
                         caption=capt)
