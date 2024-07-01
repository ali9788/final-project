from django.contrib import admin
from .models import *

admin.site.register([Car, Service, AzService, RuService, Slide, Contact,])
