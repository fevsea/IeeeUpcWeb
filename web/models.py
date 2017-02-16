from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Visita(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    date_start = models.DateTimeField('Fecha de realización')
    summary = models.TextField()
    description = models.TextField()
    id = models.AutoField(primary_key=True)
    img = models.ImageField(null=True, upload_to = 'img/actividad')
    author = models.ForeignKey(User, null=True, blank=False)

    def __str__(self):
        return self.title

class Proyecto(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    date_start = models.DateTimeField('Fecha última modificación', auto_now=True)
    date_finish = models.DateTimeField('Fecha de finalización', null=True);
    summary = models.TextField()
    description = models.TextField()
    id = models.AutoField(primary_key=True)
    img = models.ImageField(null=True, upload_to='img/actividad')
    author = models.ForeignKey(User, null=True, blank=False)

    def __str__(self):
        return self.title

class Curso(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    date_start = models.DateTimeField('Fecha de inicio')
    date_finish = models.DateTimeField('Fecha de finalización')
    summary = models.TextField()
    description = models.TextField()
    id = models.AutoField(primary_key=True)
    img = models.ImageField(null=True, upload_to = 'img/actividad')
    author = models.ForeignKey(User, null=True, blank=False)

    def __str__(self):
        return self.title

class Otro(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    date_start = models.DateTimeField('Fecha de inicio')
    date_finish = models.DateTimeField('Fecha de finalización')
    summary = models.TextField()
    description = models.TextField()
    id = models.AutoField(primary_key=True)
    img = models.ImageField(null=True, upload_to = 'img/actividad')
    author = models.ForeignKey(User, null=True, blank=False)

    def __str__(self):
        return self.title

