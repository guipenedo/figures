# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-11-15 17:34
# Manually updated to support Django 1.8 as well as 1.11

from __future__ import unicode_literals

from __future__ import absolute_import
from django import VERSION as DJANGO_VERSION
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import figures.models
import model_utils.fields


class Migration(migrations.Migration):
    if DJANGO_VERSION[0:2] == (1,8):
        dependencies = [
            ('sites', '0001_initial'),
            ('figures', '0008_cdm_meta_update'),
        ]
    else:  # Assuming 1.11+
        dependencies = [
            ('sites', '0002_alter_domain_unique'),
            ('figures', '0008_cdm_meta_update'),
        ]

    operations = [
        migrations.CreateModel(
            name='CourseMauMetrics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('date_for', models.DateField()),
                ('course_id', models.CharField(max_length=255)),
                ('mau', models.IntegerField()),
                ('site', models.ForeignKey(default=figures.models.default_site, on_delete=django.db.models.deletion.CASCADE, to='sites.Site')),
            ],
        ),
        migrations.CreateModel(
            name='SiteMauMetrics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('date_for', models.DateField()),
                ('mau', models.IntegerField()),
                ('site', models.ForeignKey(default=figures.models.default_site, on_delete=django.db.models.deletion.CASCADE, to='sites.Site')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='sitemaumetrics',
            unique_together=set([('site', 'date_for')]),
        ),
        migrations.AlterUniqueTogether(
            name='coursemaumetrics',
            unique_together=set([('site', 'course_id', 'date_for')]),
        ),
    ]
