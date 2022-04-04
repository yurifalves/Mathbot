import telebot
import os

bot = telebot.TeleBot('5280082287:AAF9zyPYm49sqF2NfwcqGmc01QYWBQqgxDY')

def checarintervalo(a, b, chatid):
    """
    Esta função checa dentro de um intervalo fechado [a, b] sendo a e b números naturais,
    quais números são primos e quais são compostos.
    :param a: Início do intervalo a ser analisado.
    :param b: Fim do Intervalo a ser analisado.
    :param chatid: ID do chat no qual o bot está enviando a mensagem.
    :return: 2 listas, uma com os números primos e outra com os números compostos. Abaixo aparecerá o tempo de execução.
    """
    from bob_telegram_tools.utils import TelegramTqdm
    from bob_telegram_tools.bot import TelegramBot
    import time
    start_time = time.time()
    if a < 0 or a > b:
        return f'alguma condição está sendo violada: a < 0 ou a < b'
    else:
        listaprimos, listacompostos = [], []
        bot_bob = TelegramBot('5280082287:AAF9zyPYm49sqF2NfwcqGmc01QYWBQqgxDY', chatid)
        pb = TelegramTqdm(bot_bob)
        for n in pb(range(a, b+1)):
            cont = 0
            for t in range(1, n+1):
                if n % t == 0:
                    cont += 1
            if cont == 2:
                listaprimos.append(n)
            else:
                listacompostos.append(n)
        return f'CONSIDERANDO O INTERVALO [{a}, {b}]\nNÚMEROS PRIMOS: {listaprimos}' \
               f'\nNÚMEROS COMPOSTOS: {listacompostos}\nTEMPO DE EXECUÇÃO: {time.time() - start_time:.3f} s'


@bot.message_handler(commands=['calcularprimos'])
def primos1(mensagem):
    texto_inicial = """
    Envie dois núemros primos, no formato *num1* *num2*\n
    Ex: '1049 10982' (sem as aspas)
    equivale a solicitar os números primos no intervalo fechado [[1049, 10982]]
    """
    sent_msg = bot.send_message(mensagem.chat.id, texto_inicial, parse_mode='Markdown')
    bot.register_next_step_handler(sent_msg, primos2)


def primos2(mensagem):
    primo1, primo2 = [int(num) for num in mensagem.text.split()]
    resposta = checarintervalo(primo1, primo2, mensagem.chat.id)
    if len(resposta) <= 4096:
        bot.send_message(mensagem.chat.id, resposta)
    else:
        bot.send_message(mensagem.chat.id, f'Tamanho da resposta muito grande ( >= 4096 caracteres ),\no resultado estará no .txt abaixo:')
        ref_arquivo = open(f'primos({primo1}-{primo2}).txt', mode='w')
        ref_arquivo.write(resposta)
        ref_arquivo.close()
        bot.send_document(mensagem.chat.id, open(f'primos({primo1}-{primo2}).txt', mode='rb'))
        os.remove(f'primos({primo1}-{primo2}).txt')


@bot.message_handler(commands=['informacoes'])
def primos1(mensagem):
    link = 'aquivaiolink.com.br'
    bot.send_message(mensagem.chat.id, f'O Bot ainda está em desenvolvimento.\nRepositório: {link}')


@bot.message_handler(func=lambda mensagem: True)
def responder(mensagem):
    texto_padrao = """
    *MENU INICIAL*
    
    /calcularprimos Calcula todos os primos num intervalo fechado [[a, b]].
    /informacoes
    """
    bot.send_message(mensagem.chat.id, texto_padrao, parse_mode='Markdown')


bot.polling()  # Mantém o bot "funcionando/ligado"
