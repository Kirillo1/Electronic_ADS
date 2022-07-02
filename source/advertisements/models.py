from django.contrib.auth import get_user_model
from django.db import models

STATUS_CHOICES = [('for_moderation', 'на модерацию'), ('rejected', 'отклонено'),
                  ('published', 'опубликовано'), ('delete', 'удалено')]

User = get_user_model()


class Advertisement(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name="Заголовок")
    description = models.TextField(max_length=2000, null=False, blank=False, verbose_name="Контент")
    category = models.ForeignKey('advertisements.Category', verbose_name="Категории", on_delete=models.CASCADE,
                                 related_name='advertisements')
    status = models.CharField(max_length=30, null=False, blank=False, default='на модерацию', choices=STATUS_CHOICES,
                              verbose_name='Статус')
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name='Цена')

    images = models.ImageField(
        verbose_name="Фотография",
        upload_to="uploads/",
        null=True,
        blank=False
    )
    author = models.ForeignKey(User, related_name="advertisements", on_delete=models.SET_DEFAULT,
                               default=1, verbose_name="Автор", )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    published_at = models.DateTimeField(auto_now=True, verbose_name="Дата публикации")
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
