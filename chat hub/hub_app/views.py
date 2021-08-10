from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from .models import Card, Link
from django.urls import reverse
from .forms import CardForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

'''random garbage and so on'''

def home(request):
    cards = Card.objects.all()
    context = {
        'cards': cards,
    }
    return render(request, 'home.html', context)

def login_user(request):
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
    return HttpResponseRedirect(reverse('hub_app:travis'))

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('hub_app:travis'))


def travis(request):
    cards = Card.objects.all()
    
    context = {
        'cards': cards,
    }
    return render(request, 'travis.html', context)

def add_card(request):
    Card.objects.create(name=None,text="")
    cards = Card.objects.all()
    context = {
        'cards': cards,
    }
    return HttpResponseRedirect(reverse('hub_app:travis'))

def add_link(request, card_id):
    card_got = get_object_or_404(Card,pk=card_id)
    link_text = request.POST['link_text']
    Link.objects.create(text=link_text, card=card_got)
    cards = Card.objects.all()
    context = {
        'cards': cards,
    }
    return HttpResponseRedirect(reverse('hub_app:travis'))

def delete_card(request, card_id):
    card_got = get_object_or_404(Card, pk=card_id)
    card_got.delete()
    cards = Card.objects.all()
    context = {
        'cards': cards,
    }
    return HttpResponseRedirect(reverse('hub_app:travis'))

def delete_link(request, link_id):
    link_got = get_object_or_404(Link, pk=link_id)
    link_got.delete()
    cards = Card.objects.all()
    context = {
        'cards': cards,
    }
    return HttpResponseRedirect(reverse('hub_app:travis'))


def edit_card(request, card_id):
    card_got = get_object_or_404(Card,pk=card_id)
    card_got.text = request.POST.get('card_text')
    card_got.save()
    cards = Card.objects.all()
    context = {
        'cards': cards,
    }
    return HttpResponseRedirect(reverse('hub_app:travis'))