# Generated by Django 4.0.3 on 2022-12-21 11:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_publicacao',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 21, 8, 16, 53, 350667)),
        ),
    ]
