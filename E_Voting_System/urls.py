#This urls page is project urls page. This page is denoted by app urls.

from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static
# from E_Voting_System import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include('Voting.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)