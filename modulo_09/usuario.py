class Usuario():
    id = 1
    
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = f'{senha[0:5]}...'
        self.id = Usuario.id
        Usuario.id += 1
