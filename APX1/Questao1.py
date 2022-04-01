# Subprogramas -----

# Função para receber os valores 
def recebeValores():

    # Variável local de armazenamento dos dados
    todosValores = list()

    # Recebendo a primeira linha de valores
    linhaValores = [float(v) for v in input().split()]

    # Loop para repetir tomada de valores
    while(linhaValores):
        # Determinando maior e menor valores
        encontraMinimoMaximo(linhaValores)

        # Salvando linha atual
        todosValores.append(linhaValores)

        # Recebendo uma nova linha de valores
        linhaValores = [float(v) for v in input().split()]

    return todosValores

# Função para encontrar o menor e o maior valores
def encontraMinimoMaximo(valores):

    # Iniciando valores
    min = valores[0]
    max = valores[0]

    # Correndo todos os valores do vetor a fim de determinar o menor e o maior valores
    for indice in range(1, len(valores)):
        if   valores[indice] < min: min = valores[indice]
        elif valores[indice] > max: max = valores[indice]

    # Imprimindo o resultado para cada linha
    print("Menor:", min, "Maior:", max)

    return None

# Fim da seção de subprogramas -----

# Programa principal

valores = recebeValores()

if len(valores) == 0:
    print("Nenhum Número Foi Lido. Portanto, não existe média!!!")

else:
    # Desempacotando os valores (flatten list)
    valores = [item for sublist in valores for item in sublist]

    # Retornando resultados ao usuário
    print("Quantidade de Números Lidos: %d" % len(valores))
    print("Média dos Números Lidos: %.2f" %(sum(valores)/len(valores)) )