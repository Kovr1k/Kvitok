from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.http import HttpResponse
from .models import Case
from transliterate import translit, get_available_language_codes

class Main(View):
    def get(self, request):
        return render(request, "main/main.html")

class Cases(View):
    def get(self, request):
        cases = Case.objects.all()
        
        i=0
        for el in cases:
            # cases[i].titleForURL = cases[i].title.replace(' ', '_')
            cases[i].titleForURL = translit(cases[i].title.replace(' ', '_'), language_code='ru', reversed=True)
            print(cases[i].titleForURL)
            print(cases[i].id)
            i += 1      
            
        data = {
            'cases': cases,
        }
        return render(request, "cases/cases.html", data)
    
class Blog(View):
    def get(self, request):
        return render(request, "blog/blog.html")
    
class Error(View):
    def get(self, request):
        return render(request, "error/errorPage.html")
        
class CasePage(View):
    def get(self, request, id, titleForURL):
        id = int(id)
        titleForURL = str(titleForURL)
        data = None

        if(id == None):
            return redirect('error')

        data = Case.objects.filter(id = id)
        
        try:
            if(titleForURL != translit(data[0].title.replace(' ', '_'), language_code='ru', reversed=True)):
                return redirect('error')
        except:
            return redirect('error')   

        context = {
            'titleForURL': titleForURL,
            'data' : data
        }
        return render(request, "cases/caseObject/caseObject.html", context=context)