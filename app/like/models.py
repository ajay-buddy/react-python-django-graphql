from django.db import models
from django_enumfield import enum
from django.contrib.auth import get_user_model
from games.models import Game
from books.models import Book
from tracks.models import Track

# Create your models here.
class LikeType(enum.Enum):
    UNDEFINED = 0
    GAME = 1
    BOOK = 2
    TRACK = 3

class Like(models.Model):
    book_like = models.ForeignKey(Book, related_name='book_like', blank=True, null=True, on_delete=models.CASCADE)
    game_like = models.ForeignKey(Game, related_name='game_like', blank=True, null=True, on_delete=models.CASCADE)
    track_like = models.ForeignKey(Track, related_name='track_like', blank=True, null=True, on_delete=models.CASCADE)
    like_type = enum.EnumField(LikeType, default=LikeType.UNDEFINED)
    created_at = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)
