# Generated by Django 3.1 on 2020-08-30 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passenger', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trajet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depart', models.CharField(max_length=50)),
                ('arrivee', models.CharField(max_length=50)),
                ('prix', models.FloatField(max_length=10)),
            ],
        ),
    ]