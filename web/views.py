import time
import datetime

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from web.models import Visita, Curso, Proyecto, Conferencia
from web.sendMail import send

months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

# Create your views here.
def index(request):
    return render(request, 'web/index.html')

def buran(request):
    return render(request, 'web/buran.html')

def contact(request):
    return render(request, 'web/contact.html')

def contactSend(request):
    ts = time.time()
    msg = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S') + '\n'
    msg += request.POST['name'] + '\n' + request.POST['email'] +'\n'
    msg +=  '################################################\n\n\n'
    msg += request.POST['msg']
    send(msg)
    return HttpResponseRedirect(reverse('web:index'))

def ieee(request):
    return render(request, 'web/ieee.html')

def visitas(request):
    latest_visits_list = Visita.objects.order_by('-date_start')#[:5]
    for v in latest_visits_list:
        v.month = months[v.date_start.month-1]
    context = {'visitas_list': latest_visits_list, 'username': request.user.username}
    return render(request, 'web/visitas.html', context)

def visita(request, visita_id):
    visita = get_object_or_404(Visita, pk=visita_id)
    visita.month = months[visita.date_start.month - 1]
    return render(request, 'web/visita.html', {'visita': visita, 'username': request.user.username})

def cursos(request):
    latest_courses_list = Curso.objects.order_by('-date_start')#[:5]
    for c in latest_courses_list:
        c.month = months[c.date_start.month-1]
    context = {'cursos_list': latest_courses_list, 'username': request.user.username}
    return render(request, 'web/cursos.html', context)

def curso(request, curso_id):
    curso = get_object_or_404(Curso, pk=curso_id)
    curso.month = months[curso.date_start.month - 1]
    return render(request, 'web/curso.html', {'curso': curso, 'username': request.user.username})

def proyectos(request):
    latest_proyectos_list = Proyecto.objects.order_by('-date_start')#[:5]
    for p in latest_proyectos_list:
        p.month = months[p.date_start.month-1]
    context = {'proyectos_list': latest_proyectos_list, 'username': request.user.username}
    return render(request, 'web/proyectos.html', context)

def proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, pk=proyecto_id)
    proyecto.month = months[proyecto.date_start.month - 1]
    return render(request, 'web/proyecto.html', {'proyecto': proyecto, 'username': request.user.username})

def conferencias(request):
    latest_conferencias_list = Conferencia.objects.order_by('-date_start')#[:5]
    for c in latest_conferencias_list:
        c.month = months[c.date_start.month-1]
    context = {'conferencias_list': latest_conferencias_list, 'username': request.user.username}
    return render(request, 'web/conferencias.html', context)

def conferencia(request, conferencia_id):
    conferencia = get_object_or_404(Conferencia, pk=conferencia_id)
    conferencia.month = months[conferencia.date_start.month - 1]
    return render(request, 'web/conferencia.html', {'conferencia': conferencia, 'username': request.user.username})

def python(request):
    latest_courses_list = Curso.objects.order_by('-date_start')#[:5]
    for c in latest_courses_list:
        c.month = months[c.date_start.month-1]
    context = {'cursos_list': latest_courses_list, 'username': request.user.username}
    return render(request, 'web/cursos.html', context)

