# Generated by Django 4.1.7 on 2023-09-26 17:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0005_new"),
    ]

    operations = [
        migrations.AddField(
            model_name="case",
            name="description",
            field=models.TextField(blank=True, verbose_name="Наполнение"),
        ),
    ]