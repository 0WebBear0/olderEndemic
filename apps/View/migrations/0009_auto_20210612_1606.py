# Generated by Django 3.2.4 on 2021-06-12 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('View', '0008_auto_20210612_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='firm',
            name='descrip',
            field=models.CharField(default='Нет описания', max_length=20, verbose_name='Описание фирм'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='firm',
            name='place',
            field=models.CharField(default=1, max_length=20, verbose_name='Расположение фирм'),
            preserve_default=False,
        ),
    ]
