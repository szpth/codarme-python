# Suponha o seguinte programa:
# Alunos e suas respectivas notas
# alunos = [
#     ("Alice", 8),
#     ("Bob", 7),
#     ("Carlos", 9),
# ]
# Escreva uma programa que calcula a média das notas de todos os alunos.

alunos = [
    {
        "nome": "Alice",
        "nota": 8,
    },
    {
        "nome": "Bob",
        "nota": 7,
    },
    {
        "nome": "Carlos",
        "nota": 9,
    }
]

i, value = 0, 0

for i in alunos:
    value = value + i["nota"]
    
print(value // len(alunos))
