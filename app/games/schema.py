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
        user = info.context.user or None
        game = Game(title = kwargs.get('title'), description = kwargs.get('description'), url = kwargs.get('url'), posted_by = user)
        game.save()
        return CreateGame(game=game)

class UpdateGame(graphene.Mutation):
    game = graphene.Field(GameType)

    class Arguments:
        game_id = graphene.Int(required=True)
        title = graphene.String()
        description = graphene.String()
        url = graphene.String()
    
    def mutate(self, info, **kwargs):
        user = info.context.user or None
        game = Game.objects.get(id=kwargs.get('game_id'))

        if game.posted_by != user:
            raise Exception('Not Permitted!!')
        game.title = kwargs.get('title')
        game.description = kwargs.get('description')
        game.url = kwargs.get('url')
        game.save()
        return UpdateGame(game=game)

class DeleteGame(graphene.Mutation):
    game = graphene.Field(GameType)

    class Arguments:
        game_id = graphene.Int(required=True)
    
    def mutate(self, info, **kwargs):
        user = info.context.user or None
        game = Game.objects.get(id=kwargs.get('game_id'))

        if game.posted_by != user:
            raise Exception('Not Permitted!!')
        game.delete()
        return DeleteGame(game=game)

class Mutation(graphene.ObjectType):
    create_game = CreateGame.Field()
    update_game = UpdateGame.Field()
    delete_game = DeleteGame.Field()