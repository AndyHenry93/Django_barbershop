# Generated by Django 4.2 on 2023-04-13 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_remove_profile_is_barber_remove_profile_shop_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='client_photo',
            field=models.ImageField(null=True, upload_to='img/client/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='profile',
            name='shop_address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='shop_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
