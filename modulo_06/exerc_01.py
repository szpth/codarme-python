# Escreva um programa que lê números inteiros positivos do usuário, um após o
# outro, e monta uma lista a partir desses números e depois imprime a lista montada.
# O programa deve continuar solicitando por números até que o elemento digitado
# seja um número negativo (que não deve ser inserido na lista).

print("-------------------------------------------------------")
print("Vamos montar uma lista?")
print("------------------------------------------------------- \n ")

lista = []

input_lista = int(input("Digite um número: "))

while input_lista >= 0:
    lista.append(input_lista)
    input_lista = int(input("Digite um número: "))

print(lista)
