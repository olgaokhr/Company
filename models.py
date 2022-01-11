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
    name = models.CharField("Название компании", max_length=200, default="",  blank=False)
    unp = models.CharField("УНП/ИНН", max_length=300, default="",  blank=False)
    text = models.TextField("Описание", max_length=2000, default="", blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, related_name='posts')
    city = models.CharField('Город', max_length=200, default="", blank=False)
    street = models.CharField('Улица', max_length=200, default="", blank=False)
    address = models.CharField('Дом', max_length=200, default="", blank=False)
    dop_address = models.CharField('Номер помещения', max_length=200, default="", blank=True)
    phone = models.CharField("Номер телефона", max_length=200, default="", blank=False)
    email = models.EmailField("E-mail", default="", blank=True)
    site = models.CharField("Сайт", max_length=200, default="", blank=True)
    telegram = models.CharField("Telegram", max_length=200, default="", blank=True)
    viber = models.CharField("Viber", max_length=200, default=" ", blank=True)
    whatsapp = models.CharField("WhatsApp", max_length=200, default="", blank=True)
    instagram = models.CharField("Instagram", max_length=200, default="", blank=True)
    vk = models.CharField("VK", max_length=200, default="", blank=True)
    ok = models.CharField("Одноклассники", max_length=200, default="", blank=True)
    facebook = models.CharField("Facebook", max_length=200, default="", blank=True)
    logo = models.ImageField( "Логотип",
        upload_to='img/',
        blank=True,
        null=True, default='img/default.jpg',
    )
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
    text = models.TextField('Отзыв')
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