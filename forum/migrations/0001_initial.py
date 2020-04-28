# Generated by Django 2.2.10 on 2020-04-25 17:06

from django.db import migrations, models
import django.db.models.deletion
import images.getImagePath
import readAndReplyNumAndLikes.getReadAndReplyNumLikes


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('yonghu', '0003_auto_20200405_0044'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=15, verbose_name='类型')),
            ],
            options={
                'verbose_name': '帖子类型',
                'verbose_name_plural': '帖子类型',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='帖子标题')),
                ('content', models.TextField(verbose_name='帖子内容')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='forum.PostType')),
                ('yonghu', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='yonghu.Yonghu', verbose_name='发帖人')),
            ],
            options={
                'verbose_name': '发表帖子',
                'verbose_name_plural': '发表帖子',
                'ordering': ['-created_time'],
            },
            bases=(models.Model, readAndReplyNumAndLikes.getReadAndReplyNumLikes.GetReadAndReplyAndLikesNum, images.getImagePath.GetImagePath),
        ),
    ]
