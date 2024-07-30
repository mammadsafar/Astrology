from django.db import models
from django.utils.html import mark_safe
from django.utils.html import strip_tags

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Home(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    persianName = models.CharField(verbose_name='نام فارسی', max_length=120)
    nationalName = models.CharField(verbose_name='نام انگلیسی', max_length=120)
    description = RichTextUploadingField(verbose_name='توضیحات', )

    created_at = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='تاریخ ویرایش', auto_now=True)

    def __str__(self):
        return self.persianName
    
    def removed_description_tag(self):
        return strip_tags(self.description)

    class Meta:
        verbose_name = 'خانه'
        verbose_name_plural = 'خانه ها'
        ordering = ['-created_at']


class Zodiac(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    persianName = models.CharField(verbose_name='نام فارسی', max_length=120)
    nationalName = models.CharField(verbose_name='نام انگلیسی', max_length=120)
    sign = models.CharField(verbose_name='علامت', max_length=120)

    description = RichTextUploadingField(verbose_name='توضیحات', )
    image = models.ImageField(verbose_name='تصویر', upload_to='chart/zodiac', blank=True)

    created_at = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='تاریخ ویرایش', auto_now=True)
    def image_tag(self):
            return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.image))
    image_tag.allow_tags = True
    image_tag.short_description = 'Image'

    def __str__(self):
        return self.persianName + ' - ' + self.nationalName
    
    def removed_description_tag(self):
        return strip_tags(self.description)
        
    class Meta:
        verbose_name = 'زودیاک'
        verbose_name_plural = 'زودیاک ها'
        ordering = ['-created_at']


class Plant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    persianName = models.CharField(verbose_name='نام فارسی', max_length=120)
    nationalName = models.CharField(verbose_name='نام انگلیسی', max_length=120)
    
    description = RichTextUploadingField(verbose_name='توضیحات', )

    reinforcement = models.ManyToManyField(Zodiac, verbose_name='تقویت', blank=True, null=True)
    reinDescription = models.TextField(verbose_name='توضیحات تقویت', max_length=3000, blank=True, null=True)

    image = models.ImageField(verbose_name='تصویر', upload_to='chart/plant', blank=True)


    created_at = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='تاریخ ویرایش', auto_now=True)

    def image_tag(self):
            return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.image))
    image_tag.allow_tags = True
    image_tag.short_description = 'Image'

    def get_reinforcement(self):
        return ', '.join(str(p.nationalName) for p in self.reinforcement.all())
    get_reinforcement.short_description = 'تقویت'
        # return "\n".join([p.reinforcement for p in self.reinforcement.all()])

    def __str__(self):
        return self.persianName
    
    def removed_description_tag(self):
        return strip_tags(self.description)
        
    class Meta:
        verbose_name = 'سیاره'
        verbose_name_plural = 'سیاره ها'
        ordering = ['-created_at']


class PlantLayer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    persianName = models.CharField(verbose_name='نام فارسی', max_length=120)
    nationalName = models.CharField(verbose_name='نام انگلیسی', max_length=120)
    description = RichTextUploadingField(verbose_name='توضیحات', )

    created_at = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='تاریخ ویرایش', auto_now=True)

    def __str__(self):
        return self.persianName
    
    def removed_description_tag(self):
        return strip_tags(self.description)
        
    class Meta:
        verbose_name = 'لایه'
        verbose_name_plural = 'لایه ها'
        ordering = ['-created_at']



class Detail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='نام', max_length=120, blank=True, null=True)

    plant = models.ForeignKey(Plant, verbose_name='سیاره', on_delete=models.PROTECT, blank=True, null=True)
    plantLayer = models.ForeignKey(PlantLayer, verbose_name='لایه سیاره', on_delete=models.PROTECT, blank=True, null=True)
    zodiac = models.ForeignKey(Zodiac, verbose_name='زودیاک', on_delete=models.PROTECT, blank=True, null=True)
    home = models.ForeignKey(Home, verbose_name='خانه', on_delete=models.PROTECT, blank=True, null=True)

    description = RichTextUploadingField(verbose_name='توضیحات', )

    created_at = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='تاریخ ویرایش', auto_now=True)

    def __str__(self):
        return self.name
    
    def removed_description_tag(self):
        return strip_tags(self.description)
        
    class Meta:
        verbose_name = 'جزییات'
        verbose_name_plural = 'جزییات ها'
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if self.plant and self.zodiac:
            self.name = f"{self.plant.nationalName} in {self.zodiac.nationalName}"
        
        super().save(*args, **kwargs)
    
    


class Psychology(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='نام', max_length=120)

    detail = models.ManyToManyField(Detail, verbose_name='خانه')

    description = RichTextUploadingField(verbose_name='توضیحات', )

    created_at = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='تاریخ ویرایش', auto_now=True)

    def __str__(self):
        return self.persianName
    
    def removed_description_tag(self):
        return strip_tags(self.description)
        
    class Meta:
        verbose_name = 'نکته روانشناسی'
        verbose_name_plural = 'نکات روانشناسی'
        ordering = ['-created_at']

