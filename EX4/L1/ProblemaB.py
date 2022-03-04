#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Problema B: Plano de Dieta
https://www.urionlinejudge.com.br/judge/pt/problems/view/1248 """

# Função para separar os caracteres de uma string
def separaString(string):
    
    # Alfabeto completo
    todasLetras = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    
    # Testando casos triviais
    if (string != None) and (string != ""):

        # Caso tenhamos uma string não-trivial, checamos a presença de cada letra
        n = 0
        while len(todasLetras) != len(string):

            # Se a letra estiver presente na string, pule para a próxima letra
            if todasLetras[n] in string: n = n + 1

            # Caso não esteja, remova esta letra do conjunto (neste caso pular para a próxima significa manter n inalterado)
            else: del todasLetras[n]

        # Após checar cada letra, retornar as letras contidas na string
        return todasLetras
    
    # No caso trivial retornar string vazia
    else:
        return ""
# Fim da função que separa caracteres de uma string


# Função que determina o jantar necessário para que a dieta seja cumprida
def jantarRecomendado(alimentacao):

    # Reconhecendo alimentação em cada refeição
    dieta = separaString(alimentacao[0])
    cafe = separaString(alimentacao[1])
    almoco = separaString(alimentacao[2])

    #
    print(dieta)
    print(cafe)
    print(almoco)

    #
    return None

# Recebendo dados de entrada: quantidade de casos de teste
qtdTestes = int(input())

# Alimentação recomendada, café da manhã e almoço para cada teste
for i in range(qtdTestes):
    alimentacao = [0, 0, 0]
    for j in range(3):
        alimentacao[j] = str(input())
    
    print(jantarRecomendado(alimentacao))