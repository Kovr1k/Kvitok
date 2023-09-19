# Generated by Django 4.1.7 on 2023-09-19 15:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="case",
            name="titleForURL",
            field=models.CharField(
                default="", max_length=255, verbose_name="Преобразование в URL"
            ),
        ),
        migrations.AlterField(
            model_name="case",
            name="description",
            field=models.TextField(blank=True, verbose_name="Наполнение"),
        ),
        migrations.AlterField(
            model_name="case",
            name="img",
            field=models.ImageField(upload_to="case", verbose_name="Обложка"),
        ),
        migrations.AlterField(
            model_name="case",
            name="title",
            field=models.CharField(default="", max_length=255, verbose_name="Название"),
        ),
    ]
