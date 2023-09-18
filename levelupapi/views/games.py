"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Game, Gamer, GameType


class GameView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type"""
        game = Game.objects.get(pk=pk)
        serializer = GameSerializer(game)

        """Returns:
            Response -- JSON serialized game type
        """
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
        Response -- JSON serialized game instance
        """
        gamer = Gamer.objects.get(user=request.auth.user)
        game_type = GameType.objects.get(pk=request.data["game_type"])

        game = Game.objects.create(
            name=request.data["name"],
            publisher=request.data["publisher"],
            num_of_players=request.data["num_of_players"],
            instructions=request.data["instructions"],
            gamer=gamer,
            game_type=game_type
        )
        serializer = GameSerializer(game)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a game

        Returns:
        Response -- Empty body with 204 status code
            """
        game_type = GameType.objects.get(pk=request.data["game_type"])

        game = Game.objects.get(pk=pk)
        game.name = request.data["name"]
        game.publisher = request.data["publisher"]
        game.num_of_players = request.data["num_of_players"]
        game.instructions = request.data["instructions"]
        game.game_type = game_type
        game.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)


class GameSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Game
        fields = ('id', 'game_type', 'name', 'gamer',
                  'instructions', 'num_of_players', 'publisher')
