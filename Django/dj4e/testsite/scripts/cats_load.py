import csv
from cats.models import Cat2, Breed


# python manage.py runscript cats_load

def run():
    fhand = open('cats/meow.csv')
    reader = csv.reader(fhand)
    next(reader)

    Cat2.objects.all().delete()
    Breed.objects.all().delete()

    # Name, Breed, Weight
    # Abby, Sphinx, 6.4
    # Annie, Burmese, 7.6
    # Ash, Manx, 7.8

    for row in reader:
        print(row)
        b, created = Breed.objects.get_or_create(name=row[1])
        c = Cat2(nickname=row[0], breed=b, weight=row[2])
        c.save()

