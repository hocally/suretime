from django.shortcuts import render

# Create your views here.

from .models import Event, Location

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_locations = Location.objects.all().count()
    num_events = Event.objects.all().count()

    events = [
        {
            "Name" : "Work",
            "Location" : "3M Corporate Center",
            "Departure_Time" : "7:41 AM",
            "Color" : "lightblue"
        },
        {
            "Name" : "School",
            "Location" : "University of Minnesota",
            "Departure_Time" : "4:35 PM",
            "Color" : "lightyellow"
        },
        {
            "Name" : "Flight DL892",
            "Location" : "MSP Airport",
            "Departure_Time" : "8:49 PM",
            "Color" : "lightgreen"
        }
    ]

    context = {
        "events": events
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)