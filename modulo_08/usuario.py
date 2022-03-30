# 1. Módulo usuario.py
# 	1. Deve conter uma classe Usuario

# 	2. Classe Usuario deve ter um construtor que recebe nome e email

# 	3. Classe Usuario deve possuir um método de instância imprime_usuario que imprime:
# 		"Gabriel (gabriel@exemplo.com)", para uma instância
#       com nome = "Gabriel" e email = "gabriel@exemplo.com"

# 	4. Classe Usuario deve possuir um atributo de classe quantidade que
# 		armazena a quantidade de instâncias criadas, sejam instâncias
#       de Usuario ou de qualquer classe que estenda Usuario. Por exemplo:
#       Administrador(Usuario).
class Usuario:
    quantidade = 0
    
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.quantidade = Usuario.quantidade
        Usuario.quantidade += 1

    def imprime_usuario(self):
        print(f'{self.nome} ({self.email})')
