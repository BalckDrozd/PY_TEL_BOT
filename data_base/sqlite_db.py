import sqlite3, time
from create_bot import dp, bot
from random import randint
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



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

    #Подключаем хромдрайвер
    ser = Service('/home/blackdrozd/PycharmProjects/pythonTB/chromedriver')
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    # options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(service=ser, options=options)

    #Поиск названия фильма
    for name1 in cur.execute('SELECT NAME FROM BD_Film_lordfilm WHERE mylower(NAME) LIKE ?',
                             ('%' + message.text.lower() + '%',)):
        name_list.append(name1[0])
    for year1 in cur.execute('SELECT YEAR FROM BD_Film_lordfilm WHERE mylower(NAME) LIKE ?',
                             ('%' + message.text.lower() + '%',)):
        year_list.append(year1[0])
    for kp_rate1 in cur.execute('SELECT KP_RATE FROM BD_Film_lordfilm WHERE mylower(NAME) LIKE ?',
                                ('%' + message.text.lower() + '%',)):
        kp_rate_list.append(kp_rate1[0])
    for imdb_rate1 in cur.execute('SELECT IMDB_RATE FROM BD_Film_lordfilm WHERE mylower(NAME) LIKE ?',
                                  ('%' + message.text.lower() + '%',)):
        imdb_rate_list.append(imdb_rate1[0])
    for link_film1 in cur.execute('SELECT LINK_FILM FROM BD_Film_lordfilm WHERE mylower(NAME) LIKE ?',
                                  ('%' + message.text.lower() + '%',)):
        # driver.get(link_film1[0])
        # time.sleep(2)
        link_film_list.append(link_film1[0])
    for link_img1 in cur.execute('SELECT LINK_IMG FROM BD_Film_lordfilm WHERE mylower(NAME) LIKE ?',
                                 ('%' + message.text.lower() + '%',)):
        link_img_list.append(link_img1[0])
    for opisanie1 in cur.execute('SELECT OPISANIE FROM BD_Film_lordfilm WHERE mylower(NAME) LIKE ?',
                                 ('%' + message.text.lower() + '%',)):
        opisanie_list.append(opisanie1[0])

    # for time_film in link_film_list:
    #     driver.get(time_film)
    #     # time.sleep(2)
    #     # driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
    #     # element2 = driver.find_element(By.XPATH, """/html/body/div/pjsdiv/pjsdiv[1]/video""")
    #     print(element2)



    print('Поиск закончен')

    for i in range(len(name_list)):
        await bot.send_photo(message.from_user.id, photo=link_img_list[i],
                             caption=f'Название фильма: {name_list[i]}\nГод: {year_list[i]}\nРейтинг КП: {kp_rate_list[i]}\nРейтинг IMDB: {imdb_rate_list[i]}\nОписание: {opisanie_list[i]}\nСсылка на фильм: {link_film_list[i]}')

    await bot.send_message(message.from_user.id, f'Нашлось {len(name_list)} совпадений')



async def find_Film_random(message):
    r = randint(1, 37521)
    rnd_film = cur.execute(
        'SELECT NAME, YEAR, KP_RATE, IMDB_RATE, LINK_FILM, LINK_IMG, OPISANIE FROM BD_Film_lordfilm WHERE ID == ?',
        (r,))
    sfilm=rnd_film.fetchall()[0]

    await bot.send_photo(message.from_user.id, photo=sfilm[5],
                         caption=f'Название фильма: {sfilm[0]}\nГод: {sfilm[1]}\nРейтинг КП: {sfilm[2]}\nРейтинг IMDB: {sfilm[3]}\nОписание: {sfilm[6]}\nСсылка на фильм: {sfilm[4]}')
