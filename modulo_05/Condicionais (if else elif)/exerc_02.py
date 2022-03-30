# Implemente uma calculadora que recebe 3 valores do usuário:
# a. Operando a (pode ser um inteiro ou float).
# b. Operando b (pode ser um inteiro ou float).
# c. Operador op .
# i. op pode ser uma string representando o operador, por exemplo, "+" ou "-
# ". Outra opção é utilizar números, por exemplo, 1 para soma , 2 para
# subtração , etc.
# O seu programa deve receber esses 3 valores e imprimir o resultado da operação.
# Caso o operador seja de divisão e o segundo operando seja o valor zero, o
# programa deve imprimir uma mensagem: “Não é possível realizar divisão por
# zero!”.

print("-------------------------------------------------------")
print("Vamos calcular?")
print("------------------------------------------------------- \n ")
a = float(input("Digite o primeiro valor: "))
op = input("Digite a operação... \n + para soma \n - para subtração \n * para multiplicação \n / para divisão \n \nInformar: ")
b = float(input("Digite o segundo valor: "))

if op == "+":
    print("A soma dos valores é: ", a + b)
elif op == "-":
    print("A subtração dos valores é: ", a - b)
elif op == "*":
    print("A multiplicação dos valores é: ", a * b)
elif op == "/":
    print("A divisão dos valores é: ", a / b)
else:
    print("Não é possível realizar divisão por zero!")
