from django.contrib import admin

# Register your models here.
from gestionusuarios.models import registro,usuariooperador
admin.site.register(registro)
admin.site.register(usuariooperador)
