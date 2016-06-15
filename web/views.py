from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'web/base.html')

def contact(request):
    return render(request, 'web/contact.html')