from django.db import models

# Create your models here.

from django.urls import reverse # Used to generate URLs by reversing the URL patterns

class Event(models.Model):
    """Model representing an event."""
    name = models.CharField(max_length=200)
    departure_time = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    secret_number = models.CharField(max_length=200)
    
    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def jsonify(self):
        return {
            "Name" : str(self.name),
            "Location" : str(self.location),
            "Departure_Time" : str(self.departure_time),
            "Color" : str(self.color)
        }

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('event-detail', args=[str(self.id)])
