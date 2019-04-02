# Generated by Django 2.1.5 on 2019-04-02 09:34

from django.db import migrations, models
import django.db.models.deletion
import headlesspreview.models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('people', '0014_contactreasonslist_is_default_not_unique'),
        ('torchbox', '0125_auto_20190216_1713'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotFoundPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('strapline', models.CharField(max_length=255)),
                ('background_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='torchbox.TorchboxImage')),
                ('contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='people.Contact')),
                ('contact_reasons', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='people.ContactReasonsList')),
            ],
            options={
                'abstract': False,
            },
            bases=(headlesspreview.models.HeadlessPreviewMixin, 'wagtailcore.page'),
        ),
    ]
