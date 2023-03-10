# Generated by Django 4.1.7 on 2023-02-25 07:40

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="GuestBook",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200, verbose_name="Имя")),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                ("text", models.TextField(max_length=3000, verbose_name="Текст")),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата и время создания"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Дата и время изменения"
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("ACTIVE", "Активна"), ("BLOCKED", "Заблокирована")],
                        default="ACTIVE",
                        max_length=20,
                        verbose_name="Status",
                    ),
                ),
                (
                    "is_deleted",
                    models.BooleanField(default=False, verbose_name="Удалено"),
                ),
                (
                    "deleted_at",
                    models.DateTimeField(
                        default=None, null=True, verbose_name="Дата и время удаления"
                    ),
                ),
            ],
        ),
    ]
