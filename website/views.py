from django.shortcuts import render

from membership.models import Committee

def home(request):
    return render(request, 'website/home.html')

def about(request):
    committees = Committee.objects.all()
    context = {'committees': committees}
    return render(request, 'website/about.html', context)

def contact(request):
    return render(request, 'website/contact.html')

def downunder(request):
    return render(request, 'website/downunder.html')

def join(request):
    return render(request, 'website/join.html')
