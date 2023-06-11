
from django.contrib import admin
from django.urls import path, include
from ninja import NinjaAPI
from django.http import HttpResponse
from django.shortcuts import render
import logging

api = NinjaAPI()

@api.get('/A')
def A(request, ip:str):
  logger = logging.getLogger("django.request")
  message = f"A|{ip}"
  logger.info(message)

  return HttpResponse('hello')

@api.get('/B')
def B(request, ip:str):
  logger = logging.getLogger("django.request")
  message = f"A|{ip}"
  logger.info(message)

  return HttpResponse('hello')

@api.get('/C')
def C(request, ip:str):
  logger = logging.getLogger("django.request")
  message = f"A|{ip}"
  logger.info(message)

  return HttpResponse('hello')

@api.get('/D')
def D(request, ip:str):
  logger = logging.getLogger("django.request")
  message = f"A|{ip}"
  logger.info(message)

  return HttpResponse('hello')

@api.get('/E')
def E(request, ip:str):
  logger = logging.getLogger("django.request")
  message = f"A|{ip}"
  logger.info(message)

  return HttpResponse('hello')

@api.get('/F')
def F(request, ip:str):
  logger = logging.getLogger("django.request")
  message = f"A|{ip}"
  logger.info(message)

  return HttpResponse('hello')

@api.get('/G')
def G(request, ip:str):
  logger = logging.getLogger("django.request")
  message = f"A|{ip}"
  logger.info(message)

  return HttpResponse('hello')

@api.get('/H')
def H(request, ip:str):
  logger = logging.getLogger("django.request")
  message = f"A|{ip}"
  logger.info(message)

  return HttpResponse('hello')

@api.get('/I')
def I(request, ip:str):
  logger = logging.getLogger("django.request")
  message = f"A|{ip}"
  logger.info(message)

  return HttpResponse('hello')

urlpatterns = [
    path('', api.urls)
]
