from django.db import models

class Case(models.Model):
    title = models.CharField("Название", max_length=100, default='')
    img = models.ImageField("Обложка", upload_to='case')
    description = models.TextField("Наполнение", max_length=999, blank=True)

    def __str__(self):
        return self.title
    