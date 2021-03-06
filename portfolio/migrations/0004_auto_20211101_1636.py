# Generated by Django 3.2.5 on 2021-11-01 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20211101_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='cvlink',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='home',
            name='devtitle',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='home',
            name='profilephoto',
            field=models.ImageField(blank=True, upload_to='portfolio/images/'),
        ),
        migrations.AlterField(
            model_name='home',
            name='socialmedia_github',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='home',
            name='socialmedia_insta',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='home',
            name='socialmedia_linkedin',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='home',
            name='socialmedia_stackoverflow',
            field=models.URLField(blank=True),
        ),
    ]
