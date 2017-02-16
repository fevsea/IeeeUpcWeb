from django.conf.urls import url

from . import views

app_name = 'web'

urlpatterns = [
    # ex: ~/
    url(r'^$', views.index, name='index'),
    # ex: ~/contact
    url(r'^contact$', views.contact, name='contact'),
    # ex: ~/contact/send
    url(r'^contact/send$', views.contactSend, name='contactSend'),
    # ex: ~/buran
    url(r'^buran$', views.buran, name='buran'),
    # ex: ~/buran
    url(r'^ieee$', views.ieee, name='ieee'),
    # ex: ~/visitas
    url(r'^visitas$', views.visitas, name='visitas'),
    # ex: ~/visitas/5/
    url(r'^visitas/(?P<visita_id>[0-9]+)/$', views.visita, name='visita'),
    # ex: ~/cursos
    url(r'^cursos$', views.cursos, name='cursos'),
    # ex: ~/cursos/5/
    url(r'^cursos/(?P<curso_id>[0-9]+)/$', views.curso, name='curso'),
    # ex: ~/proyectos
    url(r'^proyectos$', views.proyectos, name='proyectos'),
    # ex: ~/proyecto/5/
    url(r'^proyectos/(?P<proyecto_id>[0-9]+)/$', views.proyecto, name='proyecto'),
    # ex: ~/conferencias
    url(r'^otros$', views.otros, name='otros'),
    # ex: ~/otros/5/
    url(r'^otros/(?P<otro_id>[0-9]+)/$', views.otro, name='otro'),
]