# Generated by Django 2.2 on 2019-04-16 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipmentmarketconnection',
            name='location',
        ),
        migrations.AddField(
            model_name='market',
            name='location',
            field=models.CharField(default='test', max_length=512),
            preserve_default=False,
        ),
    ]
