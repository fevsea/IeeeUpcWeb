from datetime import datetime, time

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from web.sendMail import send


# Create your views here.
def index(request):
    return render(request, 'web/base.html')

def contact(request):
    return render(request, 'web/contact.html')

def contactSend(request):
    ts = time()
    msg = datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    msg += request.POST['name'] + '\n' + request.POST['email'] +'\n'
    msg +=  '############################################################\n\n\n'
    msg += request.POST['msg']
    send(msg);
    return HttpResponseRedirect(reverse('web:index'))