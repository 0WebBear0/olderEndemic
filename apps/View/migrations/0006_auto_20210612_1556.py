# Generated by Django 3.2.4 on 2021-06-12 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('View', '0005_auto_20210612_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firm',
            name='img',
            field=models.ImageField(blank=True, upload_to='Image/', verbose_name='Изображения фирм'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(blank=True, upload_to='Image/'),
        ),
    ]