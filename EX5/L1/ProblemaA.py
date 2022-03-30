#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Sua tarefa é, dada uma linha de texto, indicar se ele cabe ou não cabe em um formulário com 80 caracteres.
Entrada: uma linha de texto L (1 <= |L| <= 500)
Saída: A saída é dada em uma única linha. Ela deve ser YES se a linha de texto
L tem até 80 caracteres. Se L tem mais de 80 caracteres, a saída deve ser NO."""

# Recebendo a entrada da linha de texto
L = str(input("Entre com um nome:"))

# Testando se a string fornecida tem tamanho adequado
if len(L) <= 80:
    print("YES")
else:
    print("NO")