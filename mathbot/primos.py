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
        bot_bob = TelegramBot(TOKEN, chatid)
        pb = TelegramTqdm(bot_bob)
        for n in pb(range(a, b + 1)):
            cont = 0
            for t in range(1, n + 1):
                if n % t == 0:
                    cont += 1
            if cont == 2:
                listaprimos.append(n)
            else:
                listacompostos.append(n)
        return f'Considerando o intervalo [{a}, {b}]\n\n-NÚMEROS PRIMOS: {listaprimos}' \
               f'\n-NÚMEROS COMPOSTOS: {listacompostos}\n\n\ntempo de execução: {time.time() - start_time:.3f} s'
