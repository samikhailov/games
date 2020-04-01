from django.shortcuts import render
from .models import Deck

def homepage(request):
    decks = Deck.objects.all()
    return render(request, 'alias/base.html', {'decks': decks})
