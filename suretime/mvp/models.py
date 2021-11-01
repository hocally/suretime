from django.db import models

# Create your models here.

from django.urls import reverse # Used to generate URLs by reversing the URL patterns

class Location(models.Model):
    """Model representing an author."""
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, help_text='Enter a brief description of the event')

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('location-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.name}'

class Event(models.Model):
    """Model representing an event."""
    title = models.CharField(max_length=200)
    location = models.ForeignKey('Location', on_delete=models.RESTRICT, null=True)
    start = models.DateField(null=True, blank=True)
    end = models.DateField(null=True, blank=True)

    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the event')
    
    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('event-detail', args=[str(self.id)])
