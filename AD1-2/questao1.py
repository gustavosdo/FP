#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Possível solução da questão 1 da AD1-2 do curso de
Fundamentos de Programação do CEDERJ (2022.1) """

# # # # # Subprogramas # # # # #

# Cálculo do número total de permutações de n inteiros
def fat(n):
    if n < 2:
        return 1
    else:
        return n * fat(n-1)
# Fim da função fat

# Função para checagem das restrições
def checaRestricoes(arranjo, restricoes = True):
    for elm in range(1, int(len(arranjo)/2)+1): # percorrer apenas elementos únicos
    
        indElm = []
        for ind in range(len(arranjo)):
            if arranjo[ind] == elm:
                indElm.append(ind)
                
        # Índice da primeira vez que o elemento surge
        indInicial = indElm[0]
        
        # Índice da repetição
        indRepeticao = indElm[1]

        # Para cada elemento, sua repetição deve ocorrer em indice + elemento + 1
        if (indInicial + elm + 1 != indRepeticao):
            restricoes = False

    return(restricoes)
# Fim da função checaRestricoes

# Função para encontrar todos as permutações possíveis de n números
def permutaN(iniArranjo, indice = 0, permutacoes = [], nPermutacoes = 0):

    # 1. Condição de interrupção (índice final):
    # não é preciso permutar nenhum elemento, temos uma sequência viável.
    # Falta checar se a sequência satisfaz as restrições
    if indice == len(iniArranjo):
        nPermutacoes = nPermutacoes + 1
        print(nPermutacoes)

        # Checar se a permutação satisfaz as restrições:
        restricoes = checaRestricoes(iniArranjo)

        # Se as restrições são satisfeitas, adicionar a sequência ao resultado a ser retornado
        if restricoes:
            permutacoes.append(iniArranjo)
            #print(permutacoes)
    
    # 2. Loop de permutação:
    # Permutaremos o elemento no índice dado com todos à direita deste mesmo elemento
    for i in range(indice, len(iniArranjo)):

        # Copiamos o arranjo inicial dado
        permutacao = []
        for j in range(0, len(iniArranjo)):
            permutacao.append(iniArranjo[j])

        # Permutamos o i-ésimo elemento com o elemento no indice dado
        permutacao[indice], permutacao[i] = permutacao[i], permutacao[indice]

        # Recursivamente atualizamos o índice e realizamos uma nova permutação
        permutaN(permutacao, indice + 1, permutacoes)
    
    # 3. Retorno do resultado:
    if (nPermutacoes == fat(len(iniArranjo))):
        return permutacoes
# Fim da função permutaN

# # # # # Programa principal # # # # #

# Entrada do valor inteiro n
n = int(input("Digite um número inteiro: "))

# Vamos criar todas as permutações de 1 até n e verificar se é possível construir uma sequência
# que respeite as restrições para cada permutação

# Criamos um vetor inicial simples ordenado de 1 a n
iniArranjo = []
for j in range(0, n):
    iniArranjo.append(j + 1)

iniArranjo = iniArranjo + iniArranjo

# Encontrando todos as permutações possíveis com os números de 1 a n
permutacoes = permutaN(iniArranjo = iniArranjo, indice = 0)

#print(permutacoes)
print(len(permutacoes))