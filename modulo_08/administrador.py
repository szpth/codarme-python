# 2. Módulo administrador.py
# 	1. Deve conter uma classe Administrador que estende (herda de) Usuario.
# 	2. Deve sobrescrever o método imprime_usuario e imprimir:
#   "Gabriel (gabriel@exemplo.com) – Administrador", para uma instância com
#   nome = "Gabriel" e email = "gabriel@exemplo.com”

from usuario import Usuario

class Administrador(Usuario):
    def __init__(self, nome, email):
        super().__init__(nome, email)
        
    
    def imprime_usuario(self):
        print(f'{self.nome} ({self.email}) – Administrador')
        print('------------------------------')