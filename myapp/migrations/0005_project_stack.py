# Generated by Django 4.2.1 on 2024-01-31 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_tech'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='stack',
            field=models.ManyToManyField(blank=True, related_name='techused', to='myapp.tech'),
        ),
    ]