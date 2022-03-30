# Um número primo é um número que é divisível apenas por 1 e por ele mesmo.
# Escreva um programa que receba um número n e informe se esse número é primo
# ou não.

print("-------------------------------------------------------")
print("Números primos! ")
print("------------------------------------------------------- \n ")

value = int(input("Digite um número: "))

i, c = 2, True

while i < value and c == True:
    if (value % i) == 0:
        c = False
    i += 1

if c == True:
    print(f"{value}, é um número é primo!")
else:
    print(f"{value}, não é um número é primo!")
