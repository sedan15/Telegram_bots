import telebot
from telebot import types #Импорт типов для определения свойств
import userModel
import keyboards
from json_commands import *
import db

token = '8428189477:AAGbLM-CXunZrAMdE71ckM0A1tTsIzFkLks'

bot = telebot.TeleBot(token)

commands = ['start','help','myname']

#Обработчик команд start и help
@bot.message_handler(commands=['start','help'])
def bot_hello(message:types.Message):
    user = db.get_one_by_id('users',message.from_user.id) #Поиск пользователя в базе данных
    if user == None:
        bot.send_message(message.chat.id,f'Cначала необходимо зарегистроваться',reply_markup=keyboards.registration_keyboard())
    else:
        bot.send_message(message.chat.id,f'Вот мои комманды',reply_markup=keyboards.command_keyboard())


@bot.callback_query_handler(func=lambda call:True)
def callback_handler(call:types.CallbackQuery):
    if call.message:
        if call.data == 'registration':
            user = userModel.create_user(call.from_user)
            db.save_one('users','id,first_name,last_name',f'''{user.id},'{user.first_name}','{user.last_name}' ''') #Запись пользоватея в базу данных
            bot.send_message(call.message.chat.id,'Регистрация успешна')    
            bot.edit_message_text(call.message.text,call.message.chat.id,call.message.id)
        elif call.data == 'delete_account':
            db.delete_one_by_id('users',call.from_user.id) #Удаление пользователя из базы данныз
            bot.send_message(call.message.chat.id,'Данные удалены')
            bot.edit_message_text(call.message.text,call.message.chat.id,call.message.id)


bot.infinity_polling()