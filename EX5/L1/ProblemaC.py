#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Faça um programa que leia um valor e apresente o número de Fibonacci correspondente
a este valor lido. Lembre que os 2 primeiros elementos da série de Fibonacci são 0 e 1 e
cada próximo termo é a soma dos 2 anteriores a ele. Todos os valores de Fibonacci
calculados neste problema devem caber em um inteiro de 64 bits sem sinal.

Entrada
A primeira linha da entrada contém um inteiro T, indicando o número de casos de teste.
Cada caso de teste contém um único inteiro N (0 <= N <= 60), correspondente ao N-ésimo
termo da série de Fibonacci.

Saída
Para cada caso de teste da entrada, imprima a mensagem Fib(N) = X, onde X é o
N-ésimo termo da série de Fibonacci. """

# Obtendo número de testes
nTestes = int(input())

# Obtendo os elementos para os quais queremos calcular fib(n)
elementos = []
for indice in range(nTestes):
    elementos.append(int(input()))

# Valores fundamentais de Fibonacci
fib = [0, 1]

# Calculando a série de Fibonacci a partir destes valores fundamentais
for indice in range(2, max(elementos) + 1):
    fib.append(fib[indice - 2] + fib[indice - 1])

# Imprimindo resultados
for elemento in elementos:
    print("Fib[%d] = %d" % (elemento, fib[elemento]))