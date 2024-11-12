
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('usuarios.urls')), 
    path('usuarios/', include('usuarios.urls')),
    path('estoque/', include('estoque.urls'))
]
