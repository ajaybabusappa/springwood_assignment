from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('postinput', views.trigerpreferencepage, name='trigerpreferencepage'),
    path('analysereq', views.analysereq, name='analysereq'),
    path('functionality', views.functionality, name='functionality'),
    path('copynumber', views.copynumber, name='copynumber'),
    path('arthematic', views.arthematic, name='arthematic'),
    path('expression', views.expression, name='expression')
]
