# Generated by Django 3.1.7 on 2021-03-28 21:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210328_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]