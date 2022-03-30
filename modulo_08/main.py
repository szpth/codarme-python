# 3. Módulo main.py
#     1. Deve importar os módulos usuario.py e administrador.py.

#     2. Deve ser executado contendo as instruções abaixo:
#         > u = Usuario("Gabriel", "gabriel@exemplo.com")
#         a = Usuario("Admin", "admin@exemplo.com")
#         > u.imprime_usuario()
#         => "Gabriel (gabriel@exemplo.com)
#         > a.imprime_usuario()
#         => "Admin (admin@exemplo.com) – Administrador"
#         > print(Usuario.quantidade)
#         => 2

from usuario import Usuario
from administrador import Administrador

u = Usuario("Gabriel", "gabriel@exemplo.com")
a = Administrador("Admin", "admin@exemplo.com")

u.imprime_usuario()
# => "Gabriel (gabriel@exemplo.com)

a.imprime_usuario()
# => "Admin (admin@exemplo.com) – Administrador"

print(Usuario.quantidade)
# => 2