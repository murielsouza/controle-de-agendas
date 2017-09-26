# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-25 23:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
                ('tipo', models.CharField(choices=[('Publica', 'Pública'), ('Privada', 'Privada'), ('Institucional', 'Institucional')], max_length=14)),
                ('usuario', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Compromisso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
                ('dataHora', models.DateTimeField(blank=True, null=True)),
                ('local', models.CharField(max_length=60)),
                ('notas', models.TextField()),
                ('agenda', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='agenda.Agenda')),
            ],
        ),
        migrations.CreateModel(
            name='Convite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('situacao', models.BooleanField(default=0)),
                ('anfitriao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('compromisso', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='agenda.Compromisso')),
                ('convidados', models.ManyToManyField(blank=True, related_name='convidados', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
