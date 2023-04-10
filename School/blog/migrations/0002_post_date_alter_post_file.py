# Generated by Django 4.1.7 on 2023-03-30 18:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 3, 30, 18, 38, 23, 314565, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='file',
            field=models.FileField(default=None, null=True, upload_to='static/assets/blog/file'),
        ),
    ]