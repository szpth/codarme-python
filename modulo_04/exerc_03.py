# Considere o programa abaixo
# resultado = 2 + 3 * 2 ** 2
# print(resultado)
# É possível conseguir resultados diferentes, sem alterar os números e operadores,
# apenas com a utilização de parênteses. Por exemplo:
# resultado = (2 + 3) * 2 ** 2
# print(resultado)
# > 20
# Utilize parênteses de modo que o programa imprima os seguintes resultados:
# > 14
# > 38
# > 100

resultado1 = 2 + (3 * 2 ** 2)
resultado2 = 2 + (3 * 2) ** 2
resultado3 = ((2 + 3) * 2) ** 2

print(resultado1, resultado2, resultado3)
