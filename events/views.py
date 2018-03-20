# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import redirect
from social_django.models import UserSocialAuth
from django.http.response import HttpResponse
import requests
from .models import Evento,Asistente_Evento

def home(request):
    return render(request, 'events/home.html',{})

def all(request):
    events = Evento.objects.all()
    return render(request, 'events/eventos.html',{'eventos': events})

def go(request,pk):
        events = Evento.objects.filter(pk=pk)
        return render(request, 'events/evento.html',{'evento': events})
