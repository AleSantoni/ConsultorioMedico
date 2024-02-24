
from django.contrib import admin
from django.urls import path
from django.urls import include




urlpatterns = [
    path('admin/', admin.site.urls),
    
# url core
      path('', include('core.urls')),

     
# path del Auth
     path('accounts/', include('django.contrib.auth.urls')),
]
