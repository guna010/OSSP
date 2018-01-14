from django.shortcuts import render
from .models import School
import csv
# Create your views here.
def index(request):

    line = []
    line1 = []

    f = open('학교정보.csv', 'r')
    #f1 = open('장애인편의.csv', 'r')
    rdr = csv.reader(f)
    #rdr1 = csv.reader(f1)

        #for row in rdr1:
           #line1.append(row)

    schools = School.objects.all()
    context = {
        'schools':schools
    }

    return render(request, 'myapp/index.html', context)
