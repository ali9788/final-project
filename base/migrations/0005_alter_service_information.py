# Generated by Django 4.2.13 on 2024-06-21 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_rename_namee_service_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='information',
            field=models.CharField(max_length=150),
        ),
    ]
