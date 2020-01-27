# Generated by Django 3.0.2 on 2020-01-27 10:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date Joined'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account',
            name='last_login',
            field=models.DateTimeField(auto_now=True, default=django.utils.timezone.now, verbose_name='Last Active'),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='account',
            table='Account',
        ),
    ]
