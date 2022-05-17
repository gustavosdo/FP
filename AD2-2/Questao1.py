import struct

# Estrutura do registro dentro do arquivo binário
Cartao = struct.Struct("20s 50s")

# Subprogramas -----

# Solução da questão 1: codificação que gera um arquivo .bin a partir do arquivo .txt
def geraBinarioCartoes():

    # Abrindo (ou criando) arquivo binário para salvar os dados
    with open("cartoes.bin", "wb") as arquivoBinario:

        # Abrindo o arquivo txt original com os dados
        with open("cartoes.txt", "r") as arquivoTexto:

            # Lendo cada linha dos dados
            for linha in arquivoTexto.readlines():

                # Obtendo as strings que definem a bandeira e a taxa do cartão
                bandeira, taxa = linha.strip().split("#")

                # Empacotando e codificando em binário os dados
                bloco = Cartao.pack(bandeira.encode("utf-8"), taxa.encode("utf-8"))

                # Escrevendo os dados processados no arquivo binário
                arquivoBinario.write(bloco)

    # Finalizando o programa
    return(None)

# Fim dos Subprogramas -----
geraBinarioCartoes()