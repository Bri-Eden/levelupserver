from django.db import models
from django.contrib.auth.models import User


class Gamer(models.Model):
    # Relationship to the built-in User model which has name and email
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Additional bio field to capture from the client
    bio = models.CharField(max_length=155)

    events_attending = models.ManyToManyField("Event", through="EventGamer")
