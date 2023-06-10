from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
import logging
from ninja import NinjaAPI


def index(request):
  logger = logging.getLogger("loggers")
  message = {
    'message' : "user visits index()"
  }
  logger.info(message)
  return HttpResponse("hello")