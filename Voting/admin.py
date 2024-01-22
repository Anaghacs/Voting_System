from django.contrib import admin

# Register your models here.

from .models import Candidate,Vote

admin.site.register(Candidate)
admin.site.register(Vote)