# Generated by Django 4.1.7 on 2023-03-30 19:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LMS', '0010_alter_post_uploaded_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='uploaded_time',
            field=models.CharField(default=datetime.datetime(2023, 3, 30, 19, 43, 2, 457369, tzinfo=datetime.timezone.utc), max_length=100),
        ),
    ]