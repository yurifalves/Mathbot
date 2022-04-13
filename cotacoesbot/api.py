def currency_api(key):
    """
    Currencyapi --> https://app.currencyapi.com/
    :param key: API Key.
    :return: String com as cotações de todas as moedas disponíveis na API.
    """
    import requests
    res = requests.get(f'https://api.currencyapi.com/v3/latest?apikey={key}&base_currency=BRL').json()
    last_updated = res['meta']['last_updated_at']
    moedas = [moeda for moeda in res['data']]
    quantidade_moedas = len([moeda for moeda in res['data']])
    texto1 = f'{quantidade_moedas} Moedas\n({last_updated})\n\n'  # Moedas importantes
    texto2 = str()  # Moedas Secundárias

    moedas_importantes = {'USD': 'Dólar Americano',
                          'EUR': 'Euro',
                          'GPB': 'Libra esterlina',
                          'JPY': 'Iene japonês',
                          'CHF': 'Franco suíço',
                          'CAD': 'Dólar canadense',
                          'AUD': 'Dólar Australiano',
                          'RUB': 'Rublo russo',
                          'ARS': 'Peso argentino'}

    c = 0
    while c < quantidade_moedas:
        moeda = moedas[c]
        code, valor = res['data'][moeda]['code'], str(round(1/res['data'][moeda]['value'], 6)).replace('.', ',')
        if code in moedas_importantes:
            texto1 += f'1 {code} ({moedas_importantes[code]}) = R$ {valor}\n'
        else:
            texto2 += f'1 {code} = R$ {valor}\n'
        c += 1
    return texto1 + texto2
