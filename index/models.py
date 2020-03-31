from django.db import models
from django.conf import settings
from django.utils import timezone


class Perfil(models.Model):
    nome = models.CharField(max_length=200)
    segundo_nome = models.CharField(max_length=200)
    ultimo_nome = models.CharField(max_length=200)
    sou_1 = models.CharField(max_length=200)
    sou_2 = models.CharField(max_length=200)
    sou_3 = models.CharField(max_length=200)
    sobre_mim = models.TextField()
    cidade = models.CharField(max_length=200)
    email = models.EmailField()
    telefone = models.CharField(max_length=13)
    curriculo = models.FileField(null=True, blank=True)
    curriculo_base = models.TextField(max_length=999999,null=True, blank=True)
    foto_perfil = models.ImageField()
    foto_perfil_base = models.TextField(max_length=999999,null=True, blank=True)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
            import base64

            self.foto_perfil_base = "%s"%base64.b64encode(self.foto_perfil.read())
            self.foto_perfil_base = self.foto_perfil_base.replace("b'","").replace("'","")

            self.curriculo_base = "%s"%base64.b64encode(self.curriculo.read())
            self.curriculo_base = self.curriculo_base.replace("b'","").replace("'","")

            super(Perfil, self).save(*args, **kwargs)


class Experiencia(models.Model):
    preiodo = models.CharField(max_length=200)
    local = models.CharField(max_length=200)
    titulo = models.TextField()
    descricao = models.TextField()

    def __str__(self):
        return self.titulo


class Educacao(models.Model):
    periodo = models.CharField(max_length=200)
    local = models.CharField(max_length=200)
    titulo = models.TextField()
    descricao = models.TextField()

    def __str__(self):
        return self.titulo

# classe para range de inteiros
class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)

class Habilidade(models.Model):
    habilidade = models.CharField(max_length=200)
    nivel_habilidade = IntegerRangeField(min_value=0, max_value=100)
    nivel_teorico = IntegerRangeField(min_value=0, max_value=100)
    nivel_pratico = IntegerRangeField(min_value=0, max_value=100)
    prioridade = models.CharField(choices = [("principal","principal"),("secundaria","secundaria"),],max_length=200)

    def __str__(self):
        return self.habilidade


class Case(models.Model):
    titulo = models.CharField(max_length=200)
    resumo = models.TextField()
    data_criado = models.DateField()
    url = models.URLField()
    imagem = models.ImageField(null=True, blank=True)
    fimagem_base = models.TextField(max_length=999999,null=True, blank=True)

    def save(self, *args, **kwargs):
        import base64

        self.fimagem_base = "%s"%base64.b64encode(self.imagem.read())
        self.fimagem_base = self.fimagem_base.replace("b'","").replace("'","")

        super(Case, self).save(*args, **kwargs)
