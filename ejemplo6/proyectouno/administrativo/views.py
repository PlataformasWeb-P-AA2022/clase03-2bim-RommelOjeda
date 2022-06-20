from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render

# importar las clases de models.py
from administrativo.models import Matricula

# vista que permita presesentar las matriculas
# el nombre de la vista es index.
def index(request):
    """
        Listar los registros del modelo Estudiante,
        obtenidos de la base de datos.
    """

    matricula = Matricula.objects.all()

    informacion_template = {'matriculas': matricula, 'numero_matriculas': len(matricula)}
    return render(request, 'index.html', informacion_template)
