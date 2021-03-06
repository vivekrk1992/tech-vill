# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-21 04:52
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
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='ExpenseType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('note', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PerDayTotalProductCost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='PickupTrip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('odo_start', models.IntegerField(blank=True, null=True)),
                ('odo_end', models.IntegerField(blank=True, null=True)),
                ('date', models.DateField()),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('logged_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logged_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TripProductCost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('pickup_trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maligai.PickupTrip')),
            ],
        ),
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
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10)),
                ('insurance_data', models.DateField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='maligai.UserType'),
        ),
        migrations.AddField(
            model_name='pickuptrip',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maligai.Vehicle'),
        ),
        migrations.AddField(
            model_name='expense',
            name='expense_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maligai.ExpenseType'),
        ),
        migrations.AddField(
            model_name='expense',
            name='pickup_trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maligai.PickupTrip'),
        ),
    ]
