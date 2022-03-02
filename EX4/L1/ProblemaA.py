#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Dados os comprimentos de quatro varetas, é ou não é possível selecionar três varetas,
dentre as quatro, e formar um triângulo?

Para que 3 varetas formem um triângulo é necessário e suficiente que a soma dos
comprimentos das duas varetas menores seja maior que o comprimento da vareta maior. """

# Função para ordenar um conjunto de valores em ordem crescente
def ordenaComprimentos(comprimentos, n):

    # Utilizando recursividade: condição de interrupção
    if n == 0:
        return(comprimentos)
    else:
        # Iniciamos tomando o último valor do vetor como o maior
        maior = comprimentos[n]

        # Iterativamente verificamos a validade dessa hipótese inicial comparando com cada elemento do conjunto de valores
        for ind in range(0, n):
            valor = comprimentos[ind]
            if valor > maior:
                comprimentos[n] = valor
                comprimentos[ind] = maior
                maior = valor
        return ordenaComprimentos(comprimentos, n - 1)
# Fim da função de ordenamento

# Primeiro recebemos os valores dos comprimento separados por espaço em uma única linha
inputComprimentos = input().split(" ")

# Convertemos para o tipo inteiro e formamos uma base de dados estruturada
comprimentos = [int(inputComprimentos[0]), int(inputComprimentos[1]), int(inputComprimentos[2]), int(inputComprimentos[3])]

# Como o cálculo a ser feito indica o comprimento da maior vareta como referência usamos uma função de ordenamento
comprimentosOrdenados = ordenaComprimentos(comprimentos, len(comprimentos) - 1)

# Número de triângulos viáveis pelo método da soma dos lados menores
nTri = 0

# Encontramos as combinações possíveis de 3 valores dentro do conjunto dos 4 valores dados
# e com esses 3 valores tentamos estabelecer um triângulo pela regra da soma dos menores lados
for ind1 in range(len(comprimentos)):
    for ind2 in range(ind1 + 1, len(comprimentos)):
        for ind3 in range(ind2 + 1, len(comprimentos)):
            if comprimentos[ind1] + comprimentos[ind2] > comprimentos[ind3]:
                nTri = nTri + 1

if nTri > 0:
    print('S')
else:
    print('N')