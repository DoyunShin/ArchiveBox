# Generated by Django 5.0.6 on 2024-08-20 03:42

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0059_tag_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
