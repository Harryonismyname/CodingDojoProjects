# Generated by Django 2.2 on 2020-09-29 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semi_restful_tv_shows', '0002_show_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='release_date',
            field=models.DateField(),
        ),
    ]
