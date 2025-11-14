from django.shortcuts import render, get_object_or_404
from .models import Tournament, Registration
from django.shortcuts import render
from .models import Tournament


def inicio(request):
    torneos_destacados = Tournament.objects.filter(status='UPCOMING')[:3]
    return render(request, 'torneos/inicio.html', {
        'torneos_destacados': torneos_destacados
    })


def catalogo(request):
    tipo = request.GET.get('tipo', 'proximos')
    if tipo == 'realizados':
        torneos = Tournament.objects.filter(status='DONE')
        titulo = "Torneos realizados"
    else:
        torneos = Tournament.objects.filter(status='UPCOMING')
        titulo = "Próximos torneos"
    return render(request, 'torneos/catalogo.html', {
        'torneos': torneos,
        'titulo': titulo,
        'tipo': tipo,
    })


def detalle_torneo(request, pk):
    torneo = get_object_or_404(Tournament, pk=pk)
    equipos_registrados = Registration.objects.filter(
        torneo=torneo,
        status='APPROVED'
    ).select_related('equipo')
    return render(request, 'torneos/detalle_torneo.html', {
        'torneo': torneo,
        'equipos_registrados': equipos_registrados,
    })



def preinscripcion(request):
    torneos = Tournament.objects.filter(status='UPCOMING').order_by('fecha_inicio')

    return render(request, 'torneos/preinscripcion.html', {
        'torneos': torneos
    })
