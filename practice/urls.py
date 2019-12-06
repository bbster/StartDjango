from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),
    path('fbv/', include('fbv.urls')),
    # path('users/', include('users.urls'))
]
