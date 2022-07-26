from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Advertisement(models.Model):
    TO_MODERATE = 'MOD'
    PUBLISHED = 'PUB'
    REJECTED = 'REJ'
    TO_DELETE = 'DEL'

    STATUS_CHOICES = [
        (TO_MODERATE, 'На модерацию'), (PUBLISHED, 'Опубликовано'),
        (REJECTED, 'Отклонено'), (TO_DELETE, 'На удаление')
    ]

    title = models.CharField(max_length=200, null=False, blank=False, verbose_name="Заголовок")
    description = models.TextField(max_length=2000, null=False, blank=False, verbose_name="Контент")
    category = models.ForeignKey('advertisements.Category', verbose_name="Категории", on_delete=models.CASCADE,
                                 related_name='advertisements')
    status = models.CharField(max_length=30, default=TO_MODERATE, choices=STATUS_CHOICES,
                              verbose_name='Статус')
    price = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True, verbose_name='Цена')

    images = models.ImageField(
        verbose_name="Фотография",
        upload_to="uploads/",
        null=True,
        blank=False
    )
    author = models.ForeignKey(User, related_name="advertisements", on_delete=models.SET_DEFAULT,
                               default=1, verbose_name="Автор", )
    likes = models.ManyToManyField(User, related_name="liked_ads")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    published_at = models.DateTimeField(null=True, blank=True, verbose_name="Дата публикации")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    def __str__(self):
        return f"{self.title}: {self.author}: {self.description}: {self.category}: {self.status}: {self.price}"

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


class Category(models.Model):
    name = models.CharField(max_length=40, verbose_name="Категория")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Comment(models.Model):
    advertisement = models.ForeignKey("advertisements.Advertisement", on_delete=models.CASCADE,
                                      related_name="comments", verbose_name="Объявление", )
    author = models.ForeignKey(User, related_name="comments",
                               on_delete=models.CASCADE, verbose_name="Автор")
    content = models.TextField(max_length=1000, verbose_name="Контент")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    def __str__(self):
        return f"{self.content}. {self.author}"

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
