# Escreva uma função que recebe um número inteiro positivo e retorna True caso ele
# seja primo e False , caso contrário.
# Sugestão:
    
def e_primo(n):
    i, c = 2, True

    while i < value and c == True:
        if (value % i) == 0:
            c = False
        i += 1

    if c == True:
        return True
    else:
        return False

print("-------------------------------------------------------")
print("Números primos! ")
print("------------------------------------------------------- \n ")

value = int(input("Digite um número: "))

result = e_primo(value)

print(result)