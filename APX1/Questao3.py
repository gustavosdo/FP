# Subprogramas -----

# Função para determinar se uma entrada é float (letra a)
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

# Função para converter uma entrada para float caso seja possível (letra b)
def converteParaFloat(entrada):

    # Caso seja possível converter a entrada em float, faça
    try:
        entradaFloat = float(entrada)
        return(entradaFloat)

    # em casos de exceção buscamos a justificativa
    except:
        # Contador de pontos
        contadorPontos = 0

        # Índices onde ocorrem caracteres não-numéricos
        naoNumericos = list()

        # Vamos analisar cada caractere da entrada inserida
        for indice in range(len(entrada)):
            char = entrada[indice]

            # Um float é composto de apenas dígitos numéricos, até um "." e nenhum caractere não-numérico (p.ex.: alfabeto)
            if (char >= '0' and char <= '9'):
                pass
            elif (char == "."):
                contadorPontos = contadorPontos + 1
            else:
                naoNumericos.append(indice)

        # Aplicando os vínculos aos contadores e reportando o problema ao usuário
        if (contadorPontos > 1):
            print("Há mais do que um \".\".")
        if (len(naoNumericos) > 0):
            for indice in naoNumericos:
                print("Você digitou errado, "+entrada+" não é do tipo float.")
                print("Na posição "+str(indice+1)+" há o caractere "+entrada[indice]+".")
        
        return None

# Função para converter um valor (float) em USD para BRL usando uma taxa inserida pelo usuário (letra c)
def converteMoeda(valorUSD, cambioBRL):

    # Convertendo valores para float
    valorUSD = converteParaFloat(valorUSD)
    cambioBRL = converteParaFloat(cambioBRL)

    # Terminando execução em caso de erro
    if (valorUSD == None) or (cambioBRL == None):
        return None
    
    # Caso os valores estejam corretamente convertidos podemos aplicar a taxa de câmbio
    valorBRL = valorUSD * cambioBRL

    print(f"O valor {valorUSD:.3f} USD com a taxa {cambioBRL:.3f} vai para {valorBRL:.3f} BRL")

    return valorBRL

# Função que aplica um desconto de 15% a um valor de entrada (letra d)
def aplicaDesconto(valor):
    return(valor * 0.85)

# Função para determinar o valor devido, a aplicação de desconto ou de juros e a exibição do valor por parcela (letra e)
def pagamento(valor, cambio):

    # Convertendo o valor original pelo câmbio
    valor = converteMoeda(valor, cambio)

    # Interrompendo a execução caso haja um erro na conversão
    if valor == None:
        return None
    else:
        # Coletando do usuário a escolha da quantidade de meses para o pagamento
        meses = int(input("Em quantas vezes você quer comprar o produto?"))

        # Aplicando desconto caso o pagamento seja à vista
        if (meses == 1):
            valorComDesconto = aplicaDesconto(valor)
            print(f"Você ganhou 15% de desconto, portanto, de {valor:.2f} BRL você vai pagar {valorComDesconto:.2f} BRL")
        # Aplicando juros compostos de 5% ao mês caso pagamento seja parcelado
        elif (meses > 1):
            valorComJuros = aplicaJurosCompostos(valor, taxa = 0.05, meses = meses)

            # Calculando valor da parcela mensal
            valorMensal = valorComJuros/meses
            print(f"Pagando em {meses} parcelas, e com 5% de juros ao mês, você pagará {valorMensal:.2f} BRL por mês, sendo o total de {valorComJuros:.2f} BRL")

    return None

# Função para aplicar juros compostos usando recursividade (auxiliar à letra e)
def aplicaJurosCompostos(valor, taxa, meses):
    # Condição de interrupção
    if meses == 0:
        return(valor)

    # Atualizando mês a mês o valor da compra
    else:
        valor = valor * (1 + taxa)
        return(aplicaJurosCompostos(valor, taxa, meses - 1))
# Fim da seção de subprogramas -----

# Testes sugeridos no enunciado
pagamento("2.2.2..22.", "23")
print("\n")
pagamento("123123s", "2")
print("\n")
pagamento("123", "2.5")
print("\n")
pagamento("123.5", "2.0")