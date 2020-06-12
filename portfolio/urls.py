from django.urls import path
from . import views

urlpatterns = [
    path('', views.portafolio, name='portafolio'),
    path('projecto/<id>', views.projecto, name='projecto'),
]
