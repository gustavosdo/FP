# Subprogramas -----

# Função que recebe o número de nomes e os nomes
def recebeNumeroNomes():

    # Iniciamos definindo o número de nomes (strings) a serem recebidas
    quantidadeNomes = int(input("Quantidade de nomes:"))

    # Definindo uma lista de strings onde serão armazenados os nomes
    nomes = quantidadeNomes * [""]

    # Recebendo os nomes
    for indice in range(len(nomes)):
        nomes[indice] = str(input("Digite o "+str(indice + 1)+"º nome:"))

    # Retornando os nomes para o programa principal
    return nomes

# Função que suprime os nomes do meio
def suprimeNomesMeio(nomes):

    for indice in range(len(nomes)):

        # Para cada nome contido na lista...
        nome = nomes[indice]

        # realizamos a separação por espaço
        nomeSeparado = nome.split()

        # e armazenamos o primeiro e o último nome
        nomes[indice] =  nomeSeparado[0] + " " + nomeSeparado[len(nomeSeparado) - 1]
    
    return nomes

# Fim da seção de subprogramas -----

# Programa principal -----

# Obtendo a lista de nomes
nomes = recebeNumeroNomes()

# Processando os nomes: remover todos os nomes do meio
nomesSuprimidos = suprimeNomesMeio(nomes)

# Imprimindo resultado
print(*nomesSuprimidos, sep = "\n")