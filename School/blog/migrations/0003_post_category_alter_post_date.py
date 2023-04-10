# Generated by Django 4.1.7 on 2023-03-30 19:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_date_alter_post_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='سلام', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 3, 30, 19, 29, 13, 339702, tzinfo=datetime.timezone.utc)),
        ),
    ]