# Generated by Django 2.0.5 on 2019-09-25 05:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cricketapp', '0003_auto_20190925_0508'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='date',
        ),
        migrations.AddField(
            model_name='match',
            name='match_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 25, 5, 16, 27, 787992)),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='MatchDate',
        ),
    ]
