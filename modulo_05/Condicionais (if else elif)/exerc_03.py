# Escreva um programa de autenticação que receba um nome de usuário e senha
# ( input ) informe se:
# Exercícios – Controle de Fluxo 2
# Autenticação foi bem-sucedida.
# Se o nome de usuário não existe.
# Se a senha está incorreta.
# Os valores corretos de nome de usuário e senha devem estar armazenados em
# constantes, como no exemplo abaixo:
# USUARIO = "admin"
# SENHA = "123123"
# nome_usuario = input("Digite o nome do usuário: "\n)
# ...

user, pwd = "admin", "123123"

user_input = input("Digite o nome do usuário: ")

if user_input == user:
    senha = input("Digite a senha: ")
    if senha == pwd:
        print("-------------------------------------------------------")
        print("Autenticação foi bem-sucedida!")
        print("-------------------------------------------------------")
    else:
        print("########################################################")
        print("Senha incorreta!")
        print("########################################################")
else:
    print("////////////////////////////////////////////////////////////")
    print("Usuário não localizado!")
    print("////////////////////////////////////////////////////////////")
