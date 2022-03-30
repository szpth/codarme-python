# Escreva um programa que receba um número inteiro n e imprima todos os
# números pares de 1 até n (inclusive n ).

n = int(input("Digite um número: "))

i = 1

while i <= n:
    if i % 2 == 0:
        print(i)
    i += 1

print("Fim do programa!")
