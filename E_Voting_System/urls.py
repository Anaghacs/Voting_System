#This urls page is project urls page. This page is denoted by app urls.

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include('Voting.urls'))
]