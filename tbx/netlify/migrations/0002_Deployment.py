# Generated by Django 2.0.7 on 2018-08-05 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netlify', '0001_deployment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deployment',
            name='title',
            field=models.TextField(default='08/05/18 - 12:30', help_text='Deployment Title'),
        ),
    ]
