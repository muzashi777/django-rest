# Generated by Django 3.0.4 on 2021-02-18 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20210219_0048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article_image',
            name='description',
        ),
        migrations.AddField(
            model_name='article_content',
            name='title',
            field=models.CharField(default='not set', max_length=15),
        ),
        migrations.AddField(
            model_name='article_image',
            name='title',
            field=models.CharField(default='not set', max_length=15),
        ),
    ]
