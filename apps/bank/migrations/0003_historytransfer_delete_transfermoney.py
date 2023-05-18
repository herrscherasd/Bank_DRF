# Generated by Django 4.2.1 on 2023-05-18 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoryTransfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_completed', models.BooleanField(default=False, verbose_name='Статус')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('amount', models.CharField(max_length=255, verbose_name='Количество')),
            ],
            options={
                'verbose_name': 'История',
                'verbose_name_plural': 'История',
            },
        ),
        migrations.DeleteModel(
            name='TransferMoney',
        ),
    ]
