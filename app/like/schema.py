import graphene
from graphene_django import DjangoObjectType

from .models import Like, LikeType


class LikeDataType(DjangoObjectType):
    class Meta:
        model = Like

class Query(graphene.ObjectType):
    likes = graphene.List(LikeDataType)

    def resolve_likes(self, info):
        return Like.objects.all()

class CreateLike(graphene.Mutation):
    like = graphene.Field(LikeDataType)

    class Arguments:
        book_like = graphene.Int()
        game_like = graphene.Int()
        track_like = graphene.Int()
        # like_type = graphene.Field(GrapheneEnum)

    def mutate(self, info, **kwargs):
        user = info.context.user or None
        like = Like(book_like = kwargs.get('book_like'), game_like = kwargs.get('game_like'), track_like = kwargs.get('track_like'), posted_by = user)
        like.save()
        return CreateLike(like=like)

class UpdateLike(graphene.Mutation):
    like = graphene.Field(LikeDataType)

    class Arguments:
        like_id = graphene.Int(required=True)
        book_like = graphene.Int()
        game_like = graphene.Int()
        track_like = graphene.Int()
        # like_type = graphene.Field(GrapheneEnum)
    
    def mutate(self, info, **kwargs):
        user = info.context.user or None
        like = Like.objects.get(id=kwargs.get('like_id'))

        if like.posted_by != user:
            raise Exception('Not Permitted!!')
        like.book_like = kwargs.get('book_like')
        like.track_like = kwargs.get('track_like')
        like.game_like = kwargs.get('game_like')
        # like.like_type = kwargs.get('like_type')
        like.save()
        return UpdateLike(like=like)

class DeleteLike(graphene.Mutation):
    like = graphene.Field(LikeDataType)

    class Arguments:
        like_id = graphene.Int(required=True)
    
    def mutate(self, info, **kwargs):
        user = info.context.user or None
        like = Like.objects.get(id=kwargs.get('like_id'))

        if game.posted_by != user:
            raise Exception('Not Permitted!!')
        like.delete()
        return DeleteLike(like=like)

class Mutation(graphene.ObjectType):
    create_like = CreateLike.Field()
    update_like = UpdateLike.Field()
    delete_like = DeleteLike.Field()