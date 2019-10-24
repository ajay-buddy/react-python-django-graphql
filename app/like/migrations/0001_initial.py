# Generated by Django 2.2.6 on 2019-10-24 21:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0002_book_posted_by'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('games', '0002_game_posted_by'),
        ('tracks', '0002_track_posted_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('book_like', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='book_like', to='books.Book')),
                ('game_like', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='game_like', to='games.Game')),
                ('posted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('track_like', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='track_like', to='tracks.Track')),
            ],
        ),
    ]