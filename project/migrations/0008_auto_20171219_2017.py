# Generated by Django 2.0 on 2017-12-19 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_auto_20171219_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Projects', verbose_name='Выберите проект'),
        ),
    ]
