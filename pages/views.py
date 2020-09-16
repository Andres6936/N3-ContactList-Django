from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

def index(request, pagename):
    return render(request, pagename + '.html')


def add(request):
    if request.method == 'POST':
        return HttpResponseRedirect('/add?submitted=True')
    elif request.method == 'GET':
        pass
    return render(request, 'add.html')
