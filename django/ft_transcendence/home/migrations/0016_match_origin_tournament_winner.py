# Generated by Django 4.2.9 on 2024-02-08 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_waitinglist'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='origin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.tournament'),
        ),
        migrations.AddField(
            model_name='tournament',
            name='winner',
            field=models.CharField(default='', max_length=100),
        ),
    ]
