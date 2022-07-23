import sqlite3
import telebot
from telebot import types
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

bot = telebot.TeleBot(" ")


@bot.message_handler(command=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    markup = types.ReplyKeybordMarkup(row_width=1)
    itembtn1 = types.KeybordButton('Поиск по названию')
    itembtn2 = types.KeybordButton('Поиск по описанию')
    itembtn3 = types.KeybordButton('Случайный')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.send_message(chat_id, "Что найти?", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == 'Поиск по названию':
        f = open("text.txt", "w")
        f.write("название")
        f.close()
        chat_id = message.chat.id
        bot.send_message(chat_id, "Введите название:")

    elif message.text == 'Поиск по описанию':
        f = open("text.txt", "w")
        f.write("описание")
        f.close()
        chat_id = message.chat.id
        bot.send_message(chat_id, "Введите описание:")

    elif message.text == 'Случайный':

    else:
        chat_id = message.chat.id
        bot.send_message(chat_id, "Обрабатываю запрос...")

        db = sqlite3.connect('Triangle_Kino.db')
        cur = db.cursor()

        word = message.text
        r = open("text.txt", "r")
        readR = r.read()

        if readR == 'название':
            driver = webdriver.Firefox(options=options)

            name_list = []
            opisanie_list = []
            god_list = []
            Link1_list = []
            Link2_list = []

            for name in cur.execute('SELECT NAME FROM Triangle_Kino WHERE NAME LIKE ?', ('%' + word + '%',)):
                name_list.append(name[0])
            for opisanie in cur.execute('SELECT OPISANIE FROM Triangle_Kino WHERE NAME LIKE ?', ('%' + word + '%',)):
                opisanie_list.append(opisanie[0])
            for god in cur.execute('SELECT GOD FROM Triangle_Kino WHERE NAME LIKE ?', ('%' + word + '%',)):
                god_list.append(god[0])
            for Link1 in cur.execute('SELECT LINK FROM Triangle_Kino WHERE NAME LIKE ?', ('%' + word + '%',)):
                Link1_list.append(Link1[0])

            for film in Link1_list:
                try:
                    driver.get(film)
                    time.sleep(2)
                    driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
                    element2 = driver.find_element((By.XPATH, """/html/body/div/pjsdiv/pjsdiv[1]/video"""))
                    itog = str(element2.get_attribute('src'))
                    print(itog)
                    Link2_list.append(itog)

               2_list.append('Ошибка')
            driver.quit()

            i = 0
            while i < len(name_list):
                q = open('text.txt', 'w')
                q.write(str(name_list[i]))
                q.write('\n')
                q.write(str(god_list[i]))
                q.write('\n')
                q.write('\n')
                q.write(str(opisanie_list[i]))
                q.write('\n')
                q.write('\n')
                q.write(str(Link1_list[i]))
                q.write('\n')
                q.write('\n')
                q.write(str(Link2_list[i]))
                q.close()

                msg = open('text.txt', 'r')
                msgR = msg.read()
                chat_id = message.chat.id
                bot.send_message(chat_id, msgR)
                time.sleep(1)
                i += 1

bot.polling()
