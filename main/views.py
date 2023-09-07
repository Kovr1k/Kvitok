from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse

class Main(View):
    def get(self, request):
        return render(request, "base.html")
        
        