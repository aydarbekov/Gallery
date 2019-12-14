from django.conf import settings
from django.db import models


class Photo(models.Model):
    image = models.ImageField(null=False, blank=False, upload_to='pics', verbose_name='Фотография')
    description = models.TextField(null=False, blank=False, max_length=2000, verbose_name='Подпись')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    likes = models.PositiveIntegerField(default=0, verbose_name='Лайки')
    author_name = models.CharField(null=False, blank=False, max_length=50, verbose_name='Автор')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


class Comment(models.Model):
    text = models.TextField(null=False, blank=False, max_length=400, verbose_name='Текст')
    Photo = models.ForeignKey('webapp.Photo', null=False, blank=False,
                                on_delete=models.CASCADE, verbose_name='Фотография', related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return self.text[:20]


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='likes',
                             on_delete=models.CASCADE)
    photo = models.ForeignKey('Photo', verbose_name='Фото', on_delete=models.CASCADE, related_name='likes_status')
    like = models.BooleanField(default=False, verbose_name='Статус лайка')

    def __str__(self):
        return self.like