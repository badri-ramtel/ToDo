# Generated by Django 4.2.1 on 2023-05-17 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['updated_date'], 'verbose_name_plural': 'todo'},
        ),
    ]
