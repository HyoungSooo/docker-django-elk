
from django.contrib import admin
from django.urls import path, include
from ninja import NinjaAPI
from django.http import HttpResponse
from django.shortcuts import render
import logging

api = NinjaAPI()

@api.get('/test')
def test(request, ip:str):
  logger = logging.getLogger("django.request")
  message = f"user visits index()|{ip}"
  logger.info(message)
  

  return HttpResponse('hello')


urlpatterns = [
    path('', api.urls)
]
