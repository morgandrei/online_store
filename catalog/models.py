from _datetime import datetime

from django.db import models

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
    updated_at = models.DateTimeField(default=datetime.now, verbose_name='Дата последнего изменения')  # дата последнего изменения

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Contacts(models.Model):
    contact_name = models.CharField(max_length=100, verbose_name='Имя')
    phone = models.CharField(max_length=50, verbose_name='Телефон')
    message = models.TextField(verbose_name='Сообщение')

    def __str__(self):
        return self.contact_name

    class Meta:
        pass
