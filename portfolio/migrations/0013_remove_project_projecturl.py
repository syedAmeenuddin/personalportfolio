# Generated by Django 3.2.5 on 2021-11-07 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0012_alter_project_describe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='projecturl',
        ),
    ]