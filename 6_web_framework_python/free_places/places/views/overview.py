from django.shortcuts import render

from places.models import Place, Establishment


def overview(request):
    # places = Place.objects.filter(status='vacant')
    context = {
        'places': Place.objects.filter(status='vacant'),
        'establishments': Establishment.objects.all(),
    }
    return render(request, 'overview.html', context)
