# Generated by Django 3.2.5 on 2021-11-06 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_project_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='describe',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='project',
            name='language',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='project',
            name='projectliveurl',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='projectsourcecodeurl',
            field=models.URLField(blank=True),
        ),
    ]
