# Subprogramas ----------

# Função utilizada para calcular todos os sumários estatísticos requiridos
def sumario(dados):

    # Cardinalidade do conjunto de dados
    N = 0

    # Variável que receberá a soma de todos os dados contidos no arquivo
    somaValores = 0

    # Variável que receberá a soma dos quadrados dos dados do arquivo
    somaValoresQuad = 0

    # Iniciando valores mínimo e máximo
    minimo = 0
    maximo = 0

    # Correndo todos os valores do vetor a fim de determinar o menor e o maior valores além de somar os valores e seus quadrados
    for linha in dados:

        # Imprimindo linha de dados
        print("\t", linha, end = "")

        # Separando os valores da linha atual
        valores = [int(v) for v in linha.split()]
        
        # Percorrendo todos os valores previamente separados por espaço na mesma linha
        for indice in range(len(valores)):
            N = N + 1

            # Definindo valores mínimo e máximo
            if   valores[indice] < minimo: minimo = valores[indice]
            elif valores[indice] > maximo: maximo = valores[indice]

            # Somando valores e quadrado dos valores
            somaValores = somaValores + valores[indice]
            somaValoresQuad = somaValoresQuad + valores[indice] * valores[indice]

    # Calculando média e desvio padrão
    media = somaValores/N
    sigma = (somaValoresQuad/N - (2*media/N) * somaValores + media ** 2) ** (1/2)

    return minimo, maximo, media, sigma
# Fim dos subprogramas ----------

# Programa principal

# Recebendo nome do arquivo que contém os dados
arquivo = str(input("Entre com o nome do arquivo que contém os dados:"))

# Lendo o arquivo de dados
dados = open(arquivo + ".txt", "r")

# Verificando existência de dados dentro do arquivo
if (dados.read(1)):

    # Voltando ao início do arquivo
    dados = open(arquivo + ".txt", "r")

    # Caso os dados estejam no arquivo, imprimi-los e calcular as grandezas solicitadas no enunciado
    print("Conteúdo do Arquivo "+arquivo+":")
    minimo, maximo, media, sigma = sumario(dados)

    # Retornando resultados ao usuário
    print("\n")
    print("Menor Valor em "+arquivo+": %d"%minimo)
    print("Maior Valor em "+arquivo+": %d"%maximo)
    print("Média dos Valores em "+arquivo+": %.2f"%media)
    print("Desvio Padrão em "+arquivo+": %.2f"%sigma)

else:
    print("Não existem menor, maior, média e desvio, pois o arquivo está vazio!!!")
    
# Fechando arquivo de dados após sua utilização
dados.close()