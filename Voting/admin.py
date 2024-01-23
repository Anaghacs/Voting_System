from django.contrib import admin

# Register your models here.

from .models import Candidate,Votes

admin.site.register(Candidate)
admin.site.register(Votes)