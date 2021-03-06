# Generated by Django 2.2 on 2019-12-14 06:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pics', verbose_name='Фотография')),
                ('description', models.TextField(max_length=2000, verbose_name='Подпись')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('author_name', models.CharField(max_length=50, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Фотография',
                'verbose_name_plural': 'Фотографии',
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.PositiveIntegerField()),
                ('photo', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='webapp.Photo', verbose_name='Лайки')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=400, verbose_name='Текст')),
                ('author', models.CharField(max_length=40, verbose_name='Автор')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('Photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Photo', verbose_name='Фотография')),
            ],
        ),
    ]
