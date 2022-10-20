from django.conf import settings
from django.db import models

from ads.validators import check_date_not_past
from django.utils import timezone


class Ad(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Название товара",
        help_text="Введите название товара"
    )

    price = models.PositiveIntegerField(
        verbose_name="Цена товара",
        help_text="Введите цену товара"
    )

    description = models.CharField(
        max_length=1000,
        null=True,
        blank=True,
        verbose_name="Описание товара",
        help_text="Введите описание"
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="ads",
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        null=True,
        default=timezone.now,
        validators=[check_date_not_past]
    )

    image = models.ImageField(
        upload_to="ads/",
        null=True,
        blank=True,
        verbose_name="Фото",
        help_text="Загрузите фото",
    )

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ["created_at"]

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.CharField(
        max_length=1000,
        null=True,
        blank=True,
        verbose_name="Комментарий",
        help_text="Введите комментарий"
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="comments",
        on_delete=models.CASCADE
    )

    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)

    created_at = models.DateTimeField(
        null=True,
        default=timezone.now,
        validators=[check_date_not_past]
    )

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return self.author