from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель для хранения данных пользователя"""
    UZ = 'uz'
    RU = 'ru'
    EN = 'en'
    LANGUAGES_CHOICES = (
        (UZ, 'uz'),
        (RU, 'ru'),
        (EN, 'en'),
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    language = models.CharField(max_length=2, choices=LANGUAGES_CHOICES, default=UZ)
    roles = models.ManyToManyField("users.Role", blank=True)

    def get_full_name(self):
        """Функция возвращает полный инициал"""
        return f"{self.first_name} {self.last_name} {self.middle_name}"

    def __str__(self):
        return f"{self.username}"
