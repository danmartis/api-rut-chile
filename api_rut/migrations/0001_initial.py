# Generated by Django 2.0.7 on 2018-07-27 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=9)),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=20)),
                ('region', models.CharField(max_length=20)),
                ('comuna', models.CharField(max_length=20)),
                ('provincia', models.CharField(max_length=20)),
                ('circunscripcion', models.CharField(max_length=50)),
                ('mesa', models.CharField(max_length=50)),
                ('domicilio_electoral', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sexo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='persona',
            name='sexo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_rut.Sexo'),
        ),
    ]