# Generated by Django 2.0 on 2017-12-19 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0011_auto_20171219_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='category',
            field=models.PositiveIntegerField(choices=[(0, 'Дизайн'), (1, 'Разработка')], verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='status_type',
            field=models.PositiveIntegerField(choices=[(0, 'Выполнено'), (1, 'Не выполнено')], default=0, verbose_name='Статус'),
        ),
    ]
