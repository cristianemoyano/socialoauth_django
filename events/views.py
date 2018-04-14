"""
INTEGRATE EVENTBRITE OAUTH LOGIN IN OUR DJANGO PROJECT
by Cristian Moyano

"""
from __future__ import unicode_literals

from django.shortcuts import render
from eventbrite import Eventbrite


def home(request):
    return render(request, 'events/home.html', {})


def all(request):
    access_token = request.user.social_auth.get(
        provider=request.session.get('social_auth_last_login_backend')
    ).access_token
    eventbrite = Eventbrite(access_token)
    events = [
        event
        # Status : live, draft, canceled, started, ended, all
        for event in eventbrite.get(
            '/users/me/events/?status=live,draft'
        )['events']
    ]
    return render(request, 'events/eventos.html', {'events': events})
