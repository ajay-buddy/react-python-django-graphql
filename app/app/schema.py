import graphene
import graphql_jwt
import tracks.schema
import users.schema
import books.schema
import games.schema
import like.schema

class Query(users.schema.Query, books.schema.Query, games.schema.Query, tracks.schema.Query, like.schema.Query, graphene.ObjectType):
    pass

class Mutation(users.schema.Mutation, books.schema.Mutation, games.schema.Mutation, tracks.schema.Mutation, like.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)