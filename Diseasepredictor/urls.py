from django.contrib import admin
from django.urls import path, include
from Diseasepredictor import views
urlpatterns=[

    path('',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
    path('reportanalysis/',views.reportanalysis,name='reportanalysis'),

]