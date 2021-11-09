from django.shortcuts import render
import random

# Create your views here.

from .models import Event

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects

    items = list(Event.objects.all())

    # For the current demo, select three events at random
    events_set = random.sample(items, 3)

    print(events_set)

    events_set.sort(key=lambda x: x.secret_number)

    events = []
    for event in events_set:
        events.append(event.jsonify())

    context = {
        "events": events
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)