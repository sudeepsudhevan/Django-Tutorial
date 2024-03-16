from django.contrib import admin
from .models import Actor, CensorInfo, Director, MovieInfo

# Register your models here.
admin.site.register(MovieInfo)
admin.site.register(CensorInfo)
admin.site.register(Actor)
admin.site.register(Director)
