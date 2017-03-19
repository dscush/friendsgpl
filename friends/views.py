from django.shortcuts import render

def home(request):
    return render(request, 'friends/home.html')

def about(request):
    return render(request, 'friends/about.html')

def contact(request):
    return render(request, 'friends/contact.html')

def downunder(request):
    return render(request, 'friends/downunder.html')

def join(request):
    return render(request, 'friends/join.html')
