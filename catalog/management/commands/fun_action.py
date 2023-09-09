from django.core.management import BaseCommand

from catalog.models import Products, Categories


class Command(BaseCommand):

    def handle(self, *args, **options):
        products_list = [
            {'product_name': 'Яблоки', 'description': 'Российские яблоки', 'category': 'Овощи, фрукты', 'price': 100},
            {'product_name': 'Макароны', 'description': 'Макароны из муки высшего сорта', 'category': 'Бакалея',
             'price': 124},
            {'product_name': 'Килька', 'description': 'Килька в томатном соусе', 'category': 'Консервы', 'price': 35},
            {'product_name': 'Сахар', 'description': 'Сахар тростниковый', 'category': 'Бакалея', 'price': 70},
            {'product_name': 'Архыз', 'description': 'Питьевая вода высшей категории', 'category': 'Вода', 'price': 55},
            {'product_name': 'Соль', 'description': 'Соль морская, поваренная', 'category': 'Бакалея', 'price': 80},
            {'product_name': 'Nuka-cola', 'description': 'Напиток постапокалиптического мира', 'category': 'Вода',
             'price': 500},

        ]
        Products.objects.all().delete()
        for product in products_list:
            Products.objects.create(**product)

#class Command(BaseCommand):

    #def handle(self, *args, **options):
        #Categories.objects.all().delete()
        #return os.system("python manage.py loaddata data.json")