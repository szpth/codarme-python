# Escreva um programa com as seguintes especificações:
# Uma variável “valor_compras” que receba um valor do tipo float, representando
# o valor total das compras.
# Uma variável “desconto” que receba um valor do tipo float, representando o
# desconto a ser aplicado sobre o valor total das compras.
# Uma variável “quantidade_itens”, que represente a quantidade de itens que
# foram comprados.
# Seu programa deve imprimir dois resultados:
# 1. O valor final das compras, considerando o desconto aplicado.
# 2. O custo médio de cada item (considerando o valor final das compras).
# 💡 Lembre que podemos utilizar símbolos como + - * / para fazer cálculos
# em Python.

valor_compras = float(input("Digite o valor das compras: "))
valor_desconto = float("{:.2f}".format(valor_compras * 0.15))
valor_total = float("{:.2f}".format(valor_compras - valor_desconto))
quantidade_itens = int(input("Digite a quantidade de itens: "))
valor_medio = float("{:.2f}".format(valor_total / quantidade_itens))

print("-------------------------------------------------------")
print("Valor das compras: R$", valor_compras)
print("Desconto aplicado (15%): R$", valor_desconto)
print("Valor médio por item: R$", valor_medio)
print("-------------------------------------------------------")
print("Valor total a ser pago: R$", valor_total)
print("-------------------------------------------------------")
