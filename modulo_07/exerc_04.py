# Adapte a função  maior_idade(pessoa)  de forma que ela possa receber tanto uma 
# tupla quanto um dicionário. Dica: método  type  pode te ajudar.

def maior_idade(pessoa):
    set_age = 18

    if type(pessoa) == tuple:
        name, age = pessoa
        if age >= set_age:
            return f'{name} é maior de idade.'
        else:
            return f'{name} é menor de idade.'
    elif type(pessoa) == dict:
        for x in pessoa:
            if pessoa[x] >= set_age:
                return f'{x} é maior de idade.'
            else:
                return f'{x} é menor de idade.'

var_tuple = ("João", 20)

var_dict = {
    "Ana": 12
}

print(maior_idade(var_tuple))
print(maior_idade(var_dict))