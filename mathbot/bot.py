import telebot
import os

bot = telebot.TeleBot(TOKEN)


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
        bot.send_message(mensagem.chat.id,
                         f'Tamanho da resposta muito grande ( >= 4096 caracteres ),\no resultado estará no .txt abaixo:')
        ref_arquivo = open(f'primos({primo1}-{primo2}).txt', mode='w')
        ref_arquivo.write(resposta)
        ref_arquivo.close()
        bot.send_document(mensagem.chat.id, open(f'primos({primo1}-{primo2}).txt', mode='rb'))
        os.remove(f'primos({primo1}-{primo2}).txt')
    bot.send_message(mensagem.chat.id, 'Para voltar ao menu principal:\n/menu')

@bot.message_handler(commands=['informacoes'])
def primos1(mensagem):
    link = 'https://github.com/yurifalves/telegrambots/tree/main/mathbot'
    bot.send_message(mensagem.chat.id, f'O Bot ainda está em desenvolvimento.\nRepositório: {link}')


@bot.message_handler(func=lambda mensagem: True)
def responder(mensagem):
    texto_padrao = """
    *MENU INICIAL*

    /calcularprimos Calcula todos os primos num intervalo fechado [[a, b]].
    /informacoes
    """
    bot.send_message(mensagem.chat.id, texto_padrao, parse_mode='Markdown')


bot.polling()
