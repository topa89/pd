# Generated by Django 2.0 on 2017-12-19 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_auto_20171219_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='category',
            field=models.CharField(choices=[('Д', 'Дизайн'), ('Р', 'Разработка')], default='Д', max_length=1, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='importance_type',
            field=models.CharField(choices=[('В', 'Высокая'), ('С', 'Средняя'), ('Н', 'Низкая')], default=0, max_length=1, verbose_name='Важность'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='status_type',
            field=models.CharField(choices=[('В', 'Выполнено'), ('НВ', 'Не выполнено')], default='НВ', max_length=1, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='student',
            field=models.CharField(max_length=64, verbose_name='Студент'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='title',
            field=models.CharField(max_length=40, verbose_name='Название'),
        ),
    ]
