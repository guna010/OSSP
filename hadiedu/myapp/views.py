from django.shortcuts import render
from .models import School
import csv

# Create your views here.

def index(request):


    schools = School.objects.filter(code='S050000210')

    context = {
      'schools' : schools
    }
    return render(request, 'myapp/index.html', context)




def input(request):


  return render(request, 'myapp/index.html')