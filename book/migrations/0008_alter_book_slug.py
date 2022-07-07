# Generated by Django 4.0.3 on 2022-05-21 11:58

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_remove_review_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, null=True, populate_from='title', unique=True),
        ),
    ]
