import telebot
from config import token

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Я бот для управления чатом.")

@bot.message_handler(commands=['ban'])
def ban_user(message):
    if message.reply_to_message:  # проверка на то, что команда вызвана в ответ
        chat_id = message.chat.id
        user_id = message.reply_to_message.from_user.id
        user_status = bot.get_chat_member(chat_id, user_id).status

        if user_status in ['administrator', 'creator']:
            bot.reply_to(message, "Невозможно забанить администратора.")
        else:
            bot.ban_chat_member(chat_id, user_id)
            bot.reply_to(message, f"Пользователь @{message.reply_to_message.from_user.username} был забанен.")
    else:
        bot.reply_to(message, "Эта команда должна быть использована в ответ на сообщение.")

@bot.message_handler(func=lambda message: True)
def check_links(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    username = message.from_user.username

    if "https://" in message.text: 
        user_status = bot.get_chat_member(chat_id, user_id).status

        if user_status in ['administrator', 'creator']:
            bot.reply_to(message, "Администратор отправил ссылку, бан невозможен.")
        else:
            bot.ban_chat_member(chat_id, user_id)
            bot.reply_to(message, f"Пользователь @{username} был забанен за отправку ссылки.")

bot.infinity_polling(none_stop=True)

bot.infinity_polling(none_stop=True)

