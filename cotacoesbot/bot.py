import telebot
from telebot import types
import apis


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(func=lambda mensagem: True if mensagem.text == 'currencyapi' else False)
@bot.message_handler(commands=['currencyapi'])
def currencyapi(mensagem):
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(mensagem.chat.id, apis.currency_api(key), parse_mode='Markdown', reply_markup=markup)


@bot.message_handler(func=lambda mensagem: True)
def responder(mensagem):
    texto_padrao = """
    *MENU INICIAL*
    /currencyapi Consultar cotações usando Currencyapi
    /informacoes
    """
    markup = types.ReplyKeyboardMarkup()
    itembtn1 = types.KeyboardButton('currencyapi')
    itembtn2 = types.KeyboardButton('informações')
    markup.row(itembtn1)
    markup.row(itembtn2)
    bot.send_message(mensagem.chat.id, texto_padrao, parse_mode='Markdown', reply_markup=markup)


bot.polling()
