import graphene
from graphene_django import DjangoObjectType

from .models import Game

class GameType(DjangoObjectType):
    class Meta:
        model = Game

class Query(graphene.ObjectType):
    games = graphene.List(GameType)

    def resolve_games(self, info):
        return Game.objects.all()

class CreateGame(graphene.Mutation):
    game = graphene.Field(GameType)

    class Arguments:
        title = graphene.String()
        description = graphene.String()
        url = graphene.String()

    def mutate(self, info, **kwargs):
        game = Game(title = kwargs.get('title'), description = kwargs.get('description'), url = kwargs.get('url'))
        game.save()
        return CreateGame(game=game)

class Mutation(graphene.ObjectType):
    create_game = CreateGame.Field()