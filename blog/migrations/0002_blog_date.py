# Generated by Django 3.1.7 on 2021-03-28 21:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]