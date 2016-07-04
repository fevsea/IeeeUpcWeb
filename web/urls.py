from django.conf.urls import url

from . import views

app_name = 'web'

urlpatterns = [
    # ex: /web/
    url(r'^$', views.index, name='index'),
    # ex: /web/contact
    url(r'^contact$', views.contact, name='contact'),
    # ex: /web/contact/send
    url(r'^contact/send$', views.contactSend, name='contactSend'),
    # ex: /web/buran
    url(r'^contact/buran$', views.buran, name='buran'),
    # ex: /web/visitas
    url(r'^visitas$', views.visitas, name='visitas'),
    # ex: /web/visitas/5/
    url(r'^visitas/(?P<visita_id>[0-9]+)/$', views.visita, name='visita'),
    # ex: /web/cursos
    url(r'^cursos$', views.cursos, name='cursos'),
    # ex: /web/cursos/5/
    url(r'^cursos/(?P<curso_id>[0-9]+)/$', views.curso, name='curso'),

]