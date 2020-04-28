# Generated by Django 2.2.10 on 2020-04-25 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yonghu', '0003_auto_20200405_0044'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('readAndReplyNumAndLikes', '0003_readandreplynum_main_floor_num'),
    ]

    operations = [
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('like_num', models.IntegerField(default=0, verbose_name='点赞数')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': '点赞数',
                'verbose_name_plural': '点赞数',
            },
        ),
        migrations.CreateModel(
            name='LikeDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_liked', models.BooleanField(default=False, verbose_name='是否点赞')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='点赞时间')),
                ('likes', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='readAndReplyNumAndLikes.Likes')),
                ('yonghu', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='yonghu.Yonghu', verbose_name='点赞者')),
            ],
            options={
                'verbose_name': '点赞细节',
                'verbose_name_plural': '点赞细节',
            },
        ),
    ]
