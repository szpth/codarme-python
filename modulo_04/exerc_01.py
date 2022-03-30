# Escreva um programa que receba um número inteiro do usuário e imprima True
# caso o número seja par e False, caso o número seja ímpar

value = input('Digite um valor: ')
value = int(value)
result = value % 2

print("O valor digitado foi par? ", result == 0)

