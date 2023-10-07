import os

from django.core.management import BaseCommand

from catalog.models import Products, Categories


class Command(BaseCommand):

    def handle(self, *args, **options):
        products_list = [
            {'product_name': 'Apples', 'description': 'Russian apples', 'category_id': 4, 'price': 100, 'product_pic':'apple.jpg'},
            {'product_name': 'Pasta', 'description': 'Pasta made from premium flour', 'category_id': 2, 'price': 124, 'product_pic':'pasta.jpg'},
            {'product_name': 'Sprat', 'description': 'Sprat in tomato sauce', 'category_id': 3, 'price': 35, 'product_pic':'kilka.jpg'},
            {'product_name': 'Sugar', 'description': 'Cane sugar', 'category_id': 2, 'price': 70, 'product_pic':'sugar.jpg'},
            {'product_name': 'Water', 'description': 'Drinking water of the highest category', 'category_id': 1, 'price': 55, 'product_pic':'arkhiz.jpg'},
            {'product_name': 'Salt', 'description': 'Sea salt, table salt', 'category_id': 2, 'price': 80, 'product_pic':'sol.jpg'},
            {'product_name': 'Nuka-cola', 'description': 'Drink of the post-apocalyptic world', 'category_id': 1, 'price': 500, 'product_pic':'coca_cola.jpg'},

        ]
        Products.objects.all().delete()
        for product in products_list:

            Products.objects.create(**product)

#class Command(BaseCommand):

    #def handle(self, *args, **options):
        #Categories.objects.all().delete()
        #return os.system("python manage.py loaddata data.json")