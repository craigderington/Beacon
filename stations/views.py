from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.template import Context, loader, TemplateDoesNotExist
from django.template.context import RequestContext
from .models import RadioStation, Office

#from .form import MyForm

# Create your views here.
def index(request):
    if request:
        context = RequestContext(request)
        stations = RadioStation.objects.all().order_by('radio_station_call_sign')

        if search:
            stations = stations.filter(
                Q(radio_station_call_sign__icontains=search) |
                Q(radio_station_band__icontains=search) |
                Q(radio_station_format__icontains=search)
            ).distinct()

        request.context.update({
            'stations' : stations,
        })

        template = loader.get_template('index.html')
        return HttpResponse(template.render(request.context))
