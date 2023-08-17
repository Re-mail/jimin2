from django.contrib import admin
from .models import Remail


admin.site.register(Remail)

class RemailAdmin(admin.ModelAdmin):
    list_display = ['user', 'remail1', 'remail2', 'remail3', 'remail4', 'remail5', 'category1', 'category2', 'category3', 'category4', 'category5']