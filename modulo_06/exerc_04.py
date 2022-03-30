# Suponha o seguinte programa:
# Alunos e suas respectivas notas
# alunos = [
#     ("Alice", 8),
#     ("Bob", 7),
#     ("Carlos", 9),
# ]
# Escreva uma programa que calcula a média das notas de todos os alunos.

alunos = [
    ("Alice", 8),
    ("Bob", 7),
    ("Carlos", 9),
]

c = 0

for d in alunos:
    c += d[1]
    value = c // len(alunos)

print(value)
