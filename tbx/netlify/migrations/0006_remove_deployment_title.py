# Generated by Django 2.0.7 on 2018-08-06 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('netlify', '0005_auto_20180805_1427'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deployment',
            name='title',
        ),
    ]
