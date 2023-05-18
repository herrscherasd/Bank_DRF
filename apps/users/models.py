from django.db import models
from django.contrib.auth.models import AbstractUser
import secrets

# Create your models here.
class BankUser(AbstractUser):
    username = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Ник пользователя')

    email = models.EmailField(
        verbose_name="Ваша почта",
        unique=True
    )
    phone_number = models.CharField(
        max_length=255,
        verbose_name="Ваш номер телефона"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="дата создания"
    )
    age = models.IntegerField(
        verbose_name="ваш возраст",
        blank = True, null = True
    )
    balance = models.CharField(
        max_length=255,
        verbose_name="Баланс",
        blank = True, null = True,
        default=0
    )
    wallet_address = models.CharField(
        max_length=12,
        verbose_name="Кошелек",
        blank = True, null = True,
        unique=True
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователи"
        verbose_name_plural = "Пользователь"

    def save(self, *args, **kwargs):
        if not self.wallet_address:
            self.wallet_address = secrets.token_hex(6)
        super().save(*args, **kwargs)