from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cbv/', include('cbv.urls')),
    path('fbv/', include('fbv.urls')),
    # path('users/', include('users.urls'))
]
