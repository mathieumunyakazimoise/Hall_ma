# Generated by Django 5.1.1 on 2024-09-20 12:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_room_building'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='building',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_building', to='core.building'),
        ),
    ]