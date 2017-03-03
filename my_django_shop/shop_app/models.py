from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=254, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    parent = models.ForeignKey('self', verbose_name='Родительская категория', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
