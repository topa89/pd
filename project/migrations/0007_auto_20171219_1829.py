# Generated by Django 2.0 on 2017-12-19 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_auto_20171219_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='category',
            field=models.CharField(choices=[('Д', 'Дизайн'), ('Р', 'Разработка')], default='Д', max_length=1),
        ),
    ]
