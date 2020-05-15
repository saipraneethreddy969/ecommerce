from django.contrib import admin

# Register your models here.
from .models import name,Farmer,crops,actors,movies
admin.site.register(name)
admin.site.register(Farmer)
admin.site.register(crops)
admin.site.register(movies)
admin.site.register(actors)