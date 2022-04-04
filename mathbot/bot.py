import telebot
from telebot import types
import os
import math
import time
import primos, trigonometria, eq2grau

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(func=lambda mensagem: True if mensagem.text == 'Trigonometria' else False)
@bot.message_handler(commands=['trigonometria'])
def trigonometria1(mensagem):
    texto_inicial = """
    Envie um ângulo entre -∞ e +∞, no formato *angulo*\n
    Ex: '389' (sem as aspas)
    equivale a solicitar as informações trigonométricas do ângulo 389°
    """
    markup = types.ReplyKeyboardRemove(selective=False)
    sent_msg = bot.send_message(mensagem.chat.id, texto_inicial, parse_mode='Markdown', reply_markup=markup)
    bot.register_next_step_handler(sent_msg, trigonometria2)


def trigonometria2(mensagem):
    start_time = time.time()
    angulo = int(mensagem.text)
    ref_arquivo = trigonometria.grafico(angulo)
    resposta = trigonometria.trig(angulo) + f'\ntempo de execução: {time.time() - start_time:.3f} s'
    bot.send_photo(mensagem.chat.id, ref_arquivo)
    bot.send_message(mensagem.chat.id, resposta)
    bot.send_message(mensagem.chat.id, 'Para voltar ao menu principal:\n/menu')
    ref_arquivo.close()
    os.remove(f'trigonometria({angulo}).png')


@bot.message_handler(func=lambda mensagem: True if mensagem.text == 'Calcular Primos' else False)
@bot.message_handler(commands=['calcularprimos'])
def primos1(mensagem):
    texto_inicial = """
    Envie dois números primos, no formato *a* *b*\n
    Ex: '1049 10982' (sem as aspas)
    equivale a solicitar os números primos no intervalo fechado [[1049, 10982]]
    """
    markup = types.ReplyKeyboardRemove(selective=False)
    sent_msg = bot.send_message(mensagem.chat.id, texto_inicial, parse_mode='Markdown', reply_markup=markup)
    bot.register_next_step_handler(sent_msg, primos2)


def primos2(mensagem):
    start_time = time.time()
    primo1, primo2 = [int(num) for num in mensagem.text.split()]
    resposta = f'{primos.checarintervalo(primo1, primo2, mensagem.chat.id)}\n\n\ntempo de execução: {time.time() - start_time:.3f} s'
    if len(resposta) <= 4096:
        bot.send_message(mensagem.chat.id, resposta)
    else:
        bot.send_message(mensagem.chat.id,
                         f'Tamanho da resposta muito grande ( >= 4096 caracteres ),\no resultado estará no .txt abaixo:')
        ref_arquivo = open(f'primos({primo1}-{primo2}).txt', mode='w')
        ref_arquivo.write(resposta)
        ref_arquivo.close()
        bot.send_document(mensagem.chat.id, open(f'primos({primo1}-{primo2}).txt', mode='rb'), caption=f'tempo de execução: {time.time() - start_time:.3f} s')
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
    start_time = time.time()
    num = int(mensagem.text)
    resposta = f'{num}! =\n{math.factorial(num)}\n\ntempo de execução: {time.time() - start_time:.3f} s'
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


@bot.message_handler(func=lambda mensagem: True if mensagem.text == 'Equação 2° grau' else False)
@bot.message_handler(commands=['eq2grau'])
def eq2grau1(mensagem):
    texto_inicial = """
    P(x) = ax²+bx+c
    Envie os coeficientes, no formato *a b c*\n
    Ex: '3 4 1' (sem as aspas)
    equivale a solicitar as raízes de P(x) = 3x²+4x+1.
    """
    markup = types.ReplyKeyboardRemove(selective=False)
    sent_msg = bot.send_message(mensagem.chat.id, texto_inicial, parse_mode='Markdown', reply_markup=markup)
    bot.register_next_step_handler(sent_msg, eq2grau2)


def eq2grau2(mensagem):
    start_time = time.time()
    a, b, c = [float(num) for num in mensagem.text.split()]
    resposta = f'As raízes de {a}x²+{b}x+{c} são:\n{eq2grau.eq2grau(a, b, c)}\n\ntempo de execução: {time.time() - start_time:.3f} s'
    bot.send_message(mensagem.chat.id, resposta)
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

    /trigonometria Fornece informações a respeito de algum ângulo fornecido.
    /fatorial Calcula o fatorial de um número x.
    /calcularprimos Calcula todos os primos num intervalo fechado [[a, b]].
    /eq2grau Calcula as raízes de um polinômio de grau 2.
    /informacoes
    """
    markup = types.ReplyKeyboardMarkup()
    itembtn1 = types.KeyboardButton('Trigonometria')
    itembtn2 = types.KeyboardButton('Fatorial')
    itembtn3 = types.KeyboardButton('Calcular Primos')
    itembtn4 = types.KeyboardButton('Equação 2° grau')
    itembtn5 = types.KeyboardButton('informações')
    markup.row(itembtn1)
    markup.row(itembtn2)
    markup.row(itembtn3)
    markup.row(itembtn4)
    markup.row(itembtn5)
    bot.send_message(mensagem.chat.id, texto_padrao, parse_mode='Markdown', reply_markup=markup)


bot.polling()
