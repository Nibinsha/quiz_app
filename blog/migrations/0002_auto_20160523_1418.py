# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-23 14:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.URLField(blank=True)),
                ('picture', models.ImageField(blank=True, upload_to='profile_images')),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=250)),
                ('option1', models.CharField(max_length=128)),
                ('option2', models.CharField(max_length=128)),
                ('option3', models.CharField(max_length=128)),
                ('option4', models.CharField(max_length=128)),
                ('correct_ans', models.CharField(max_length=128)),
            ],
        ),
        migrations.RemoveField(
            model_name='question',
            name='questionnaire',
        ),
        migrations.RemoveField(
            model_name='questionanswer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='useranswer',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='useranswer',
            name='user_questionnaire',
        ),
        migrations.RemoveField(
            model_name='userquestionnaire',
            name='questionnaire',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='QuestionAnswer',
        ),
        migrations.DeleteModel(
            name='Questionnaire',
        ),
        migrations.DeleteModel(
            name='UserAnswer',
        ),
        migrations.DeleteModel(
            name='UserQuestionnaire',
        ),
        migrations.AddField(
            model_name='person',
            name='play',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Questions'),
        ),
        migrations.AddField(
            model_name='person',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
