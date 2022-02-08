#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Este código apresenta uma possível
solução para a primeira questão da AD1-1 do
curso de Fundamentos de Programação (CEDERJ)
do semestre 2022.1

O objetivo deste código é realizar teste(s) estatístico(s)
dos dados inseridos em relação ao(s) intervalo(s) também
fornecido(s) pelo usuário"""

# A primeira entrada diz respeito ao número de testes que será realizado
qtdTestes = int(input())

# Também devemos saber o número de dados que serão inseridos
qtdValoresTeste = int(input())

# Lemos os valores mínimo e máximo para o intervalo de teste
minIntervalo = float(input())
maxIntervalo = float(input())

# Após isso lemos a coleção de dados numéricos para o teste e realizamos os testes
for i in range(0, qtdTestes):

    # Iniciando os resultados estatísiticos
    abaixoIntervalo, noIntervalo, acimaIntervalo, somaIntervalo = 0, 0, 0, 0

    for j in range(0, qtdValoresTeste):
        # Tomando o valor do dado
        dado = float(input())

        # Realizando os testes
        if dado < minIntervalo:
            abaixoIntervalo = abaixoIntervalo + 1
        elif dado > maxIntervalo:
            acimaIntervalo = acimaIntervalo + 1
        elif dado >= minIntervalo and dado <= maxIntervalo:
            noIntervalo = noIntervalo + 1
            somaIntervalo = somaIntervalo + dado
        
    # Iniciando o retorno dos resultados para o usuário
    print("Teste", i+1, "\b:")
    print("   Intervalo:", [minIntervalo, maxIntervalo])

    # Imprimindo os resultados
    print("   Abaixo do Intervalo:", abaixoIntervalo, "\b, No Intervalo:", noIntervalo, "\b, Acima do Intervalo:", acimaIntervalo)
    print("   Soma de Valores no Intervalo: %.1f" % somaIntervalo)