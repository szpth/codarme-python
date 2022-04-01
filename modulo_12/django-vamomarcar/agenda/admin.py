from django.contrib import admin

from agenda.models import Categoria, Evento


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ['uuid', 'created_at', 'updated_at',
                    'nome', 'categoria', 'data', 'participantes']

    # define search columns list, then a search box will be added at the top of Department list page.
    search_fields = ['nome', 'categoria']

    # define filter columns list, then a filter widget will be shown at right side of Department list page.
    list_filter = ['created_at', 'updated_at', 'categoria']


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['uuid', 'created_at', 'updated_at', 'nome']

    # define search columns list, then a search box will be added at the top of Department list page.
    search_fields = ['nome']

    # define filter columns list, then a filter widget will be shown at right side of Department list page.
    list_filter = ['created_at', 'updated_at']
