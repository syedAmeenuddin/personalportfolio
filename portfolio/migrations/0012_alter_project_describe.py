# Generated by Django 3.2.5 on 2021-11-06 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_auto_20211106_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='describe',
            field=models.TextField(blank=True),
        ),
    ]