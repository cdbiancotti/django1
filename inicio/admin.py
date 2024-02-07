from django.contrib import admin
from inicio.models import Alumno

# v1
admin.site.register(Alumno)
# admin.site.register(OtroModelo)

# v2
# admin.site.register([Alumno, OtroModelo])