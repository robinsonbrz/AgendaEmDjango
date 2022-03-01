from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import Contato


def index(request):
    contatos = Contato.objects.order_by('-id').filter(
        mostrar=True
    )
    paginator = Paginator(contatos, 25)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    contatos = paginator.get_page(page_number)
    return render(request, 'contatos/index.html', {
        'contatos': contatos,
    })


def ver_contato(request, contato_id):
    contato = get_object_or_404(Contato, id=contato_id)
    if not contato.mostrar:   # evita forçar páginas de número não permitidas mostrar
        raise Http404()

    return render(request, 'contatos/ver_contato.html', {
        'contato': contato
    })
