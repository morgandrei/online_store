import os

from django.core.management import BaseCommand

from catalog.models import Products, Categories


class Command(BaseCommand):

    def handle(self, *args, **options):
        products_list = [
            {'product_name': 'Яблоки', 'description': 'Российские яблоки', 'category_id': 6, 'price': 100},
            {'product_name': 'Макароны', 'description': 'Макароны из муки высшего сорта', 'category_id': 7,
             'price': 124},
            {'product_name': 'Килька', 'description': 'Килька в томатном соусе', 'category_id': 8, 'price': 35},
            {'product_name': 'Сахар', 'description': 'Сахар тростниковый', 'category_id': 7, 'price': 70},
            {'product_name': 'Архыз', 'description': 'Питьевая вода высшей категории', 'category_id': 9, 'price': 55},
            {'product_name': 'Соль', 'description': 'Соль морская, поваренная', 'category_id': 7, 'price': 80},
            {'product_name': 'Nuka-cola', 'description': 'Напиток постапокалиптического мира', 'category_id': 9,
             'price': 500},

        ]
        Products.objects.all().delete()
        for product in products_list:

            Products.objects.create(**product)

#class Command(BaseCommand):

    #def handle(self, *args, **options):
        #Categories.objects.all().delete()
        #return os.system("python manage.py loaddata data.json")