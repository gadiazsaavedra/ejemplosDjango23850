# Generated by Django 3.2.9 on 2021-12-06 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellido', models.CharField(max_length=40)),
                ('numero', models.IntegerField()),
                ('esBueno', models.BooleanField()),
            ],
        ),
    ]
