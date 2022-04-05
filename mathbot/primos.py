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
    if a < 0 or a > b:
        return f'Alguma condição está sendo violada: a < 0 ou a < b'
    else:
        bot_bob = TelegramBot(TOKEN, chatid)
        pb = TelegramTqdm(bot_bob)
        
        def is_prime(n):
            if n == 2 or n == 3: return True
            if n < 2 or n % 2 == 0: return False
            if n < 9: return True
            if n % 3 == 0: return False
            r = int(n ** 0.5)
            f = 5
            while f <= r:
                if n % f == 0: return False
                if n % (f + 2) == 0: return False
                f += 6
            return True
        listaprimos = [n for n in pb(range(a, b + 1)) if is_prime(n)]
        return f'Considerando o intervalo [{a}, {b}]\n\n-NÚMEROS PRIMOS: {listaprimos}'
