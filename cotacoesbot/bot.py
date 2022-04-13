import telebot
from telebot import types
import time
import os
import apis


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(func=lambda mensagem: True if mensagem.text == 'currencyapi' else False)
@bot.message_handler(commands=['currencyapi'])
def currencyapi(mensagem):
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(mensagem.chat.id, f'Tamanho da resposta muito grande ( >= 4096 caracteres ),\no resultado estará no .txt abaixo:', reply_markup=markup)
    start_time = time.time()
    ref_arquivo = open('cotacao-currencyapi.txt', mode='w')
    ref_arquivo.write(apis.currency_api(key))
    ref_arquivo.close()
    bot.send_document(mensagem.chat.id, open(f'cotacao-currencyapi.txt', mode='rb'), caption=f'tempo de execução: {time.time() - start_time:.3f} s')
    os.remove('cotacao-currencyapi.txt')
    bot.send_message(mensagem.chat.id, 'Para voltar ao menu principal:\n/menu')


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
