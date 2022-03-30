# DESAFIO. Escreva um programa que dado uma lista de números inteiros, imprime
# o maior número dessa lista.
# lista = [1, 3, 2, 5]
# ...
# Deve imprimir 5

lista = [1, 3, 2, 5]

lista.sort(reverse=True)

print(lista[0])
