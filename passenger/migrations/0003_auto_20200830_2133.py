# Generated by Django 3.1 on 2020-08-30 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passenger', '0002_trajet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trajet',
            name='prix',
            field=models.CharField(max_length=10),
        ),
    ]
