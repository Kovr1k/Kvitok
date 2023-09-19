from django.db import models

class Case(models.Model):
    title = models.CharField("Название", max_length=255, default='')
    img = models.ImageField("Обложка", upload_to='case')
    description = models.TextField("Наполнение", blank=True)
    titleForURL = models.CharField("Преобразование в URL", max_length=255, default='', blank=True)

    def __str__(self):
        return self.title
    