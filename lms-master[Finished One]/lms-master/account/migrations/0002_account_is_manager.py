# Generated by Django 2.2.4 on 2019-10-18 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_manager',
            field=models.BooleanField(default=False),
        ),
    ]