# Generated by Django 4.2.7 on 2023-12-06 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journaling', '0008_alter_journal_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journalpage',
            name='prompt',
            field=models.CharField(max_length=450),
        ),
    ]
