def verificar_conexao():
    try:
        import speedtest
        st = speedtest.Speedtest()
        saida = f'Download: {st.download() / 1024 ** 2:.2f} Mb/s\nUpload: {st.upload() / 1024 ** 2:.2f} Mb/s\nPing: {st.results.ping} ms\nOUTRAS INFORMAÇÕES: {st.results.client}'
        return saida
    except Exception as e:
        return e


def informacoes_os():
    import platform
    bit_architecture, linkage_format = platform.architecture()
    sistema = platform.platform()
    processador = platform.processor()
    versao_python, compilador, implementacao = platform.python_version(), platform.python_compiler(), platform.python_implementation()
    informacoes = f'bit_architecture: {bit_architecture}, linkage_format={linkage_format}\n'
    informacoes += f'Sistema: {sistema}\n'
    informacoes += f'Processador: {processador}\n'
    informacoes += f'Python {versao_python}, Compilador: {compilador}, Implementação: {implementacao}'
    return informacoes


if __name__ == '__main__':
    print(verificar_conexao())
    print(informacoes_os())
