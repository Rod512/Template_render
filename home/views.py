from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {'page':'Home'}
    return render(request, 'index.html', context)


def vote(request):
    peoples = [
        {'name': 'Rudro', 'age': 22, },
        {'name': 'Joya', 'age': 22, },
        {'name': 'Nobonita', 'age': 16, },
        {'name': 'Purnima', 'age': 21, },
        {'name': 'Dhruba', 'age': 15, },
        {'name': 'Suparna', 'age': 12, }
    ]

    text = 'Lorem, ipsum dolor sit amet consectetur adipisicing elit. Cum, vel.'

    
    context = {'page':'Vote'}

    return render(request, 'voting.html', context={'peoples' : peoples, 'text': text, 'page':'Vote'} )

def contact(request):
    context = {'page':'Contact'}
    return render(request, 'contact.html', context)