def gerar_inteiros(api_key: str, n: int, min: int, max: int) -> str:
    """
    Esta função retorna n números inteiros aleatórios dentro de um intervalo fechado [min, max].
    :param api_key: https://api.random.org/
    :param n: Quantos números inteiros aleatórios serão gerados. Deve estar dentro do intervalo [1, 10000].
    :param min: Limites inferior do intervalo. Deve estar dentro do intervalo [-1000000000, 1000000000].
    :param max: Limites superior do intervalo. Deve estar dentro do intervalo [-1000000000, 1000000000].
    :return:
    """
    from rdoclient import RandomOrgClient
    r = RandomOrgClient(api_key, blocking_timeout=2.0, http_timeout=10.0)
    res = r.generate_signed_integers(n, min, max)
    lista_inteiros = res['data']
    horario_utc = res['random']['completionTime']
    return f'{lista_inteiros}\n\ncompletionTime(UTC): {horario_utc}'
  
