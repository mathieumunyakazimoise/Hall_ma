# Generated by Django 5.1.1 on 2024-09-27 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('student', 'Student'), ('admin', 'Administrator')], default='student', max_length=20),
        ),
    ]