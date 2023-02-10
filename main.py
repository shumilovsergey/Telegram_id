import telebot
from telebot import types


token = input("Please enter a token:\n")
print(token)
bot = telebot.TeleBot(token)


@bot.message_handler(content_types='text')
def feedback(message):
    
    bot.send_message(chat_id=message.chat.id, text=message.chat.id)






bot.polling(none_stop=True, interval=0) 