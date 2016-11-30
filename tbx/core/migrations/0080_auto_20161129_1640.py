# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-11-29 16:17
from __future__ import unicode_literals

import json

from django.db import migrations


def migrate_streamfield_json(json):
    for block in json:
        if block['type'] == 'case_studies':
            block['value']['case_studies'] = [
                {
                    'page': page_id,
                    'title': '',
                    'descriptive_title': '',
                    'image': None,
                }
                for page_id in block['value']['case_studies']
            ]

    return json


def migrate_service_pages(apps, schema_editor):
    ServicePage = apps.get_model('torchbox.ServicePage')

    for service_page in ServicePage.objects.all():
        service_page.streamfield.stream_data = migrate_streamfield_json(service_page.streamfield.stream_data)
        service_page.save(update_fields=['streamfield'])

        for revision in service_page.revisions.all():
            content_json = json.loads(revision.content_json)
            content_json['streamfield'] = json.dumps(migrate_streamfield_json(json.loads(content_json['streamfield'])))
            revision.content_json = json.dumps(content_json)

            revision.save(update_fields=['content_json'])


class Migration(migrations.Migration):

    dependencies = [
        ('torchbox', '0079_auto_20161129_1640'),
    ]

    operations = [
        migrations.RunPython(migrate_service_pages),
    ]