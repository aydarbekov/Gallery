# Generated by Django 2.2 on 2019-12-14 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20191214_0645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='Photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='webapp.Photo', verbose_name='Фотография'),
        ),
    ]
