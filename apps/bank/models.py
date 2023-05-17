from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from apps.users.models import BankUser

class TransferMoney(models.Model):
    from_user = models.ForeignKey(
        BankUser,
        on_delete=models.CASCADE,
        related_name="from_user",
        verbose_name="От пользователя"
    )
    to_user = models.ForeignKey(
        BankUser,
        on_delete=models.CASCADE,
        related_name="to_user",
        verbose_name="Пользователю"
    )
    status = models.BooleanField(
        default=False,
        verbose_name="Статус"
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )
    amount = models.CharField(
        max_length=255,
        verbose_name="Сумма"
    )
    def __str__(self):
        return self.amount 
    
    class Meta:
        verbose_name = "Перевод"
        verbose_name_plural = "Переводы"

