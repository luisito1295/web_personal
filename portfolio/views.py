from django.shortcuts import render
from .models import Project

# Create your views here.
def portafolio(request):
    projects = Project.objects.all()
    return render(request, "portafolio.html", {'projects':projects})

def projecto(request, id):
    project = Project.objects.get(id=id)
    return render(request, 'projecto.html', {'project':project})

    