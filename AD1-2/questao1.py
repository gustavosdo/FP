#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Possível solução da questão 1 da AD1-2 do curso de
Fundamentos de Programação do CEDERJ (2022.1) """

# # # # # Subprogramas # # # # #

# Função para checar se a restrição de repetição está sendo satisfeita
def checaRestricao(listaInteiros, listaNumeros):
    
    # Iniciamos criando uma chave de decisão
    restricaoSatisfeita = True

    inteiro = 1 # o primeiro inteiro é sempre 1

    # Se a restrição for quebrada para qualquer inteiro podemos imediatamente parar a execução
    while (inteiro <= max(listaInteiros) and restricaoSatisfeita):

        # Lista dos dois índices onde surge o inteiro
        indicesInteiro = []

        # Verificação se cada número na lista é o inteiro
        for indice in range(len(listaNumeros)):
            numero = listaNumeros[indice]
            if (numero == inteiro):
                indicesInteiro.append(indice)
        
        # Checando a restrição para este inteiro
        restricaoSatisfeita = (indicesInteiro[1] == indicesInteiro[0] + inteiro + 1)
        inteiro = inteiro + 1
    
    return restricaoSatisfeita
# Fim da função checaRestricao

# Função para permutar a lista de entrada
def permutaN(listaInteiros, listaNumeros, indice = 0, permutacoes = []):
    
    # Loop de permutação:
    # Permutaremos o elemento no índice dado com todos à direita deste mesmo elemento
    for i in range(indice, len(listaNumeros)):

        # Copiamos o arranjo inicial dado
        permutacao = []
        for j in range(0, len(listaNumeros)):
            permutacao.append(listaNumeros[j])

        # Permutamos o i-ésimo elemento com o elemento no indice dado
        permutacao[indice], permutacao[i] = permutacao[i], permutacao[indice]

        # Condição de aceitação: não foi adicionado previamente e obedece às restrições
        if (permutacao not in permutacoes) and (checaRestricao(listaInteiros, permutacao)):
            permutacoes.append(permutacao)

        # Recursivamente atualizamos o índice e realizamos uma nova permutação
        permutaN(listaInteiros, permutacao, indice + 1, permutacoes)
    
    # Retorno do resultado:
    return permutacoes
# Fim da função permutaN

# # # # # Programa principal # # # # #

# Entrada do valor inteiro n
n = int(input())

# Gerando uma lista com todos os inteiros de 1 até n (com duas aparições)
listaInteiros = [] # criando lista

# Preenchendo com a primeira aparição de cada inteiro
for indice in range(n):
    listaInteiros.append(indice + 1)

# Repetindo os números
listaNumeros = listaInteiros + listaInteiros

# Obtendo sequências que satisfazem as restrições
sequencias = permutaN(listaInteiros, listaNumeros)

# Retornando resultados ao usuário
if (len(sequencias) == 0):
    print("Não há sequências com o valor", n, "de entrada")
else:
    for seq in sequencias:
        print(seq)
    print("Há", len(sequencias), "sequências")