# Generated by Django 2.2.10 on 2020-03-17 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0005_auto_20200317_1842'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commody',
            name='floorNum',
        ),
        migrations.RemoveField(
            model_name='commody',
            name='read_num',
        ),
        migrations.RemoveField(
            model_name='commody',
            name='replyNum',
        ),
        migrations.DeleteModel(
            name='ImagePath',
        ),
    ]
