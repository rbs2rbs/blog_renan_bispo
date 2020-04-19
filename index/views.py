from django.shortcuts import render
from index.models import Perfil, Educacao, Habilidade, Case,Experiencia

def home(request):

    perfil = Perfil.objects.all()
    experiencia = Experiencia.objects.all()
    educacao = Educacao.objects.all()
    principal = Habilidade.objects.filter(prioridade="principal")
    secundaria = Habilidade.objects.filter(prioridade="secundaria")
    case = Case.objects.order_by("-data_criado")


    return render(request, 'index.html', {'perfil':perfil, 'experiencia':experiencia,'educacao':educacao, 'principal':principal, 'secundaria':secundaria, 'case':case})