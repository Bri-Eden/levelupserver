from django.db import models


class Event(models.Model):
    game = models.ForeignKey(
        "Game", null=True, blank=True, on_delete=models.CASCADE, related_name='event')
    organizer = models.ForeignKey("Gamer", null=True, blank=True,
                                  on_delete=models.CASCADE, related_name='events')
    attendees = models.ManyToManyField("Gamer", through="EventGamer")
    address = models.CharField(max_length=155)
    date = models.DateTimeField(
        null=True, blank=True, auto_now=False, auto_now_add=False)
