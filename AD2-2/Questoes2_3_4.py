import struct

# Estrutura do registro dentro do arquivo binário
Cartao = struct.Struct("20s 50s")

# Subprogramas -----

# Função para determinar se uma entrada é float
def verificaFloat(entrada):

    # Contadores
    contadorPonto = 0
    contadorNaoNumeros = 0

    # Vamos analisar cada caractere da entrada inserida
    for char in entrada:

        # Um float é composto de apenas dígitos numéricos, um "." e nenhum caractere não-numérico (p.ex.: alfabeto)
        if (char >= '0' and char <= '9'):
            pass
        elif (char == "."):
            contadorPonto = contadorPonto + 1
        else:
            contadorNaoNumeros = contadorNaoNumeros + 1

    # Aplicando os vínculos aos contadores e retornando o resultado negativo ao usuário
    if (contadorPonto > 1) or (contadorNaoNumeros > 0):
        return False

    # Retornando resultado positivo caso nenhum erro seja encontrado
    return True

# Função que busca o valor adicional associado à bandeira inserida pelo usuário
def buscaAdicionalCartao(cartoes, bandeira):

    # Inicializando resultado: valor nulo servirá de teste no Programa Principal
    adicionalCartao = 0

    # Determinando número de registros contidos no arquivo
    arquivo = cartoes.read()
    numeroRegistros = len(arquivo)/Cartao.size

    # Retornando cursor ao início do arquivo
    cartoes.seek(0)

    # Lendo os cartões disponíveis e buscando por aquele que corresponde ao nome inserido pelo usuário
    for indice in range(int(numeroRegistros)):
        bloco = cartoes.read(Cartao.size)
        campos = Cartao.unpack(bloco)
        if(campos[0].decode("utf-8").rstrip(chr(0)) == bandeira):
            adicionalCartao = campos[1].decode("utf-8").rstrip(chr(0))

    return(adicionalCartao)

def calculaValorTotal(bandeira, adicionalCartao, taxa, preco):
    valorTotal = preco * taxa + adicionalCartao
    print(f"Como seu cartão é da bandeira {bandeira}, então você pagará {valorTotal:.2f}")
    return(None)

# Fim dos Subprogramas -----

# Programa Principal: recebendo arquivo binário
arquivoBinario = input()

# Questão 2: recebendo o nome da bandeira do cartão
bandeira = input()

# Questão 3: recebendo o valor da taxa de conversão
taxa = input()

# Questão 4: recebendo o preço a ser convertido
preco = input()

# Testando se arquivo binário existe
try:
    with open(arquivoBinario, "rb") as cartoes:

        # Lendo as bandeiras de cartões disponíveis e verificando validade do nome inserido pelo usuário
        adicionalCartao = buscaAdicionalCartao(cartoes, bandeira)
        if (adicionalCartao != 0):

            adicionalCartao = float(adicionalCartao)

            # Testando se entradas de taxa e preço são floats
            if (verificaFloat(taxa)):
                taxa = float(taxa)
                if(verificaFloat(preco)):
                    preco = float(preco)
                    calculaValorTotal(bandeira, adicionalCartao, taxa, preco)
                else:
                    print("você colocou um valor não correspondente")
            else:
                print("você colocou uma taxa não correspondente")
        else:
            print("Cartão não consta")

except IOError:
    print("Um dos arquivos não foi encontrado ou você digitou errado.")