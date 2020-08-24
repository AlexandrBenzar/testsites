from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(verbose_name='Наименование', max_length=150)
    content = models.TextField(verbose_name='Контент', blank=True)
    created_at = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Обновлено', auto_now=True)
    photo = models.ImageField(verbose_name='Фото', upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(verbose_name='Опубликовано', default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    views_count = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('view_news', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(verbose_name='Наименование категории', max_length=150, db_index=True)

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
        ordering = ['title']
