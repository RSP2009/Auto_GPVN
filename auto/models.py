from django.db import models
from django.urls import reverse


# Create your models here.
class Auto(models.Model):
    marka = models.CharField(max_length=255, verbose_name='Марка, модель')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    gos_number = models.CharField(max_length=10, verbose_name='Гос.№')
    norma = models.FloatField()
    mileage = models.FloatField()
    operating_time = models.FloatField(blank=True)
    driver = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True)
    post = models.CharField(max_length=255, verbose_name='Описание последних работ')
    is_published = models.BooleanField(default=True, verbose_name='Исправна')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')



    def __str__(self):
        return self.driver

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = "Парк техники"
        verbose_name_plural = "Парк техники"
        ordering = ['-time_create', 'marka']



class Category(models.Model):
    objects = None
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})


    class Meta:
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"  # Множественное число
        ordering = ['id']

