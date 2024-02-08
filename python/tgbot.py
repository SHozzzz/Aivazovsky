import telebot
from telebot import types
import requests
import time
import configparser

bot = telebot.TeleBot('6149431036:AAHRIu33NtVGguTr0CkYNvW8kMV15UaYa84')

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("magsafe")
    btn2 = types.KeyboardButton("softtauch")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я тестовый бот для твоей статьи для habr.com".format(message.from_user), reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "👋 Поздороваться"):
        bot.send_message(message.chat.id, text="Привеет.. Спасибо что читаешь статью!)")
    elif(message.text == "softtauch"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("darkgreen🍏")
        btn2 = types.KeyboardButton("darkpurple👾")
        btn3 = types.KeyboardButton("orange🍊")
        btn4 = types.KeyboardButton("dark🥷🏻")
        markup.add(btn1, btn2, btn3 , btn4)
        bot.send_message(message.chat.id, text="pick a color", reply_markup=markup)
    
    elif(message.text == "darkgreen🍏"):
        img = open('D:\Сайт\python\phone1.png' , 'rb')
        bot.send_photo(message.chat.id ,img)
    
    elif(message.text == "darkpurple👾"):
        img = open('D:\Сайт\python\phone3.png' , 'rb')
        bot.send_photo(message.chat.id ,img)
    
    elif(message.text == "dark🥷🏻"):
        img = open('D:\Сайт\python\phone2.png' , 'rb')
        bot.send_photo(message.chat.id ,img)

    elif(message.text == "orange🍊"):
        img = open('D:\Сайт\python\phone4.png' , 'rb')
        bot.send_photo(message.chat.id ,img)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")

bot.polling(none_stop=True)