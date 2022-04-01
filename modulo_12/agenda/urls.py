from django.urls import path

from agenda.views import exibir_categoria, exibir_evento, listar_categorias, listar_eventos, participar_evento


urlpatterns = [
    path('eventos/', listar_eventos, name='listar_eventos'),
    path('eventos/<str:uuid>/', exibir_evento, name='exibir_evento'),
    path('participar/', participar_evento, name='participar_evento'),
    path('categorias/', listar_categorias, name='listar_categorias'),
    path('categorias/<str:uuid>/', exibir_categoria, name='exibir_categoria'),
]
