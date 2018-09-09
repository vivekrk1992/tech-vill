# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-01 14:34
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
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('street', models.TextField(blank=True, null=True)),
                ('village', models.CharField(blank=True, max_length=100, null=True)),
                ('taluk', models.CharField(blank=True, max_length=100, null=True)),
                ('district', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('pincode', models.IntegerField(blank=True, null=True)),
                ('latitude', models.CharField(blank=True, max_length=40, null=True)),
                ('longitude', models.CharField(blank=True, max_length=40, null=True)),
                ('mobile', models.BigIntegerField(blank=True, null=True)),
                ('alternate_mobile', models.BigIntegerField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='main_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('notes', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.UserType'),
        ),
    ]