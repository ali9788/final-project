# Generated by Django 4.2.13 on 2024-06-21 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_service'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='namee',
            new_name='name',
        ),
    ]
