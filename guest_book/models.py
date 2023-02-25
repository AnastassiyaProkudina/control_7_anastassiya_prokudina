from django.db import models
from django.db.models import TextChoices
from django.utils import timezone


class StatusChoice(TextChoices):
    ACTIVE = "ACTIVE", "Активна"
    BLOCKED = "BLOCKED", "Заблокирована"


class GuestBook(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name="Имя")
    email = models.EmailField(
        max_length=254, null=False, blank=False, verbose_name="Email"
    )
    text = models.TextField(
        max_length=3000, null=False, blank=False, verbose_name="Текст"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата и время создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата и время изменения"
    )
    status = models.CharField(
        verbose_name="Status",
        choices=StatusChoice.choices,
        max_length=20,
        default=StatusChoice.ACTIVE,
    )
    is_deleted = models.BooleanField(verbose_name="Удалено", null=False, default=False)
    deleted_at = models.DateTimeField(
        verbose_name="Дата и время удаления", null=True, default=None
    )

    def __str__(self):
        return f"{self.name} - {self.email}"

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
