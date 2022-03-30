# Implemente uma função que recebe dois argumentos, uma lista e um 
# elemento, e retorna  True  caso  elemento  seja encontrado na lista,
# e False caso contrário. Não é permitido utilizar o método in.

""" 
# Teste convertendo a lista em dict
# ...
def search_list(list, element):
    dict_list = dict(zip(list,list))
    
    checking = dict_list.get(element, True)
    if checking == element:
        return True
    return False
"""
 
def search_list(list, element):
    for i in list:
        if i == element:
            return True
    return False

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
search = 7

print(search_list(values, search))