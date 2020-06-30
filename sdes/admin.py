from django.contrib import admin
from .models import Input

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Input, AuthorAdmin)
