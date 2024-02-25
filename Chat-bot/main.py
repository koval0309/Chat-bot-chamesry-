import telebot

bot = telebot.TeleBot('6692662161:AAFO43MklaENKhglMu7ptViXP_7QQu_zI80')


@bot.message_handler(commands=["start"])
def main(message):
    bot.send_message(message.chat.id, "Привіт, я твій помічник з хімії!І в даний момент я в стані розробки, тому я можу тобі розказати про елементи в таблці Менделєєва.Введи любий хімічний елемент:")


@bot.message_handler()
def info(message):
    if message.text.lower() == "h":
        bot.send_message(message.chat.id, "Гідроген")
    elif message.text.lower() == "he":
        bot.send_message(message.chat.id, "Гелій")
    elif message.text.lower() == "li":
        bot.send_message(message.chat.id, "Літій")
    elif message.text.lower() == "be":
        bot.send_message(message.chat.id, "Берилій")
    elif message.text.lower() == "b":
        bot.send_message(message.chat.id, "Бор")




bot.polling(non_stop=True)

