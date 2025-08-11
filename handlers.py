#Отправка пользовтелю контактов
@bot.message_handler(commands=['send_contact'])
def bot_send_contact(message:types.Message):
    bot.send_contact(message.chat.id,'Номер телефона','Фамилия','Имя')
    #Если пользователь есть в списке контактов аргументы заменятся на данные из профиля

#Отправка пользовтелю документов
@bot.message_handler(commands=['send_document'])
def bot_send_document(message:types.Message):
    bot.send_document(message.chat.id,types.InputFile('Files/Telegram.docx'))
    #Если пользователь есть в списке контактов аргументы заменятся на данные из профиля

#Отправка аудио
@bot.message_handler(commands=['send_audio'])
def bot_send_audio(message:types.Message):
    bot.send_audio(message.chat.id,types.InputFile('Files/cicada.mp3'))

#Отправка кубика
@bot.message_handler(commands=['send_dice'])
def bot_send_dice(message:types.Message):
    bot.send_dice(message.chat.id)

#Отправка текущего действия бота например пишет
@bot.message_handler(commands=['send_chat_action'])
def bot_send_chat_action(message:types.Message):
    bot.send_chat_action(message.chat.id,'typing',5)
     #action (str) – Тип действия. Выберите один, в зависимости от того, что получит пользователь:
     # typing для текстовых сообщений, upload_photo для фото, record_video или upload_video для видео,
     # record_voice или upload_voice для голосовых сообщений, upload_document для файлов, choose_sticker для стикеров,
     # find_location для данных о местоположении, record_video_note или upload_video_note для видео заметок (кружочков).

@bot.message_handler(commands=['send_poll'])
def bot_send_poll(message:types.Message):
    answers = ['19:00','20:00']
    bot.send_poll(message.chat.id,'Сколько времени',answers,correct_option_id=1)

#Обработчик команды myname
@bot.message_handler(commands=['myname'])
def bot_user_name(message:types.Message):
    bot.send_message(message.chat.id,f'Вас зовут {message.from_user.full_name}')

@bot.message_handler(commands=['inline'])
def bot_inline(message:types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Документация telegram bot',url='https://pypi.org/project/pyTelegramBotAPI/'))
    bot.send_message(message.chat.id,'Главное меню',reply_markup=keyboard)

#Обработчик сообщений
@bot.message_handler(content_types='text')
def bot_text(message:types.Message):
    if message.text == '1':
       bot.reply_to(message,'Вы написали 1')
    elif message.text == '2':
       bot.reply_to(message,'Вы написали 2')

@bot.message_handler(content_types=['document','audio']) #Обработка отправки документов и аудио
def bot_document(message:types.Message):
    if message.content_type == 'document':
        print(message.document.file_id)
    elif message.content_type == 'audio':
        print(message.audio.title)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "game":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Вторичное меню')
    # Если сообщение из инлайн-режима
    elif call.inline_message_id:
        if call.data == "test":
            bot.edit_message_text(inline_message_id=call.inline_message_id, text="Бдыщь")