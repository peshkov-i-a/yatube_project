from django.shortcuts import render
from django.http import HttpResponse


# Главная страница
def index(reguest):
    return HttpResponse('Главная страница')
