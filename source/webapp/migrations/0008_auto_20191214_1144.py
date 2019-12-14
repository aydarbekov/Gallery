# Generated by Django 2.2 on 2019-12-14 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(max_length=50, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='like',
            name='like',
            field=models.IntegerField(default=1, verbose_name='лайк'),
        ),
    ]