# Generated by Django 2.0 on 2017-12-19 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0010_auto_20171219_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='category',
            field=models.PositiveIntegerField(choices=[(0, 'Д'), (1, 'Дизайн'), (2, 'Р'), (3, 'Разработка')], verbose_name='Категория'),
        ),
    ]
