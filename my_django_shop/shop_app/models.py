from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=254, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    parent = models.ForeignKey('self', null=True, blank=True, verbose_name='Родительская категория')
    order = models.IntegerField(default=1, verbose_name='Порядок показа')
    alias = models.SlugField(max_length=100, verbose_name='Псевдоним для url', default='')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class CategoryMPTT(MPTTModel):
    title = models.CharField(max_length=50, unique=True, verbose_name='Наименование')
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, verbose_name='Родительская категория')

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'