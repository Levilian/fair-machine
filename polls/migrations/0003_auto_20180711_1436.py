# Generated by Django 2.0.1 on 2018-07-11 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20180710_0417'),
    ]

    operations = [
        migrations.AddField(
            model_name='decisiongroup',
            name='slug',
            field=models.SlugField(default='None', unique=True),
        ),
        migrations.AlterField(
            model_name='decisiongroup',
            name='scenario_title',
            field=models.CharField(db_index=True, max_length=400),
        ),
    ]
