def verificar_conexao():
    try:
        import speedtest
        st = speedtest.Speedtest()
        saida = f'Download: {st.download() / 1024 ** 2:.2f} Mb/s\nUpload: {st.upload() / 1024 ** 2:.2f} Mb/s\nPing: {st.results.ping}\nOUTRAS INFORMAÇÕES: {st.results.client}'
        return saida
    except Exception as e:
        return e


if __name__ == '__main__':
    print(verificar_conexao())
