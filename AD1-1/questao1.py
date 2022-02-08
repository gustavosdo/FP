#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Este código apresenta uma possível
solução para a primeira questão da AD1-1 do
curso de Fundamentos de Programação (CEDERJ)
do semestre 2022.1

O problema fundamental definido pela questão
é a conversão de um valor monetário em um número mínimo
de cédulas (incluindo moedas de 1) """

# O desenho do código é baseado em uma estrutura de repetição indefinida (loop while):
# a chave para interromper a execução do loop é a entrada nula como valor para troca
entradaValida = True

# Início do loop: neste ponto certamente entradaValida é True
while entradaValida:

    # Entrada do valor a ser trocado em cédulas e moedas
    valorParaTroca = input()

    # Estrutura de seleção de dois ramos para interromper imediatamente a execução caso um valor vazio seja dado como entrada
    if valorParaTroca == "":
        entradaValida = False
    # Ou continuar caso o valor dado na entrada seja válido
    else:
        # Para realizar as contas corretamente é necessário converter a entrada para tipo inteiro
        valorParaTroca = int(valorParaTroca)

        # Antes de iniciar as contas imprimimos uma mensagem padrão para informar o valor de entrada
        print("Trocando", valorParaTroca, "em:")

        # Como os cálculos são facilmente generalizados, podemos aplicar uma estrutura de repetição definida pelos valores de cada cédula
        # Começamos por encontrar qual é o valor possível de ser recertido para as notas de 100 já que elas são as de maior valor nesse caso
        for nota in [100, 50, 20, 10, 5, 2, 1]:
            # i) o resto da divisão entre o valor total e o valor por nota (valorParaTroca % nota) nos diz tudo que não pode ser convertido nessas notas
            # ii) então tudo que pode ser convertido nessas notas será dado simplesmente pela subtração do valor total e o resto da divisão de (i)
            valorNotas = valorParaTroca - (valorParaTroca % nota)

            # O número de cádulas/moedas é simplesmente o valor total em notas dividido pelo valor de cada cédula
            quantidadeNotas = int(valorNotas/nota)

            # Aplicamos uma estrutura de dois ramos para imprimir uma mensagem caso o número de notas seja positivo para lidar corretamente com a concordância nominal
            if quantidadeNotas == 1:
                # E também utilizamos a mesma estrutura para lidar com a impressão do nome correto: moedas ou notas
                if nota > 1:
                    print("   1 nota de", nota, "reais")
                else:
                    print("   1 moeda de", nota, "real")
            elif quantidadeNotas > 1:
                if nota > 1:
                    print("  ", quantidadeNotas,"notas de", nota, "reais")
                else:
                    print("  ", quantidadeNotas,"moedas de", nota, "real")

            # Atualizamos o valor que deverá ser convertido nas próximas cédulas/moedas
            valorParaTroca = valorParaTroca - valorNotas