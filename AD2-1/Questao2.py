# Subprogramas ----------

# Função que copia os dados de um arquivo para outro (levemente modificada do slide 49 da aula 9)
def copiaArquivo(arquivoOriginal):

    # Lendo arquivo original
    original = open(arquivoOriginal + ".txt", "r")
    
    # Definindo endereço do novo arquivo
    arquivoNovo = arquivoOriginal + "_copia"

    # Abrindo arquivo para escrita
    destino = open(arquivoNovo + ".txt", "w")
    
    # Copiando linha-a-linha
    for linha in original:
        destino.write(linha)
    
    # Fechando arquivos
    destino.close()
    original.close()

    # Retorna endereço da cópia do arquivo
    return(arquivoNovo)

# Essa função imprime todos os dados
def imprime(arquivo, remocao = False):
    
    # Lendo os arquivos
    dados = open(arquivo + ".txt", "r")

    # Caso tenha sido realizada a remoção, deixar explícito na impressão
    if (remocao):
        print("Conteúdo do Arquivo "+arquivo+" após eventuais remoções:")
    else:
        print("Conteúdo do Arquivo "+arquivo+":")

    # Imprimindo dados linha por linha
    for linha in dados:
        print("\t\t", linha, end = "")
    print("\n")

    # Fechando arquivo
    dados.close()

    # Retorna ao programa principal
    return None

# Função que remove do arquivo os pontos que estiverem dentro dos círculos
def removePontos(arquivoPontos, arquivoCirculos):

    # Copiando os pontos orginais para um arquivo auxiliar
    arquivoAux = copiaArquivo(arquivoPontos)

    # Arquivo original (copiado)
    pontos = open(arquivoAux + ".txt", "r")

    # Sobrescrevendo arquivo de dados com o resultado
    pontosAposRemocao = open(arquivoPontos + ".txt", "w")

    for linha in pontos:
        if (foraDosCirculos(linha, arquivoCirculos)):
            pontosAposRemocao.write(linha)

    # Fechando arquivos
    pontosAposRemocao.close()
    pontos.close()

    # Retornando ao programa principal
    return(None)

# Função para determinar se um ponto está dentro dos círculos
def foraDosCirculos(linha, arquivoCirculos):

    # Obtendo coordenadas do ponto
    pontoX, pontoY = [int(v) for v in linha.split()]

    # Lendo arquivo da posição e raio dos círculos
    circulos = open(arquivoCirculos + ".txt", "r")

    # Para cada um dos círculos definidos no arquivo de entrada...
    for circulo in circulos:
        # ...obtemos suas coordenadas e raio...
        circuloX, circuloY, raio = [int(v) for v in circulo.split()]

        # ...e calculamos a distância euclidiana entre o centro do círculo e o ponto.
        if (distanciaEuclidiana(pontoX, pontoY, circuloX, circuloY) > raio): continue
        else:
            circulos.close() # para garantir que vamos fechar o arquivo caso o ponto esteja dentro de um círculo

            # Se o ponto estiver dentro de qualquer círculo, ele é removido do arquivo
            return False
        
    # Fechando arquivo
    circulos.close()

    # Se o ponto estiver fora de todos os círculos, ele será mantido no arquivo
    return True

# Calcula a distância euclidiana entre 2 pontos no espaço 2D
def distanciaEuclidiana(pontoX, pontoY, circuloX, circuloY):
    return( ( (pontoX - circuloX)**2 + (pontoY - circuloY)**2 ) ** (1/2) )

# Fim dos subprogramas ----------

# Programa principal

# Recebendo nome do arquivo que contém os pontos
arquivoPontos = str(input("Entre com o nome do arquivo que contém os pontos:"))

# Recebendo nome do arquivo que contém os círculos
arquivoCirculos = str(input("Entre com o nome do arquivo que contém os circulos:"))

# Imprimindo conteúdo dos arquivos
imprime(arquivoPontos)
imprime(arquivoCirculos)

# Removendo os pontos que estiverem dentro dos círculos
removePontos(arquivoPontos, arquivoCirculos)

# Lendo os dados após a remoção dos pontos e imprimindo
imprime(arquivoPontos, remocao = True)