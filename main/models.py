from django.db import models



class TelegramUser(models.Model):
    telegram_id = models.BigIntegerField(unique=True)
    full_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)  # ➕ telefon raqam

    def __str__(self):
        return f"{self.full_name} ({self.phone_number})"
