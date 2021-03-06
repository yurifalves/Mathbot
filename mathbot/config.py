import telebot
from telebot import types
from bot import Bot
import logging
import sys
import os
import math
import time
from funcionalidades import primos, trigonometria, eq2grau, numaleatorios, matrizes

bot = telebot.TeleBot(Bot.token())


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
    try:
        start_time = time.time()
        angulo = int(mensagem.text)
    except:
        msg_erro = """
Erro detectado - Mensagem fora do formato.\n
/trigonometria Para tentar novamente
/menu Voltar ao menu inicial
"""
        bot.reply_to(mensagem, msg_erro)

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
    try:
        start_time = time.time()
        primo1, primo2 = [int(num) for num in mensagem.text.split()]
    except:
        msg_erro = """
Erro detectado - Mensagem fora do formato.\n
/calcularprimos Para tentar novamente
/menu Voltar ao menu inicial
"""
        bot.reply_to(mensagem, msg_erro)

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
    try:
        start_time = time.time()
        num = int(mensagem.text)
    except:
        msg_erro = """
Erro detectado - Mensagem fora do formato.\n
/fatorial Para tentar novamente
/menu Voltar ao menu inicial
    """
        bot.reply_to(mensagem, msg_erro)

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
    try:
        start_time = time.time()
        a, b, c = [float(num) for num in mensagem.text.split()]
    except:
        msg_erro = """
Erro detectado - Mensagem fora do formato.\n
/eq2grau Para tentar novamente
/menu Voltar ao menu inicial
        """
        bot.reply_to(mensagem, msg_erro)

    resposta = f'{eq2grau.eq2grau(a, b, c)}\n\ntempo de execução: {time.time() - start_time:.3f} s'
    bot.send_message(mensagem.chat.id, resposta)
    bot.send_message(mensagem.chat.id, 'Para voltar ao menu principal:\n/menu')


@bot.message_handler(func=lambda mensagem: True if mensagem.text == 'Números Aleatórios' else False)
@bot.message_handler(commands=['numaleatorios'])
def numaleatorios_1(mensagem):
    texto_inicial = """
    Envie um mensagem no formato:
    *n min max*
    *n* - Quantos números inteiros. Deve estar dentro do intervalo [[1, 10000]].
    *min* e *max* - Limites inferior/superior do intervalo. Deve estar dentro do intervalo [[-1000000000, 1000000000]].
    
    Ex: '7 13 19' (sem as aspas)
    Resultado --> [[17, 17, 15, 18, 14, 13, 18]]
    Isso equivale a solicitar 7 números aleatórios dentro do intervalo fechado [[13, 19]].
    """
    markup = types.ReplyKeyboardRemove(selective=False)
    sent_msg = bot.send_message(mensagem.chat.id, texto_inicial, parse_mode='Markdown', reply_markup=markup)
    bot.register_next_step_handler(sent_msg, numaleatorios_2)


def numaleatorios_2(mensagem):
    try:
        n, min, max = [int(num) for num in mensagem.text.split()]
        resposta = numaleatorios.gerar_inteiros(Bot.random_api(), n, min, max)
        bot.send_message(mensagem.chat.id, resposta)
        bot.send_message(mensagem.chat.id, 'Para voltar ao menu principal:\n/menu')
    except:
        msg_erro = """
Erro detectado - Mensagem fora do formato.\n
/numaleatorios Para tentar novamente
/menu Voltar ao menu inicial
"""
        bot.reply_to(mensagem, msg_erro)


@bot.message_handler(func=lambda mensagem: True if mensagem.text == 'Matrizes' else False)
@bot.message_handler(commands=['matrizes'])
def matrizes1(mensagem):
    texto_inicial = """
Envie as linhas da matriz, separando cada elemento por um espaço " ".\n
Ex: "1 9 81
     2 -21 4,551
     0 0 7" (sem as aspas)
Informações sobre a matriz serão retornadas
    """
    markup = types.ReplyKeyboardRemove(selective=False)
    sent_msg = bot.send_message(mensagem.chat.id, texto_inicial, parse_mode='Markdown', reply_markup=markup)
    bot.register_next_step_handler(sent_msg, matrizes2)


def matrizes2(mensagem):
    try:
        start_time = time.time()
        texto = mensagem.text
    except:
        msg_erro = """
Erro detectado - Mensagem fora do formato.\n
/matrizes Para tentar novamente
/menu Voltar ao menu inicial
    """
        bot.reply_to(mensagem, msg_erro)
    A = matrizes.Matriz(texto)
    matriz_reduzida = A.forma_reduzida()
    resposta = f'{matriz_reduzida}\n\ntempo de execução: {time.time() - start_time:.3f} s'
    if len(str(resposta)) <= 4096:
        bot.send_message(mensagem.chat.id, resposta)
    else:
        bot.send_message(mensagem.chat.id,
                         f'Tamanho da resposta muito grande ( >= 4096 caracteres ),\no resultado estará no .txt abaixo:')
        ref_arquivo = open(f'matriz.txt', mode='w')
        ref_arquivo.write(resposta)
        ref_arquivo.close()
        bot.send_document(mensagem.chat.id, open(f'matriz.txt', mode='rb'))
        os.remove(f'matriz.txt')
    bot.send_message(mensagem.chat.id, 'Para voltar ao menu principal:\n/menu')


@bot.message_handler(func=lambda mensagem: True if mensagem.text == 'informações' else False)
@bot.message_handler(commands=['informacoes'])
def informacoes(mensagem):
    link = 'https://github.com/yurifalves/Mathbot'
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(mensagem.chat.id, f'O Bot ainda está em desenvolvimento.\nRepositório: {link}', reply_markup=markup)


@bot.message_handler(func=lambda mensagem: True)
def responder(mensagem):
    texto_padrao = """
*MENU INICIAL*\n
/trigonometria Fornece informações a respeito de algum ângulo fornecido
/fatorial Calcula o fatorial de um número x
/calcularprimos Calcula todos os primos num intervalo fechado [[a, b]]
/eq2grau Calcula as raízes de um polinômio de grau 2
/numaleatorios Retorna uma lista de números aleatórios
/matrizes Retorna informações sobre uma matriz
/informacoes
    """
    markup = types.ReplyKeyboardMarkup()
    itembtn1 = types.KeyboardButton('Trigonometria')
    itembtn2 = types.KeyboardButton('Fatorial')
    itembtn3 = types.KeyboardButton('Calcular Primos')
    itembtn4 = types.KeyboardButton('Equação 2° grau')
    itembtn5 = types.KeyboardButton('Números Aleatórios')
    itembtn6 = types.KeyboardButton('Matrizes')
    itembtn7 = types.KeyboardButton('informações')
    markup.row(itembtn1)
    markup.row(itembtn2)
    markup.row(itembtn3)
    markup.row(itembtn4)
    markup.row(itembtn5)
    markup.row(itembtn6)
    markup.row(itembtn7)
    bot.send_message(mensagem.chat.id, texto_padrao, parse_mode='Markdown', reply_markup=markup)


while True:
    try:
        bot.polling(none_stop=True)
    except Exception:
        logging.error(f'{sys.exc_info()[0]}\n({time.ctime()})\n')
        time.sleep(5)
