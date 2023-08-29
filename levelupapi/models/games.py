from django.db import models


class Game(models.Model):
    game_type = models.ForeignKey(
        "GameType", on_delete=models.CASCADE, related_name='games')
    gamer = models.ForeignKey("Gamer", null=True, blank=True,
        on_delete=models.CASCADE, related_name='games')
    name = models.CharField(max_length=155)
    instructions = models.CharField(max_length=250)
    num_of_players = models.IntegerField(max_length=20)
    publisher = models.CharField(max_length= 30)
