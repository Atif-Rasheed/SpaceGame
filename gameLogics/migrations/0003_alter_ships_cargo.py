# Generated by Django 4.2.7 on 2023-11-12 14:37

from django.db import migrations
import gameLogics.models


class Migration(migrations.Migration):

    dependencies = [
        ('gameLogics', '0002_remove_ships_mid_alter_ships_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ships',
            name='cargo',
            field=gameLogics.models.MoneyField(decimal_places=2, max_digits=100),
        ),
    ]