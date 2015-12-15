# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('comment_name', models.TextField()),
                ('comment_date', models.DateField(auto_now_add=True)),
                ('comment_content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('page_title', models.TextField()),
                ('page_date', models.DateField(auto_now_add=True)),
                ('page_content', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_page',
            field=models.ForeignKey(to='blog.Page'),
        ),
    ]
