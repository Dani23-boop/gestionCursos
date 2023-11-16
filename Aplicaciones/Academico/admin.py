from django.contrib import admin
from .models import Curso

# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    
    """admin model Entry"""
    list_display=(
        'Codigo',
        'Nombre',
        'NumCreditos',
    )
    #

admin.site.register(Curso)