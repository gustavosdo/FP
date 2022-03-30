#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Faça um programa que leia um vetor X[10]. Substitua a seguir, todos os valores nulos e
negativos do vetor X por 1. Em seguida mostre o vetor X. """

# Definindo o vetor
X = []

# Percorrendo os índices deste
for indice in range(10):

    # Recebendo o vetor de entrada
    X.append(int(input()))

    # Testando o sinal do valor inserido
    if X[indice] < 0:
        # Alterando sinal caso seja negativo
        X[indice] = -X[indice]
    
    # Imprimindo resultado
    print("X[%d] = %d" % (indice, X[indice]))