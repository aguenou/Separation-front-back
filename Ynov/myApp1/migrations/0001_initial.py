# Generated by Django 4.1.5 on 2023-01-20 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artiste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('style', models.CharField(choices=[('POP', 'POP'), ('RAP', 'RAP'), ('CLASSIC', 'CLASSIC'), ('ROCK', 'ROCK'), ('UNDEFINED', 'UNDEFINED')], default='RAP', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Chanson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=30)),
                ('duree', models.TimeField()),
                ('date', models.DateField()),
                ('artiste', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp1.artiste')),
            ],
        ),
    ]
