from django.shortcuts import render
from index.models import Perfil, Educacao, Habilidade, Case

def home(request):

    perfil = Perfil.objects.all()
    experiencia = Experiencia.objects.all()
    educacao = Educacao.objects.all()
    principal = Habilidade.objects.filter(prioridade="principal")
    secundaria = Habilidade.objects.filter(prioridade="secundaria")
    case = Case.objects.all()


    return render(request, 'index.html', {'perfil':perfil, 'experiencia':experiencia,'educacao':educacao, 'principal':principal, 'secundaria':secundaria, 'case':case})