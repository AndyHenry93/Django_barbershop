# Generated by Django 4.2 on 2023-04-13 00:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_profile_is_barber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_barber',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='shop_address',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='shop_name',
        ),
    ]
