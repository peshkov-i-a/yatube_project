from django.shortcuts import render
from django.http import HttpResponse


# Страница с группами
def group_posts(request):
    return HttpResponse('Группы')
