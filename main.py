import telebot
from telebot import types
from Buttons.buttons import *
def Logo():
    print(
          f"\033[035m"
          f"  ______   ______   ______   ______   ______   ______   ______   ______ \n"
          f" /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/ \n"
          f" ._.                                                                  ._. \n"                                                                                          
          f" |_|                                   \033[033m██████╗  █████╗ ███████╗      \033[035m |_| \n"
          f" |-|      \033[031m ___                     _   \033[033m╚════██╗██╔══██╗╚════██║      \033[035m |-| \n"                                                                                          
          f" |_|      \033[031m/ __| ___  __  _ _  ___ | |_ \033[033m █████╔╝╚██████║    ██╔╝      \033[035m |_| \n"
          f" ._.      \033[031m\__ \/ -_)/ _|| '_|/ -_)|  _|\033[033m██╔═══╝  ╚═══██║   ██╔╝       \033[035m ._. \n"                                                                                          
          f" |_|      \033[031m|___/\___|\__||_|  \___| \__|\033[033m███████╗ █████╔╝   ██║        \033[035m |_| \n"
          f" |-|                                   \033[033m╚══════╝ ╚════╝    ╚═╝        \033[035m |-| \n"                                                                                          
          f" |_|                                                                  |_| \n"
          f"  ______   ______   ______   ______   ______   ______   ______   ______ \n"
          f" /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/ \n"
          "                        \033[035m---==\033[033m{\033[031m Start Server \033[033m}\033[035m==---\033[0m                         ")
bot = telebot.TeleBot("6261213223:AAEFYDDZJiWRybogl998FR4RpV6rztV_Zpg")
# Handle '/start'
@bot.message_handler(commands=['start'])
def start(message):
    buttons=Buttons()
    print(message.chat.id)
    bot.send_message(message.chat.id,'Привет, {0.first_name}!'.format(message.from_user),reply_markup=buttons.markup_out(message.chat.id))
@bot.message_handler(content_types=['text'])
def bot_message(message):
    buttons = Buttons()
    temp=buttons.markup_out_b(message.chat.id,message.text)
    try:
        for i in list(temp[0]):
            markup = types.InlineKeyboardMarkup(row_width=1)
            f=list(i.strip().split("\n"))
            num=list(f[0])
            item = types.InlineKeyboardButton('Взять заказ', callback_data=f'{num[1]}')
            markup.add(item)
            if(f[9]=="Исполнитель:"):
                bot.send_message(message.chat.id, str(i), reply_markup=markup)
            else:
               bot.send_message(message.chat.id, str(i))
        bot.send_message(message.chat.id, str("=============="), reply_markup=temp[1])
    except:
        bot.send_message(message.chat.id,str(temp[0]), reply_markup=temp[1])

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        buttons = Buttons()
        if(buttons.exe.protect_id(call.message.chat.id)): ##проверка на айди исполнителя
            if buttons.protect_ordres(call.data):   #что если кал дату использовать как номер заказа а по юзерайди находить юзернейм и подвязівать его к заказу?
                buttons.orders_add_executors(call.message.chat.id,call.data)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Отлично!')
        else:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Ошибка!')

@bot.message_handler(func=lambda message: True)
def error_message(message):
    bot.reply_to(message, "error")
Logo()
bot.infinity_polling()