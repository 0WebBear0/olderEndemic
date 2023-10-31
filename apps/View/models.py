from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name='Категории')

    def __str__(self):
        return self.name

class Firm(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название фирм')
    descrip = models.CharField(max_length=200, verbose_name='Описание фирм')
    categor = models.ManyToManyField(Category,verbose_name='Категории производства')
    place = models.CharField(max_length=50, verbose_name='Расположение фирм')
    img = models.ImageField(upload_to="Image/", verbose_name='Изображения фирм',blank=True,default="Shop/static/img/1.jpg")
    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    firmName = models.ForeignKey(Firm,max_length=25,on_delete=models.CASCADE, verbose_name='Название Фирмы')
    name = models.CharField(max_length=25, verbose_name='Название продукта')
    Description = models.CharField(max_length=1000, verbose_name='Описание продукта')
    price = models.IntegerField()
    img = models.ImageField(upload_to="Image/",blank=True,default="Shop/static/img/1.jpg")
    def __str__(self):
        return self.name