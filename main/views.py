from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse

class Main(View):
    def get(self, request):
        return render(request, "main/main.html")

class Cases(View):
    def get(self, request):
        return render(request, "cases/cases.html")
    
class Blog(View):
    def get(self, request):
        return render(request, "blog/blog.html")
        
        