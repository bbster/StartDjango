from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),
    path('myapp2/', include('myapp2.urls')),
    # path('users/', include('users.urls'))
]
