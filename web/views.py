import time
import datetime

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from web.models import Visita, Curso
from web.sendMail import send

months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

# Create your views here.
def index(request):
    return render(request, 'web/base.html')

def contact(request):
    return render(request, 'web/contact.html')

def visitas(request):
    latest_visits_list = Visita.objects.order_by('date')[:5]
    for v in latest_visits_list:
        v.month = months[v.date.month-1]
    context = {'visitas_list': latest_visits_list, 'username': request.user.username}
    return render(request, 'web/visitas.html', context)

def visita(request, visita_id):
    visita = get_object_or_404(Visita, pk=visita_id)
    visita.month = months[visita.date.month - 1]
    return render(request, 'web/visita.html', {'visita': visita, 'username': request.user.username})

def cursos(request):
    latest_courses_list = Curso.objects.order_by('date_start')[:5]
    for c in latest_courses_list:
        c.month = months[c.date_start.month-1]
    context = {'cursos_list': latest_courses_list, 'username': request.user.username}
    return render(request, 'web/cursos.html', context)

def curso(request, curso_id):
    curso = get_object_or_404(Curso, pk=curso_id)
    curso.month = months[curso.date.month - 1]
    return render(request, 'web/curso.html', {'curso': curso, 'username': request.user.username})

def buran(request):
    return render(request, 'web/buran.html')

def contactSend(request):
    ts = time.time()
    msg = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S') + '\n'
    msg += request.POST['name'] + '\n' + request.POST['email'] +'\n'
    msg +=  '################################################\n\n\n'
    msg += request.POST['msg']
    send(msg);
    return HttpResponseRedirect(reverse('web:index'))