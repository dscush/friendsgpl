from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse

def home(request):
    return render(request, 'friends/home.html', context_instance=RequestContext(request))

def about(request):
    return render(request, 'friends/about.html', context_instance=RequestContext(request))

def contact(request):
    return render(request, 'friends/contact.html', context_instance=RequestContext(request))

def downunder(request):
    return render(request, 'friends/downunder.html', context_instance=RequestContext(request))

def join(request):
    return render(request, 'friends/join.html', context_instance=RequestContext(request))
