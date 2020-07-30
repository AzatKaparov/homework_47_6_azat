from django.db import models

STATUS_CHOICES = [
    ('new', 'Новая'),
    ('in_progress', 'В процессе'),
    ('done', 'Выполнено')
]


class Task(models.Model):
    description = models.TextField(max_length=500, null=False, verbose_name='Описание')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, null=False, default='new', verbose_name='Статус')
    date = models.DateField(null=True, default=None, verbose_name='Дата выполнения (ГГГГ-ММ-ДД)')
    more = models.TextField(max_length=1500, null=True, verbose_name='Более подробное описание задачи')

    def __str__(self):
        return "{}. {}".format(self.pk, self.description)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'