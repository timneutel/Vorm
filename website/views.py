# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from models import Design

def base(request):
    designs = Design.objects.order_by('?')[:30]
    t = loader.get_template('home.html')
    c = RequestContext (request, {
            'designs': designs ,
        })
    return HttpResponse(t.render(c))