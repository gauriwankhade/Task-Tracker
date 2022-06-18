from django.contrib import admin
from django.apps import apps

model_list = apps.all_models['taskapp']

for key in model_list :
    # Register your models here
    admin.site.register(model_list[key])
