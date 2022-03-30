# Implemente uma função que recebe uma lista de números inteiros e retorna uma
# tupla (pos, num) , onde pos é a posição (ou índice) do maior número na lista e num
# é o valor desse número.

def insert_list():
    i, n, p  = 0, 0, 0
    sx = []
    
    while i < 5:
        i += 1
        value = input("Digite um número: ")
        sx.append(int(value))

    l = len(sx)
    
    for c in range(0, l):
        if sx[c] > n:
            p = c
            n = sx[c]

    return (p, n)

value = insert_list()

print(value)
