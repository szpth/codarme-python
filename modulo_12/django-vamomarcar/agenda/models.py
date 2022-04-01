from uuid import uuid4
from django.db import models


class StandardModelMixin(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4,
                            editable=False, verbose_name="ID")
    created_at = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name="Created at")
    updated_at = models.DateTimeField(
        auto_now=True, editable=False, verbose_name="Updated at")

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.nome}"


class Categoria(StandardModelMixin):
    nome = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return f"{self.nome}"

    @classmethod
    def criar_categoria(self, nome):
        if nome == '' or nome == None:
            raise ValueError("A categoria deve possuir um nome!")
        categoria = Categoria(nome=nome)
        categoria.save()
        return categoria


class Evento(StandardModelMixin):
    nome = models.CharField(max_length=256)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, null=True)
    local = models.CharField(max_length=256, blank=True)
    link = models.URLField(max_length=256, blank=True)
    data = models.DateField(null=True, verbose_name="Data do Evento")
    participantes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nome}"

    @classmethod
    def criar_evento(self, nome, categoria, local='', link='', data=None, participantes=0):
        self.nome = nome
        self.categoria = categoria
        self.local = local
        self.link = link
        self.data = data
        self.participantes = participantes

        if local == '' or link == None:
            raise ValueError("O evento não pode possuir local e link!")
        elif local == None or link == '':
            raise ValueError("O evento não pode possuir local e link!")
        elif local and link:
            raise ValueError("O evento deve possuir local ou link!")
        else:
            Evento(self)
            
        return Evento(self)