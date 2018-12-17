from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'api/', include('fosil.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls'))
]
