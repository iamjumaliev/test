from django.db import models


STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]

class Plan(models.Model):


    description = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Описание')

    full_description = models.TextField(max_length=3000, null=True, blank=False,verbose_name='Полное описание')

    deadline = models.DateField(null=True, blank=False, default='Unknown', verbose_name='Дата выполнения')

    status = models.CharField(max_length=20, verbose_name='статус', default=STATUS_CHOICES[0][0],
                              choices=STATUS_CHOICES)


    def __str__(self):
        return self.description
