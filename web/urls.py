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
]