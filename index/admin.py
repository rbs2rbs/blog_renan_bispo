from django.contrib import admin
from index.models import Perfil, Experiencia,Educacao, Habilidade, Case

class PerfilAdmin(admin.ModelAdmin):
    fields = (
        'nome',
        'segundo_nome',
        'ultimo_nome',
        'sou_1', 
        'sou_2',
        'sou_3',
        'cidade',
        'email',
        'telefone',
        'curriculo', 
        'foto_perfil',
        'linkedin',
        'github',
        'instagram'
        )


class CaseAdmin(admin.ModelAdmin):
    fields = (
        'titulo',
        'resumo',
        'data_criado',
        'url',
        'imagem'
    )


admin.site.register(Perfil, PerfilAdmin)
admin.site.register(Experiencia)
admin.site.register(Educacao)
admin.site.register(Habilidade)
admin.site.register(Case,CaseAdmin)





