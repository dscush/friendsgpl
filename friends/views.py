from django.shortcuts import render

from membership.models import Committee

def home(request):
    return render(request, 'friends/home.html')

def about(request):
    committees = Committee.objects.all()
    context = {'committees': committees}
    return render(request, 'friends/about.html', context)

def contact(request):
    return render(request, 'friends/contact.html')

def downunder(request):
    return render(request, 'friends/downunder.html')

def join(request):
    return render(request, 'friends/join.html')
