# Generated by Django 2.2 on 2019-12-14 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20191214_0646'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='likes',
            field=models.PositiveIntegerField(default=0, verbose_name='Лайки'),
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
