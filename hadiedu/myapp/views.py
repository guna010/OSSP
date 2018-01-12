from django.shortcuts import render
from .models import School
import csv
# Create your views here.
def index(request):

    matrix = []

    f = open('학교정보.csv', 'r')

    csvReader = csv.reader(f)
    for row in csvReader:
        matrix = row
    school = School(
        code = matrix[3]
    )
    school.save()
    schools = School.objects.all()
    f.close()
    context = {'schools':schools}
    return render(request , 'myapp/index.html', context)
