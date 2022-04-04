import telebot
from telebot import types
import os
import math
import primos

bot = telebot.TeleBot('5232695368:AAH_CQAYVlI0TVEas8XSppXvBOA1wY1LjY4')


@bot.message_handler(func=lambda mensagem: True if mensagem.text == 'Calcular Primos' else False)
@bot.message_handler(commands=['calcularprimos'])
def primos1(mensagem):
    texto_inicial = """
    Envie dois números primos, no formato *num1* *num2*\n
    Ex: '1049 10982' (sem as aspas)
    equivale a solicitar os números primos no intervalo fechado [[1049, 10982]]
    """
    markup = types.ReplyKeyboardRemove(selective=False)
    sent_msg = bot.send_message(mensagem.chat.id, texto_inicial, parse_mode='Markdown', reply_markup=markup)
    bot.register_next_step_handler(sent_msg, primos2)


def primos2(mensagem):
    primo1, primo2 = [int(num) for num in mensagem.text.split()]
    resposta = primos.checarintervalo(primo1, primo2, mensagem.chat.id)
    if len(resposta) <= 4096:
        bot.send_message(mensagem.chat.id, resposta)
    else:
        bot.send_message(mensagem.chat.id,
                         f'Tamanho da resposta muito grande ( >= 4096 caracteres ),\no resultado estará no .txt abaixo:')
        ref_arquivo = open(f'primos({primo1}-{primo2}).txt', mode='w')
        ref_arquivo.write(resposta)
        ref_arquivo.close()
        bot.send_document(mensagem.chat.id, open(f'primos({primo1}-{primo2}).txt', mode='rb'))
        os.remove(f'primos({primo1}-{primo2}).txt')
    bot.send_message(mensagem.chat.id, 'Para voltar ao menu principal:\n/menu')


@bot.message_handler(func=lambda mensagem: True if mensagem.text == 'Fatorial' else False)
@bot.message_handler(commands=['fatorial'])
def fatorial1(mensagem):
    texto_inicial = """
    Envie algum número, no formato *num*\n
    Ex: '10982' (sem as aspas)
    equivale a solicitar o fatorial do número 10982.
    """
    markup = types.ReplyKeyboardRemove(selective=False)
    sent_msg = bot.send_message(mensagem.chat.id, texto_inicial, parse_mode='Markdown', reply_markup=markup)
    bot.register_next_step_handler(sent_msg, fatorial2)


def fatorial2(mensagem):
    num = int(mensagem.text)
    resposta = f'O fatorial de {num} é\n{math.factorial(num)}'
    if len(str(resposta)) <= 4096:
        bot.send_message(mensagem.chat.id, resposta)
    else:
        bot.send_message(mensagem.chat.id,
                         f'Tamanho da resposta muito grande ( >= 4096 caracteres ),\no resultado estará no .txt abaixo:')
        ref_arquivo = open(f'fatorial({num}).txt', mode='w')
        ref_arquivo.write(resposta)
        ref_arquivo.close()
        bot.send_document(mensagem.chat.id, open(f'fatorial({num}).txt', mode='rb'))
        os.remove(f'fatorial({num}).txt')
    bot.send_message(mensagem.chat.id, 'Para voltar ao menu principal:\n/menu')


@bot.message_handler(func=lambda mensagem: True if mensagem.text == 'informações' else False)
@bot.message_handler(commands=['informacoes'])
def informacoes(mensagem):
    link = 'https://github.com/yurifalves/telegrambots/tree/main/mathbot'
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(mensagem.chat.id, f'O Bot ainda está em desenvolvimento.\nRepositório: {link}', reply_markup=markup)


@bot.message_handler(func=lambda mensagem: True)
def responder(mensagem):
    texto_padrao = """
    *MENU INICIAL*

    /calcularprimos Calcula todos os primos num intervalo fechado [[a, b]].
    /fatorial Calcula o fatorial de um número x.
    /informacoes
    """
    markup = types.ReplyKeyboardMarkup()
    itembtn1 = types.KeyboardButton('Calcular Primos')
    itembtn2 = types.KeyboardButton('Fatorial')
    itembtn3 = types.KeyboardButton('informações')
    markup.row(itembtn1)
    markup.row(itembtn2)
    markup.row(itembtn3)
    bot.send_message(mensagem.chat.id, texto_padrao, parse_mode='Markdown', reply_markup=markup)


bot.polling()
