import time
import datetime

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from web.sendMail import send


# Create your views here.
def index(request):
    return render(request, 'web/base.html')

def contact(request):
    return render(request, 'web/contact.html')

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