from django.db import models
from django.contrib.auth.models import AbstractUser
import secrets

# Create your models here.
class BankUser(AbstractUser):
    username = models.CharField(
        max_length=30,
        unique=True,
        verbose_name="Ник пользователя")
    phone_number = models.CharField(
        max_length=15,
        unique=True,
        verbose_name="Номер телефона")
    email = models.EmailField(
        verbose_name='Почта'
    )
    balance = models.IntegerField(verbose_name='Баланс', default=1110)
    wallet_number = models.CharField(max_length=50,
                         verbose_name='Номер кошелька',
                         unique=True)
    created = models.DateTimeField(auto_now_add=True,verbose_name='Дата создания')

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def save(self, *args, **kwargs):
        if not self.wallet_number:
            self.wallet_number = secrets.token_hex(6)
        super().save(*args, **kwargs)