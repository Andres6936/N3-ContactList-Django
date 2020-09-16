from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

def index(request, pagename):
    return render(request, pagename + '.html')


def add(request):
    submitted = False
    if request.method == 'POST':
        return HttpResponseRedirect('/add?submitted=True')
    else:
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add.html', {'submitted': submitted})
