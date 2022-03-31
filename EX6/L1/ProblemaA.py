# Começamos definindo uma lista das faixas de valores e seus respectivos aumentos
salarios = [0,  400.00, 800.00, 1200.00, 2000.00]
aumentos = [0.15, 0.12,   0.10,    0.07,    0.04]

# Recebemos, então, a entrada do valor atual do salário do funcionário
salarioAtual = float(input("Entre com o valor atual do salário do funcionário:"))

# Subprograma: busca da faixa em que está o salário atual -----
def buscaFaixa(lista, valor):
    indice = 0
    
    while (valor - lista[indice] > 0) and (indice < len(lista) - 1):
        indice = indice + 1
    
    return(indice - 1)
# Fim do subprograma buscaFaixa

# Aumento percentual
aumentoPerc = aumentos[buscaFaixa(salarios, salarioAtual)]

# Aumento
aumento = salarioAtual * aumentoPerc

# Novo salário
novoSalario = salarioAtual + aumento

# Imprmindo resultados (aqui faltou apenas colocar em 2 dígitos)
print("Novo salario: "+str(novoSalario))
print("Reajuste ganho: "+str(aumento))
print("Em percentual: "+str(10*aumentoPerc)+"%")