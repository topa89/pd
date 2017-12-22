# Generated by Django 2.0 on 2017-12-19 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_todolist_importance_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='status_type',
            field=models.CharField(choices=[('В', 'Выполнено'), ('НВ', 'Не выполнено')], default=1, max_length=1),
        ),
    ]
