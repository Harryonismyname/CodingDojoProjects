# Generated by Django 2.2 on 2020-09-24 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojos',
            name='desc',
            field=models.TextField(default='Old Dojo'),
        ),
    ]
