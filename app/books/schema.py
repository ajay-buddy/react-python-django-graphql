import graphene
from graphene_django import DjangoObjectType

from .models import Book

class BookType(DjangoObjectType):
    class Meta:
        model = Book

class Query(graphene.ObjectType):
    books = graphene.List(BookType)

    def resolve_books(self, info):
        return Book.objects.all()

class CreateBook(graphene.Mutation):
    book = graphene.Field(BookType)

    class Arguments:
        title = graphene.String()
        description = graphene.String()
        url = graphene.String()

    def mutate(self, info, **kwargs):
        user = info.context.user or None
        book = Book(title = kwargs.get('title'), description = kwargs.get('description'), url = kwargs.get('url'), posted_by = user)
        book.save()
        return CreateBook(book=book)

class UpdateBook(graphene.Mutation):
    Book = graphene.Field(BookType)

    class Arguments:
        book_id = graphene.Int(required=True)
        title = graphene.String()
        description = graphene.String()
        url = graphene.String()
    
    def mutate(self, info, **kwargs):
        user = info.context.user or None
        book = Book.objects.get(id=kwargs.get('book_id'))

        if book.posted_by != user:
            raise Exception('Not Permitted!!')
        book.title = kwargs.get('title')
        book.description = kwargs.get('description')
        book.url = kwargs.get('url')
        book.save()
        return UpdateBook(book=book)

class DeleteBook(graphene.Mutation):
    Book = graphene.Field(BookType)

    class Arguments:
        book_id = graphene.Int(required=True)
    
    def mutate(self, info, **kwargs):
        user = info.context.user or None
        book = Book.objects.get(id=kwargs.get('book_id'))

        if book.posted_by != user:
            raise Exception('Not Permitted!!')
        book.delete()
        return DeleteBook(book=book)

class Mutation(graphene.ObjectType):
    create_book = CreateBook.Field()
    update_book = UpdateBook.Field()
    delete_book = DeleteBook.Field()