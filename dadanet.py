import telebot

TOKEN = 1633603922:AAFxE90WD_IMaojKeL2jvp3ZEbwb-PAXQ0o

bot = telebot.TeleBot('TOKEN')

#Теперь напишем обработчик текстовых сообщений, который будет обрабатывать входящие команды /start и /help:
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Я бот. Приятно познакомиться, {message.from_user.first_name}')
#Добавим ещё один обработчик для получения текстовых сообщений. Если бот получит «Привет», он также поздоровается. Все остальные сообщения будут определены, как нераспознанные:

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    else:
        bot.send_message(message.from_user.id, 'Не понимаю, что это значит.')
#Запускаем бота следующей строкой:

bot.polling(none_stop=True)
#Примечание
#Так мы задаём боту непрерывное отслеживание новых сообщений.
#Если бот упадёт, а сообщения продолжат поступать, они будут накапливаться в течение 24 часов на серверах Telegram, и в случае восстановления бота прилетят ему все сразу.