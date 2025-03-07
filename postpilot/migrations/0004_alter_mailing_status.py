# Generated by Django 5.1.5 on 2025-02-26 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("postpilot", "0003_alter_mailing_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mailing",
            name="status",
            field=models.CharField(
                choices=[
                    ("completed", "Completed"),
                    ("created", "Created"),
                    ("started", "Started"),
                    ("broken", "Broken"),
                ],
                default="created",
                max_length=9,
                verbose_name="Статус отправки",
            ),
        ),
    ]
