from django.db import models

# Create your models here.
class Name(models.Model):
    sex_choices = [
        ('boy', 'Boy'),
        ('girl', 'Girl'),
    ]

    name = models.CharField(verbose_name='نام', max_length=120, unique=True)
    persian_name = models.CharField(verbose_name='نام فارسی', max_length=120, blank=True, null=True)
    gender = models.CharField(verbose_name='جنسیت', max_length=120, choices=sex_choices) 
    country = models.CharField(verbose_name='کشور', max_length=120, blank=True, null=True)
    nationality = models.CharField(verbose_name='ملیت', max_length=120, blank=True, null=True)
    Usage_percentage = models.CharField(verbose_name='استفاده', max_length=120, blank=True, null=True)
    pronunciation = models.CharField(verbose_name='تلفط', max_length=120, blank=True, null=True)
    meaning = models.CharField(verbose_name='معنی', max_length=120, blank=True, null=True)

    desteni_number = models.CharField(verbose_name='عدد تقدیر', max_length=120, blank=True, null=True)
    motivation_number = models.CharField(verbose_name='عدد روح', max_length=120, blank=True, null=True)

    created_at = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='تاریخ ویرایش', auto_now=True)

    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name = 'نام'
        verbose_name_plural = 'اسامی'
        # ordering = ['-created_at']
