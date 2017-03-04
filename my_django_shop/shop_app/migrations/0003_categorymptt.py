# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-04 16:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0002_auto_20170304_0027'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryMPTT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='Наименование')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='shop_app.CategoryMPTT', verbose_name='Родительская категория')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]