import telebot
from telebot import types #Импорт типов для определения свойств
import userModel
import keyboards
from json_commands import *
import db


token = '7663789481:AAG2hDe1_rtNGUEMl1zdkY1r2cvTXcLsQGs'

bot = telebot.TeleBot(token)
Users = read_json('users.json') #Список с пользователями

print(Users)

commands = ['start','help','myname']

#Обработчик команд start и help
@bot.message_handler(commands=['start','help'])
def bot_hello(message:types.Message):
    bot.send_message(message.chat.id,f'Cначала необходимо зарегистроваться',reply_markup=keyboards.registration_keyboard())
        # bot.send_message(message.chat.id,f'Вот мои комманды',reply_markup=keyboards.command_keyboard())


@bot.callback_query_handler(func=lambda call:True)
def Registration(call:types.CallbackQuery):
    if call.message:
        if call.data == 'registration':
            user = userModel.create_user(call.from_user)
            query = f'''INSERT INTO users(id,first_name,last_name) VALUES({user.id},'{user.first_name}','{user.last_name}');'''
            db.cursor.execute(query)
            bot.send_message(call.message.chat.id,'Регистрация успешна')    
            bot.edit_message_text(call.message.text,call.message.chat.id,call.message.id)
        elif call.data == 'delete_account':
            user = user.create_user(call.from_user)
            del Users[str(user.id)]
            write_json('users.json',Users)
            bot.send_message(call.message.chat.id,'Данные удалены')
            bot.edit_message_text(call.message.text,call.message.chat.id,call.message.id)


bot.infinity_polling()