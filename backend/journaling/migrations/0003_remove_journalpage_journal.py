# Generated by Django 4.2.7 on 2023-11-26 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journaling', '0002_journalpage_entry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journalpage',
            name='journal',
        ),
    ]
