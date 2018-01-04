from django.db import models


# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"Название")

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"


class Projects(models.Model):
    title = models.CharField(max_length=64, verbose_name=u"Название")
    description = models.CharField(max_length=64, verbose_name=u"Описание")
    deadline = models.CharField(max_length=20, verbose_name=u"Срок сдачи")
    kurator = models.CharField(max_length=64, verbose_name=u"Куратор")

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"


class TodoList(models.Model):
    CATEGORY = tuple(enumerate(
        (u"Дизайн",
         u"Разработка",
         )
    )
    )
    IMPORTANCE = tuple(enumerate(
        (u"Высокая",
         u"Средняя",
         u"Низкая",
         )
    )
    )
    STATUS = tuple(enumerate(
        (u"Выполнено",
         u"Не выполнено",
         )
    )
    )
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, verbose_name=u"Выберите проект")
    category = models.PositiveIntegerField(choices=CATEGORY, default=0, verbose_name=u"Категория")
    title = models.CharField(max_length=40, verbose_name=u"Название")
    description = models.TextField(verbose_name=u"Описание")
    student = models.CharField(max_length=64, verbose_name=u"Студент")
    importance_type = models.PositiveIntegerField(choices=IMPORTANCE, default=2, verbose_name=u"Важность")
    status_type = models.PositiveIntegerField(choices=STATUS, default=1, verbose_name=u"Статус")

    def __str__(self):
        return '{}: {}'.format(self.project, self.title)

    class Meta:
        verbose_name_plural = "Задачи для проектов"
