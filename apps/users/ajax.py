from django.http import JsonResponse
from apps.covid.models import Departamento, Municipio


def get_municipios(request):
    departamento_id = request.GET.get('departamento_id')
    municipios = Municipio.objects.none()
    options = '<option value="" selected="selected">Seleccione...</option>'
    if departamento_id:
        municipios = Municipio.objects.filter(departamento_id=departamento_id)   
    for municipio in municipios:
        options += '<option value="%s">%s</option>' % (
            municipio.pk,
            municipio.nombre_municipio
        )
    response = {}
    response['municipios'] = options
    return JsonResponse(response)

