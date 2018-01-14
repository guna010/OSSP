from django.contrib import admin
from django.conf.urls import url
from . import views
app_name = 'handi'
urlpatterns = [
    url('index',views.index ),
<<<<<<< HEAD
    #url('search', views.input, name = 'search')
=======
>>>>>>> de8cb49389d1d8787cb4b81bdf6ab4d37034e73b
]
