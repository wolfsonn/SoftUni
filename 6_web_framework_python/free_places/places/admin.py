from django.contrib import admin

# Register your models here.
from places.models import Place, Establishment, City

admin.site.register(Place)
admin.site.register(Establishment)
admin.site.register(City)