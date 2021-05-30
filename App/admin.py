from django.contrib import admin

from .models import Song
from .models import Album

# Register your models here.
admin.site.register(Song)
admin.site.register(Album)

# hello