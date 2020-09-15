from django.shortcuts import render

# Create your views here.

def index(request, pagename):
    if pagename is '':
        return render(request, 'view.html')
    elif pagename is 'add':
        return render(request, 'add.html')
    elif pagename is 'view':
        return render(request, 'view.html')
