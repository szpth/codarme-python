# Implemente uma função  maior_idade(pessoa)  que receba uma tupla representando 
# uma pessoa com nome e idade e imprime na tela se a pessoa é maior de idade ou 
# não.

def maior_idade(pessoa):
    nome, idade = pessoa
    if idade >= 18:
        maior = print(f'{nome} é maior de idade.')
        return maior
    else:
        menor = print(f'{nome} é menor de idade.')
        return menor


pessoa = ("João", 20)

maior_idade(pessoa)