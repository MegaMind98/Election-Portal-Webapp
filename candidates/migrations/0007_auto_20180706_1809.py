# Generated by Django 2.0.7 on 2018-07-06 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0006_auto_20180706_1806'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nominee',
            old_name='content_type',
            new_name='Sabha',
        ),
    ]
