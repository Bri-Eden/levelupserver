from django.db import models


class EventGamer(models.Model):
    gamer = models.ForeignKey(
        "Gamer", on_delete=models.CASCADE)
    event = models.ForeignKey("Event", null=True, blank=True,
        on_delete=models.CASCADE)

