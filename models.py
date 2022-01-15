from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Category(models.Model):
    """Category model."""
    title = models.CharField(max_length=80, blank=True, help_text='Long <= 80 simbols', verbose_name='SEO Title', )
    description = models.CharField(max_length=160, blank=True, help_text='Long <= 160 simbols',
                                   verbose_name='SEO description', )

    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(blank=True, unique=True)
    category = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, related_name='children')

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('company_category', args=[str(self.name)])


class Country(models.Model):
    """Category model."""
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(blank=True)


    class Meta:
        ordering = ['name']
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('company_country', args=[str(self.name)])


class Post(models.Model):
    title = models.CharField(max_length=80, blank=True, help_text='Long <= 80 simbols', verbose_name='SEO Title',
                             )
    description = models.CharField(max_length=160, blank=True, help_text='Long <= 160 simbols',
                                   verbose_name='SEO description',  )

    created_by = models.ForeignKey( User, on_delete=models.CASCADE, null=True, blank=True,)
    name = models.CharField(max_length=200, blank=False)
    unp = models.CharField(max_length=300, blank=False, help_text='*Обязательное поле. Пример: УНПххххххх')
    text = models.TextField(max_length=2000,  blank=True )
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, related_name='posts', help_text='*Обязательное поле')
    city = models.CharField(max_length=200, blank=False, help_text='*Обязательное поле')
    street = models.CharField(max_length=200, blank=False, help_text='*Обязательное поле')
    address = models.CharField(max_length=200, blank=False, help_text='*Обязательное поле, указывается только улица')
    dop_address = models.CharField(max_length=200, blank=True, help_text='*Номер помещения, офиса и т.д.')
    phone = models.CharField(max_length=200, blank=False, help_text='*Обязательное поле. Пример: +375ххххххх')
    email = models.EmailField(blank=True)
    site = models.CharField( max_length=200, blank=False, help_text='*Обязательное поле. Пример: https:name.com')
    telegram = models.CharField(max_length=200, blank=True)
    viber = models.CharField(max_length=200, blank=True)
    whatsapp = models.CharField(max_length=200, blank=True)
    instagram = models.CharField(max_length=200, blank=True)
    vk = models.CharField(max_length=200, blank=True)
    ok = models.CharField( max_length=200, blank=True)
    facebook = models.CharField( max_length=200, blank=True)
    logo = models.ImageField(upload_to='img/', blank=True, null=True, default='img/default.jpg',)
    categories = models.ManyToManyField(Category, related_name='posts')
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class Comment(models.Model):
    post = models.ForeignKey('company.Post', on_delete=models.CASCADE, default="", related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField( default="")
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['created_date']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


def approved_comments(self):
    return self.comments.filter(approved_comment=True)