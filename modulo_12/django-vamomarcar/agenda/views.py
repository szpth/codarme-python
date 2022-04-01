from datetime import date
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from agenda.models import Categoria, Evento


def listar_eventos(request):
    eventos = Evento.objects.filter(
        data__gte=date.today()).order_by("data", 'nome')

    return render(
        request=request,
        context={
            "eventos": eventos
        },
        template_name="agenda/listar_eventos.html"
    )


def exibir_evento(request, uuid):
    evento = get_object_or_404(Evento, uuid=uuid)
    evento = Evento.objects.get(uuid=uuid)

    return render(
        request=request,
        template_name="agenda/exibir_evento.html",
        context={
            "evento": evento
        }
    )


def participar_evento(request):
    evento_uuid = request.POST.get("evento_uuid")
    evento = get_object_or_404(Evento, uuid=evento_uuid)
    evento.participantes += 1
    evento.save()

    return HttpResponseRedirect(reverse('exibir_evento', kwargs={"uuid": evento_uuid}))


def listar_categorias(request):
    categorias = Categoria.objects.all().order_by('nome')

    return render(
        request=request,
        context={
            "categorias": categorias
        },
        template_name="agenda/listar_categorias.html"
    )


def exibir_categoria(request, uuid):
    categoria = get_object_or_404(Categoria, uuid=uuid)
    categoria = Categoria.objects.get(uuid=uuid)

    eventos = Evento.objects.filter(
        categoria__uuid=uuid, data__gte=date.today())
    qtd_eventos = eventos.count()

    return render(
        request=request,
        template_name="agenda/exibir_categoria.html",
        context={
            "categoria": categoria,
            "eventos": qtd_eventos
        }
    )
