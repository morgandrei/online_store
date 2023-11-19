from _datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

NULLABLE = {'blank': True, 'null': True}


class Categories(models.Model):
    category_name = models.CharField(max_length=150, verbose_name='Категория')  # наименование
    description = models.TextField(verbose_name='Описание')  # описание

    #    created_at = models.DateTimeField(default=datetime.now, verbose_name='Дата создания')

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Products(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='Наименование')  # наименование
    description = models.TextField(verbose_name='Описание')  # описание
    product_pic = models.ImageField(upload_to='products', verbose_name='Изображение', **NULLABLE)  # изображение(превью)

    category = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name='Категория')  # категория,
    price = models.IntegerField(verbose_name='Цена')  # цена за покупку
    created_at = models.DateTimeField(default=datetime.now, verbose_name='Дата создания')  # дата создания
    updated_at = models.DateTimeField(default=datetime.now,
                                      verbose_name='Дата последнего изменения')  # дата последнего изменения
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, verbose_name='пользователь', **NULLABLE)
    is_published = models.BooleanField(default=False, verbose_name='признак публикации')

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        permissions = [
            (
                'set_published',
                'Can publish posts'
            )
        ]


class Contacts(models.Model):
    contact_name = models.CharField(max_length=100, verbose_name='Имя')
    phone = models.CharField(max_length=50, verbose_name='Телефон')
    message = models.TextField(verbose_name='Сообщение')

    def __str__(self):
        return self.contact_name

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    slug = models.CharField(max_length=100, verbose_name='slug', **NULLABLE)
    content = models.TextField(verbose_name='содержимое')
    preview = models.ImageField(verbose_name='превью', **NULLABLE)
    created_at = models.DateField(auto_now_add=True, verbose_name='дата создания')
    is_published = models.BooleanField(default=True, verbose_name='признак публикации')
    views_count = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return f'{self.title} ({self.slug})'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'


class Version(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    version_number = models.CharField(max_length=5, verbose_name='номер версии')
    version_name = models.CharField(max_length=150, verbose_name='имя версии')
    is_current = models.BooleanField(default=False, verbose_name='признак текущей версии')

    def __str__(self):
        return f'{self.product.product_name} - {self.version_name}({self.version_number})'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'


@receiver(pre_save, sender=Version)
def update_active_versions(sender, instance, **kwargs):
    if instance.is_current_version:  # Проверяем, если версия становится активной
        Version.objects.filter(product=instance.product).exclude(pk=instance.pk).update(is_current_version=False)
