# Generated by Django 4.2.9 on 2024-01-29 16:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_tournament_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='number_registered',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='max_player',
            field=models.IntegerField(choices=[(4, '4'), (8, '8'), (16, '16'), (32, '32')], default=4),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='players_registered',
        ),
        migrations.AlterField(
            model_name='tournament',
            name='time_to_subscribe',
            field=models.IntegerField(choices=[(5, '5m'), (10, '10m'), (15, '15m'), (20, '20m'), (25, '25m'), (30, '30m')], default=15),
        ),
        migrations.AddField(
            model_name='tournament',
            name='players_registered',
            field=models.ManyToManyField(blank=True, related_name='tournaments_registered', to=settings.AUTH_USER_MODEL),
        ),
    ]
