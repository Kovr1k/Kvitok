from django.contrib import admin
from .models import Case

# class TestCase(admin.ModelAdmin):
#     description = ('date_started',),
#     titleForURL = ('date_started',)

admin.site.register(Case)