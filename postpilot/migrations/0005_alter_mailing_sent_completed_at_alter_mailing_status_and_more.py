# Generated by Django 5.1.5 on 2025-02-26 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("postpilot", "0004_alter_mailing_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mailing",
            name="sent_completed_at",
            field=models.DateTimeField(auto_now=True, null=True, verbose_name="Дата завершения отправки"),
        ),
        migrations.AlterField(
            model_name="mailing",
            name="status",
            field=models.CharField(
                choices=[
                    ("completed", "Завершено"),
                    ("created", "Создано"),
                    ("started", "Начато"),
                    ("broken", "Прервано"),
                ],
                default="created",
                max_length=9,
                verbose_name="Статус отправки",
            ),
        ),
        migrations.AlterField(
            model_name="recipient",
            name="full_name",
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name="ФИО"),
        ),
        migrations.AlterField(
            model_name="sendattempt",
            name="status",
            field=models.CharField(
                choices=[("successfully", "Successfully"), ("failed", "Failed")],
                default="failed",
                max_length=12,
                verbose_name="Статус отправки",
            ),
        ),
    ]
