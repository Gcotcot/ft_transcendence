# Generated by Django 4.2.9 on 2024-02-08 17:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_match_origin_tournament_winner'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='amis',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
